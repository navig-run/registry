<#
    devtools.ps1 - unified devtools-space engine (Windows / PowerShell 5.1 or 7+).

    Usage:  devtools.ps1 <command> [--flags]
    The same engine backs three surfaces: `navig skill run`, the agent skill_run
    tool, and the Windows right-click menu (via bin/menu + run-hidden.vbs).

    Commands:
      Compress (multi-select aware): extract-here | extract-folder | zip | 7z | 7z-split | open
      Copy:      copy-tree | copy-folders | copy-files | copy-sizes | copy-contents
      Git:       clone [--url <u>] | open-repo
      Download:  video | image
      Dev:       npm | docker
      Remote:    ssh | upload | deploy
      Other:     virustotal | shorten
      Meta:      doctor | help

    Common flags:  --target <path>   the file/folder acted on (context-menu %1 / %V)
    Destructive/remote commands prompt before acting. ASCII-only source.

    NOTE: no param()/[CmdletBinding()] block on purpose - reading $args raw keeps
    GNU-style "--flag value" literal (an advanced function would eat "--out" etc.).
#>

$Command = if ($args.Count -ge 1) { [string]$args[0] } else { 'help' }
$Rest    = if ($args.Count -ge 2) { [string[]]$args[1..($args.Count - 1)] } else { @() }

. "$PSScriptRoot\DevTools-Common.ps1"

# tiny flag parser:  --key value  /  --flag (boolean)
function Get-Flag([string]$name, $default = $null) {
    for ($i = 0; $i -lt $Rest.Count; $i++) {
        if ($Rest[$i] -eq "--$name") {
            if ($i + 1 -lt $Rest.Count -and $Rest[$i + 1] -notlike '--*') { return $Rest[$i + 1] }
            return $true
        }
    }
    return $default
}

$Target = Get-Flag 'target'
$Batch  = Get-Flag 'batch'

# =====================================================================
# Compress helpers (worker side)
# =====================================================================
$ArchiveExt = @('.zip','.7z','.rar','.tar','.gz','.tgz','.bz2','.tbz','.xz','.txz',
                '.zst','.lz','.lzma','.cab','.iso','.wim','.arj','.z','.001','.lzh')
function Test-IsArchive([string]$Path) { $ArchiveExt -contains ([System.IO.Path]::GetExtension($Path)).ToLower() }
function Get-ArchiveBase([string]$Path) {
    $name = [System.IO.Path]::GetFileName($Path)
    foreach ($d in @('.tar.gz','.tar.bz2','.tar.xz','.tar.zst')) {
        if ($name.ToLower().EndsWith($d)) { return $name.Substring(0, $name.Length - ($d.Length - 4)) }
    }
    return [System.IO.Path]::GetFileNameWithoutExtension($name)
}

function Invoke-CompressBatch {
    param([Parameter(Mandatory)][string]$Mode, [Parameter(Mandatory)][string]$ListFile)
    $z7 = Assert-Tool '7z'
    $items = @(Read-BatchList -ListFile $ListFile | Where-Object { Test-Path -LiteralPath $_ })
    $titles = @{ extract_here='Extract Here'; extract_folder='Extract to Folder'; zip='Add to .zip';
                 sevenz='Add to .7z'; sevenz_split='Add to .7z (split 4 GB)' }
    Write-Banner ("Compress  -  {0}  -  {1} item(s)" -f $titles[$Mode], $items.Count)
    Write-AuditLog ("WORKER  mode=$Mode  items=" + $items.Count)
    if ($items.Count -eq 0) { Write-Err 'No valid items.'; Read-Close; return }
    $parent = [System.IO.Path]::GetDirectoryName($items[0])

    if ($Mode -eq 'zip' -or $Mode -eq 'sevenz' -or $Mode -eq 'sevenz_split') {
        if ($items.Count -eq 1) {
            if (Test-Path -LiteralPath $items[0] -PathType Container) { $base = [System.IO.Path]::GetFileName($items[0]) }
            else { $base = [System.IO.Path]::GetFileNameWithoutExtension($items[0]) }
        } else { $base = [System.IO.Path]::GetFileName($parent); if (-not $base) { $base = 'archive' } }
        $ext = if ($Mode -eq 'zip') { '.zip' } else { '.7z' }
        $out = Join-Path $parent ($base + $ext); $i = 1
        while (Test-Path -LiteralPath $out) { $out = Join-Path $parent ($base + "_$i" + $ext); $i++ }
        $a = @('a'); if ($Mode -eq 'zip') { $a += '-tzip' } else { $a += '-t7z' }
        $a += '-mx=5'; if ($Mode -eq 'sevenz_split') { $a += '-v4g' }
        $a += '-bso0'; $a += '-bsp0'      # quiet 7-Zip chatter; our UI carries progress
        $a += $out; $a += $items
        Write-Step "Creating archive: $out"; Write-Info ("Items: " + $items.Count); Write-Host ''
        & $z7 @a
        if ($LASTEXITCODE -eq 0) { Write-Ok "Done: $out" } else { Write-Err ("7-Zip exit code " + $LASTEXITCODE) }
    }
    else {
        $arch = @($items | Where-Object { Test-IsArchive $_ })
        if ($arch.Count -eq 0) { Write-Warn 'None of the selected items are archives.'; Read-Close; return }
        $n = 0; $fail = 0
        foreach ($x in $arch) {
            $n++
            $dir = [System.IO.Path]::GetDirectoryName($x)
            $dest = if ($Mode -eq 'extract_folder') { Join-Path $dir (Get-ArchiveBase $x) } else { $dir }
            Write-Count $n $arch.Count ([System.IO.Path]::GetFileName($x))
            Write-Info "-> $dest"
            & $z7 x "$x" "-o$dest" -y -bso0 -bsp0
            if ($LASTEXITCODE -eq 0) { Write-Ok ("done  " + (Get-Arrow) + "  " + [System.IO.Path]::GetFileName($dest)) }
            else { $fail++; Write-Err ("7-Zip exit " + $LASTEXITCODE) }
            Write-Host ''
        }
        if ($fail -eq 0) { Write-Ok ("Extracted {0} archive(s)." -f $arch.Count) }
        else { Write-Warn ("Done with {0} failure(s) of {1}." -f $fail, $arch.Count) }
    }
    Write-Host ''; Read-Close
}

# =====================================================================
# Coalesce dispatch: compress verbs fire once-per-file. Unless --batch
# (worker), become a windowless collector that the leader merges into one
# visible worker window.
# =====================================================================
$CoalesceMap = @{ 'extract-here'='extract_here'; 'extract-folder'='extract_folder';
                  'zip'='zip'; '7z'='sevenz'; '7z-split'='sevenz_split' }
if ($CoalesceMap.ContainsKey($Command) -and -not $Batch) {
    Start-Coalesced -EnginePath $PSCommandPath -Command $Command -Target (Get-Target $Target)
    return
}

# =====================================================================
# Git clone (FIX: call git directly, no cmd.exe; ZIP fallback)
# =====================================================================
function Parse-GHUrl([string]$raw) {
    if (-not $raw) { return $null }
    $r = $raw.Trim().Trim('"', '<', '>', '(', ')') -replace '[\?#].*$', '' -replace '\.git/?$', ''
    if ($r -match '(?:https?://)?(?:www\.)?github\.com[:/]+([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)') { return @{ Owner = $Matches[1]; Repo = $Matches[2] } }
    if ($r -match 'git@github\.com:([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)')                          { return @{ Owner = $Matches[1]; Repo = $Matches[2] } }
    if ($r -match '^([A-Za-z0-9][\w.-]*)/([A-Za-z0-9][\w.-]*)$')                                  { return @{ Owner = $Matches[1]; Repo = $Matches[2] } }  # owner/repo shorthand
    return $null
}
function Clone-One {
    param([string]$Owner, [string]$Repo, [string]$Dest)
    $destPath = Join-Path $Dest $Repo
    if (Test-Path -LiteralPath $destPath) { Write-Warn "Skipping $Repo - already exists"; return $false }
    $git = Find-Tool 'git'
    if ($git) {
        $cloneUrl = "https://github.com/$Owner/$Repo.git"
        Write-Step "git clone $cloneUrl"
        # FIX: direct native call (the old cmd.exe string mis-parsed and caused
        #      "fatal: Too many arguments"). 2>&1 merges git's stderr for display.
        & $git clone $cloneUrl $destPath 2>&1 | ForEach-Object { Write-Info $_ }
        if ($LASTEXITCODE -eq 0 -and (Test-Path -LiteralPath $destPath)) { Write-Ok ("$Repo " + (Get-Arrow) + " $destPath"); return $true }
        Write-Warn "git clone failed (exit $LASTEXITCODE) - trying ZIP fallback..."
    } else { Write-Warn 'git not found - trying ZIP fallback...' }

    $tmpZip = Join-Path $env:TEMP "$Repo-clone.zip"
    if (Test-Path -LiteralPath $tmpZip) { Remove-Item -LiteralPath $tmpZip -Force }
    $ok = $false; $branch = $null
    foreach ($br in @('main','master')) {
        $u = "https://codeload.github.com/$Owner/$Repo/zip/refs/heads/$br"
        try { Invoke-WebRequest -Uri $u -OutFile $tmpZip -UseBasicParsing -TimeoutSec 60 -ErrorAction Stop; $ok = $true; $branch = $br; break } catch {}
    }
    if (-not $ok) { Write-Err "FAILED: $Repo (git clone and ZIP download both failed)"; return $false }
    $tmp = New-TempDir 'ghclone'
    Expand-Archive -LiteralPath $tmpZip -DestinationPath $tmp -Force
    Remove-Item -LiteralPath $tmpZip -Force
    $src = Get-ChildItem -LiteralPath $tmp -Directory | Where-Object { $_.Name -like "$Repo-*" } | Select-Object -First 1
    if (-not $src) { Write-Err "FAILED: $Repo (ZIP extract error)"; Remove-Item -LiteralPath $tmp -Recurse -Force; return $false }
    Copy-Item -LiteralPath $src.FullName -Destination $destPath -Recurse -Force
    Remove-Item -LiteralPath $tmp -Recurse -Force
    if ($git) {
        Push-Location $destPath
        & $git init -b main 2>$null | Out-Null
        & $git remote add origin "https://github.com/$Owner/$Repo" 2>$null | Out-Null
        Pop-Location
    }
    Write-Ok ("$Repo " + (Get-Arrow) + " $destPath (ZIP, branch: $branch)")
    return $true
}

# =====================================================================
# Copy-structure helpers
# =====================================================================
function Format-Size([long]$b) {
    if ($b -ge 1GB) { return "{0:N1} GB" -f ($b/1GB) }
    if ($b -ge 1MB) { return "{0:N1} MB" -f ($b/1MB) }
    if ($b -ge 1KB) { return "{0:N1} KB" -f ($b/1KB) }
    return "$b B"
}
function Build-Tree {
    param([string]$Path, [string]$Prefix = '', [string]$TreeMode = 'full', [switch]$Sizes)
    $lines = [System.Collections.Generic.List[string]]::new()
    $dirs  = Get-ChildItem -LiteralPath $Path -Directory -Force -EA SilentlyContinue | Sort-Object Name
    $files = if ($TreeMode -ne 'folders') { Get-ChildItem -LiteralPath $Path -File -Force -EA SilentlyContinue | Sort-Object Name } else { @() }
    $all = @($dirs) + @($files); $count = $all.Count
    for ($i = 0; $i -lt $count; $i++) {
        $item = $all[$i]; $isLast = ($i -eq $count - 1)
        $br = if ($isLast) { '`-- ' } else { '|-- ' }
        $ct = if ($isLast) { '    ' } else { '|   ' }
        if ($item -is [System.IO.DirectoryInfo]) {
            $lines.Add("$Prefix$br$($item.Name)/")
            foreach ($l in (Build-Tree -Path $item.FullName -Prefix ($Prefix + $ct) -TreeMode $TreeMode -Sizes:$Sizes)) { $lines.Add($l) }
        } else {
            $sz = if ($Sizes) { '  [' + (Format-Size $item.Length) + ']' } else { '' }
            $lines.Add("$Prefix$br$($item.Name)$sz")
        }
    }
    return $lines
}
function Invoke-CopyStructure {
    param([string]$Folder, [string]$Mode)   # full | folders | files | sizes | contents
    $Folder = (Resolve-Path -LiteralPath $Folder).Path.TrimEnd('\')
    Write-Banner "Copy Structure  -  $Mode"
    $root = [System.IO.Path]::GetFileName($Folder)
    $lines = [System.Collections.Generic.List[string]]::new(); $lines.Add("$root/")
    if ($Mode -eq 'files') {
        Get-ChildItem -LiteralPath $Folder -File -Recurse -Force -EA SilentlyContinue |
            ForEach-Object { $lines.Add($_.FullName.Substring($Folder.Length + 1) -replace '\\','/') }
    } elseif ($Mode -eq 'contents') {
        $bin = @('exe','dll','png','jpg','jpeg','gif','bmp','ico','webp','pdf','zip','7z','rar','gz','mp3','mp4','mov','avi','mkv','wav','flac','db','sqlite','docx','xlsx','pptx','class','pyc','bin','iso')
        foreach ($l in (Build-Tree -Path $Folder -TreeMode 'full')) { $lines.Add($l) }
        $blocks = [System.Collections.Generic.List[string]]::new()
        Get-ChildItem -LiteralPath $Folder -File -Recurse -Force -EA SilentlyContinue | ForEach-Object {
            $rel = $_.FullName.Substring($Folder.Length + 1) -replace '\\','/'
            if ($_.Length -le 100KB -and $bin -notcontains $_.Extension.TrimStart('.').ToLower()) {
                try {
                    $text = [System.IO.File]::ReadAllText($_.FullName)
                    if (-not ($text -match "\x00")) {
                        $blocks.Add(''); $blocks.Add('=' * 64); $blocks.Add("FILE: $rel"); $blocks.Add('=' * 64)
                        $blocks.Add('```' + $_.Extension.TrimStart('.')); $blocks.Add($text.TrimEnd()); $blocks.Add('```')
                    }
                } catch {}
            }
        }
        foreach ($b in $blocks) { $lines.Add($b) }
    } else {
        $tm = if ($Mode -eq 'folders') { 'folders' } else { 'full' }
        foreach ($l in (Build-Tree -Path $Folder -TreeMode $tm -Sizes:($Mode -eq 'sizes'))) { $lines.Add($l) }
    }
    $out = $lines -join "`r`n"
    Set-Clipboard -Value $out
    Write-Ok ("Copied to clipboard  -  {0} lines, {1} chars" -f $lines.Count, $out.Length)
    Write-Host ''; Write-Info 'Preview:'
    $lines | Select-Object -First 20 | ForEach-Object { Write-Info $_ }
    Start-Sleep -Milliseconds 600
}

# =====================================================================
# Remote config helper
# =====================================================================
function Get-RemoteConfig {
    $cfg = Load-Config
    if (-not $cfg -or -not $cfg.ssh_host) {
        Write-Warn 'No remote config. Copy config.example.json to config.json and fill in ssh_host etc.'
        return $null
    }
    return $cfg
}

# =====================================================================
# Unlocker - Restart Manager (finds the exact processes locking a path)
# =====================================================================
function Initialize-Unlocker {
    if ('DevTools.RM' -as [type]) { return }
    Add-Type -Language CSharp -TypeDefinition @'
using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using System.Text;
namespace DevTools {
  // Restart Manager: which apps hold a resource (catches loaded modules / sections too).
  public static class RM {
    [StructLayout(LayoutKind.Sequential)]
    struct RM_UNIQUE_PROCESS { public int dwProcessId; public System.Runtime.InteropServices.ComTypes.FILETIME ProcessStartTime; }
    [StructLayout(LayoutKind.Sequential, CharSet=CharSet.Unicode)]
    struct RM_PROCESS_INFO {
      public RM_UNIQUE_PROCESS Process;
      [MarshalAs(UnmanagedType.ByValTStr, SizeConst=256)] public string strAppName;
      [MarshalAs(UnmanagedType.ByValTStr, SizeConst=64)] public string strServiceShortName;
      public int ApplicationType; public uint AppStatus; public uint TSSessionId;
      [MarshalAs(UnmanagedType.Bool)] public bool bRestartable;
    }
    [DllImport("rstrtmgr.dll", CharSet=CharSet.Unicode)] static extern int RmStartSession(out uint h, int flags, string key);
    [DllImport("rstrtmgr.dll")] static extern int RmEndSession(uint h);
    [DllImport("rstrtmgr.dll", CharSet=CharSet.Unicode)] static extern int RmRegisterResources(uint h, uint nf, string[] files, uint na, RM_UNIQUE_PROCESS[] apps, uint ns, string[] svc);
    [DllImport("rstrtmgr.dll")] static extern int RmGetList(uint h, out uint needed, ref uint count, [In,Out] RM_PROCESS_INFO[] info, ref uint reasons);
    [DllImport("kernel32.dll", CharSet=CharSet.Unicode, SetLastError=true)] [return: MarshalAs(UnmanagedType.Bool)] static extern bool MoveFileEx(string a, string b, int flags);
    public static bool DeleteOnReboot(string path){ return MoveFileEx(path, null, 0x4); }
    public static string[] GetLockers(string[] paths){
      uint h; var res=new List<string>(); string key=Guid.NewGuid().ToString();
      if (RmStartSession(out h,0,key)!=0) return res.ToArray();
      try {
        if (RmRegisterResources(h,(uint)paths.Length,paths,0,null,0,null)!=0) return res.ToArray();
        uint needed=0, count=0, reasons=0;
        int rv=RmGetList(h, out needed, ref count, null, ref reasons);
        if (rv==234 && needed>0){
          var info=new RM_PROCESS_INFO[needed]; count=needed;
          rv=RmGetList(h, out needed, ref count, info, ref reasons);
          if (rv==0){ for(int i=0;i<count;i++){ res.Add(info[i].Process.dwProcessId+"|"+(info[i].strAppName==null?"":info[i].strAppName)+"|"+info[i].ApplicationType); } }
        }
      } finally { RmEndSession(h); }
      return res.ToArray();
    }
  }
  // Handle surgery: enumerate every handle, find the ones on the target, and
  // force-close them in the owning process (unlock WITHOUT killing the app).
  public static class Native {
    [DllImport("ntdll.dll")] static extern int NtQuerySystemInformation(int c, IntPtr i, int l, ref int r);
    [DllImport("kernel32.dll", SetLastError=true)] static extern IntPtr OpenProcess(int a, bool inh, int pid);
    [DllImport("kernel32.dll", SetLastError=true)] static extern bool DuplicateHandle(IntPtr sp, IntPtr sh, IntPtr tp, out IntPtr th, int a, bool inh, int opt);
    [DllImport("kernel32.dll", SetLastError=true)] static extern bool CloseHandle(IntPtr h);
    [DllImport("kernel32.dll")] static extern IntPtr GetCurrentProcess();
    [DllImport("kernel32.dll", CharSet=CharSet.Unicode, SetLastError=true)] static extern int GetFinalPathNameByHandle(IntPtr h, StringBuilder sb, int len, int flags);
    [DllImport("kernel32.dll")] static extern uint GetFileType(IntPtr h);
    [DllImport("advapi32.dll", SetLastError=true)] static extern bool OpenProcessToken(IntPtr p, int a, out IntPtr t);
    [DllImport("advapi32.dll", SetLastError=true, CharSet=CharSet.Unicode)] static extern bool LookupPrivilegeValue(string h, string n, out long luid);
    [DllImport("advapi32.dll", SetLastError=true)] static extern bool AdjustTokenPrivileges(IntPtr t, bool dis, ref TOKEN_PRIVILEGES np, int len, IntPtr prev, IntPtr rl);
    [StructLayout(LayoutKind.Sequential)] struct TOKEN_PRIVILEGES { public int Count; public long Luid; public int Attributes; }
    const int SystemExtendedHandleInformation = 64;
    const int DUPLICATE_CLOSE_SOURCE = 0x1, DUPLICATE_SAME_ACCESS = 0x2, PROCESS_DUP_HANDLE = 0x40;

    public static void EnableDebug() {
      IntPtr tok;
      if (!OpenProcessToken(GetCurrentProcess(), 0x28, out tok)) return; // ADJUST | QUERY
      long luid;
      if (LookupPrivilegeValue(null, "SeDebugPrivilege", out luid)) {
        var tp = new TOKEN_PRIVILEGES { Count = 1, Luid = luid, Attributes = 0x2 };
        AdjustTokenPrivileges(tok, false, ref tp, Marshal.SizeOf(tp), IntPtr.Zero, IntPtr.Zero);
      }
      CloseHandle(tok);
    }
    static string FinalPath(IntPtr h) {
      var sb = new StringBuilder(1024);
      int r = GetFinalPathNameByHandle(h, sb, 1024, 0);
      if (r <= 0 || r > 1024) return null;
      string s = sb.ToString();
      if (s.StartsWith("\\\\?\\")) s = s.Substring(4);
      return s;
    }
    // Find (and optionally force-close) handles whose path == target or is under it.
    // Returns "pid|path" for each match. pidFilter (optional) limits the scan.
    public static List<string> Scan(string target, bool close, int[] pidFilter) {
      var res = new List<string>();
      if (string.IsNullOrEmpty(target)) return res;
      string tl = target.ToLowerInvariant().TrimEnd('\\');
      string tls = tl + "\\";
      HashSet<int> only = null;
      if (pidFilter != null && pidFilter.Length > 0) { only = new HashSet<int>(pidFilter); }
      int len = 0x40000, ret = 0, st;
      IntPtr buf = Marshal.AllocHGlobal(len);
      while ((st = NtQuerySystemInformation(SystemExtendedHandleInformation, buf, len, ref ret)) == unchecked((int)0xC0000004L)) {
        Marshal.FreeHGlobal(buf); len = (ret > len) ? ret + 0x40000 : len * 2; buf = Marshal.AllocHGlobal(len);
      }
      if (st != 0) { Marshal.FreeHGlobal(buf); return res; }
      IntPtr me = GetCurrentProcess();
      int mypid = System.Diagnostics.Process.GetCurrentProcess().Id;
      long count = (long)Marshal.ReadIntPtr(buf);
      bool x64 = IntPtr.Size == 8;
      long baseOff = (long)buf + IntPtr.Size * 2;              // skip NumberOfHandles + Reserved
      int esz       = x64 ? 40 : 28;                            // sizeof(SYSTEM_HANDLE_TABLE_ENTRY_INFO_EX)
      int offPid    = x64 ? 8  : 4;
      int offHandle = x64 ? 16 : 8;
      var procs = new Dictionary<int, IntPtr>();
      try {
        for (long i = 0; i < count; i++) {
          long p = baseOff + i * esz;
          int pid = (int)Marshal.ReadIntPtr((IntPtr)(p + offPid));
          if (pid <= 4 || pid == mypid) continue;
          if (only != null && !only.Contains(pid)) continue;
          IntPtr hval = Marshal.ReadIntPtr((IntPtr)(p + offHandle));
          IntPtr ph;
          if (!procs.TryGetValue(pid, out ph)) { ph = OpenProcess(PROCESS_DUP_HANDLE, false, pid); procs[pid] = ph; }
          if (ph == IntPtr.Zero) continue;
          IntPtr dup;
          if (!DuplicateHandle(ph, hval, me, out dup, 0, false, DUPLICATE_SAME_ACCESS)) continue;
          // GetFileType is non-blocking; FinalPath would HANG on pipe/console handles
          // (also "File" objects), so resolve names ONLY for real disk files.
          string name = null;
          if (GetFileType(dup) == 1) { name = FinalPath(dup); }  // 1 = FILE_TYPE_DISK
          CloseHandle(dup);
          if (name == null) continue;
          string nl = name.ToLowerInvariant();
          if (nl == tl || nl.StartsWith(tls)) {
            res.Add(pid + "|" + name);
            if (close) { IntPtr tmp; if (DuplicateHandle(ph, hval, me, out tmp, 0, false, DUPLICATE_CLOSE_SOURCE)) CloseHandle(tmp); }
          }
        }
      } finally {
        foreach (var kv in procs) { if (kv.Value != IntPtr.Zero) CloseHandle(kv.Value); }
        Marshal.FreeHGlobal(buf);
      }
      return res;
    }
  }
}
'@
}
function Get-FileLockers([string[]]$Paths) {
    Initialize-Unlocker
    $out = @()
    foreach ($r in [DevTools.RM]::GetLockers($Paths)) {
        $f = $r -split '\|', 3
        $out += [pscustomobject]@{ Pid = [int]$f[0]; Name = $f[1]; Type = [int]$f[2] }
    }
    return $out
}
function Get-HandleLockers([string]$Target, [int[]]$PidFilter, [switch]$Close) {
    Initialize-Unlocker
    $out = @()
    foreach ($r in [DevTools.Native]::Scan($Target, [bool]$Close, $PidFilter)) {
        $f = $r -split '\|', 2
        $out += [pscustomobject]@{ Pid = [int]$f[0]; Path = $f[1] }
    }
    return $out
}
function Test-PathUnlocked([string]$Path) {
    if (Test-Path -LiteralPath $Path -PathType Container) {
        # folder: unlocked if nothing reports a lock on it
        return ((@(Get-FileLockers @($Path)).Count -eq 0) -and (@(Get-HandleLockers $Path $null).Count -eq 0))
    }
    try { $fs = [System.IO.File]::Open($Path, 'Open', 'ReadWrite', 'None'); $fs.Close(); return $true } catch { return $false }
}

# =====================================================================
# Dispatch
# =====================================================================
switch ($Command) {

  # ---- Compress (worker side; collector handled above) ----
  { $CoalesceMap.ContainsKey($_) } { Invoke-CompressBatch -Mode $CoalesceMap[$_] -ListFile $Batch; break }
  'open' {
      $z = Find-7ZipFM; $t = Get-Target $Target
      if ($z) { Start-Process $z -ArgumentList ('"' + $t + '"') } else { Write-Err '7-Zip (7zFM.exe) not found.' }
      break
  }

  # ---- Copy structure ----
  'copy-tree'     { Invoke-CopyStructure (Get-Target $Target) 'full';     break }
  'copy-folders'  { Invoke-CopyStructure (Get-Target $Target) 'folders';  break }
  'copy-files'    { Invoke-CopyStructure (Get-Target $Target) 'files';    break }
  'copy-sizes'    { Invoke-CopyStructure (Get-Target $Target) 'sizes';    break }
  'copy-contents' { Invoke-CopyStructure (Get-Target $Target) 'contents'; break }

  # ---- Git ----
  'clone' {
      Write-Banner 'Git Clone (multi)'
      $dest = Get-Target $Target
      $url  = Get-Flag 'url'
      $repos = @()
      # collect from --url, else clipboard (one per line / comma). NOTE: a foreach
      # STATEMENT (not ForEach-Object) so += actually accumulates in this scope.
      $tokens = @()
      if ($url) { $tokens = $url -split '[\s,]+' }
      else {
          $clip = ''
          try { $clip = Get-Clipboard -Raw -ErrorAction Stop } catch {}
          if (-not $clip) { try { $clip = (Get-Clipboard) -join "`n" } catch {} }
          if ($clip) { $tokens = $clip -split "[`r`n,]+" }
      }
      foreach ($tok in $tokens) { $p = Parse-GHUrl $tok; if ($p) { $repos += $p } }

      if ($repos.Count -eq 0) {
          Write-Warn 'No GitHub URLs found on the clipboard. Type/paste URLs (one per line); blank line to start.'
          while ($true) { $l = Read-Host '  URL'; if (-not $l) { break }; $p = Parse-GHUrl $l; if ($p) { $repos += $p } else { Write-Warn "Not a GitHub URL: $l" } }
      }
      # de-duplicate by owner/repo, preserving order
      $seen = @{}; $uniq = @()
      foreach ($r in $repos) { $k = ($r.Owner + '/' + $r.Repo).ToLower(); if (-not $seen.ContainsKey($k)) { $seen[$k] = $true; $uniq += $r } }
      $repos = $uniq
      if ($repos.Count -eq 0) { Write-Err 'No valid GitHub repo URLs.'; Read-Close; break }

      Write-Info ("Target : $dest"); Write-Info ("Repos  : " + $repos.Count + "  (" + (($repos | ForEach-Object { $_.Owner + '/' + $_.Repo }) -join ', ') + ")"); Write-Host ''
      $n = 0; $done = 0
      foreach ($r in $repos) {
          $n++; Write-Count $n $repos.Count ("{0}/{1}" -f $r.Owner, $r.Repo)
          if (Clone-One -Owner $r.Owner -Repo $r.Repo -Dest $dest) { $done++ }
          Write-Host ''
      }
      Write-Ok ("Cloned {0} of {1} repo(s) into {2}" -f $done, $repos.Count, $dest); Read-Close; break
  }
  'open-repo' {
      $folder = Get-Target $Target; $url = $null
      $cur = $folder
      for ($i = 0; $i -lt 6; $i++) {
          $gc = Join-Path $cur '.git\config'
          if (Test-Path -LiteralPath $gc) {
              $c = Get-Content -LiteralPath $gc -Raw
              if ($c -match 'url\s*=\s*(.+)') { $url = ($Matches[1].Trim() -replace '^git@github\.com:','https://github.com/') -replace '\.git$',''; break }
          }
          $parent = [System.IO.Path]::GetDirectoryName($cur); if (-not $parent -or $parent -eq $cur) { break }; $cur = $parent
      }
      if (-not $url) { $git = Find-Tool 'git'; if ($git) { Push-Location $folder; $url = (& $git remote get-url origin 2>$null) -replace '\.git$',''; Pop-Location } }
      if (-not $url) { Write-Err "No git remote origin found in $folder"; Start-Sleep 3; break }
      Write-Step "Opening: $url"; Start-Process $url; break
  }

  # ---- Download ----
  'video' {
      $dir = Get-Target $Target; $yt = Assert-Tool 'yt-dlp'
      $u = (Get-Clipboard -Raw).Trim()
      if (-not $u -or $u -notmatch '^https?://') { Write-Err 'Clipboard is empty or not a URL.'; Read-Close; break }
      Write-Banner 'Download video / audio'; Write-Info "URL: $u"; Write-Info "To : $dir"; Write-Host ''
      Write-Host '  1 Best video (mp4)'; Write-Host '  2 Best audio (mp3)'; Write-Host '  3 Best audio (m4a)'
      Write-Host '  4 Playlist (video)'; Write-Host '  5 Playlist (audio)'; Write-Host '  6 Custom format'
      $c = Read-Host '  Choose [1-6]'
      $a = @('--no-playlist','-o', "$dir\%(title)s.%(ext)s")
      switch ($c) {
          '2' { $a += @('-x','--audio-format','mp3','--audio-quality','0') }
          '3' { $a += @('-x','--audio-format','m4a','--audio-quality','0') }
          '4' { $a = @('--yes-playlist','-o', "$dir\%(playlist)s\%(title)s.%(ext)s",'-f','bestvideo[ext=mp4]+bestaudio[ext=m4a]/best') }
          '5' { $a = @('--yes-playlist','-o', "$dir\%(playlist)s\%(title)s.%(ext)s",'-x','--audio-format','mp3') }
          '6' { $fmt = Read-Host '  Format string'; $a += @('-f',$fmt) }
          default { $a += @('-f','bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best') }
      }
      $a += $u; Write-Host ''; & $yt @a
      if ($LASTEXITCODE -eq 0) { Write-Ok 'Download complete.' } else { Write-Err ("yt-dlp exit " + $LASTEXITCODE) }
      Read-Close; break
  }
  'image' {
      $dir = Get-Target $Target; $u = (Get-Clipboard -Raw).Trim()
      if (-not $u -or $u -notmatch '^https?://') { Write-Err 'Clipboard is empty or not a URL.'; Read-Close; break }
      Write-Banner 'Download image'; Write-Info "URL: $u"; Write-Info "To : $dir"
      $uri = [System.Uri]$u; $fn = [System.IO.Path]::GetFileName($uri.LocalPath)
      if (-not $fn -or $fn -notmatch '\.\w{2,5}$') { $fn = "image_$(Get-Date -Format 'yyyyMMdd_HHmmss')" }
      $outPath = Join-Path $dir $fn
      try {
          $resp = Invoke-WebRequest -Uri $u -OutFile $outPath -PassThru -UseBasicParsing -TimeoutSec 60
          if ($outPath -notmatch '\.\w{2,5}$' -and $resp.Headers['Content-Type']) {
              $ext = switch -Regex ($resp.Headers['Content-Type']) { 'jpeg|jpg' {'.jpg'} 'png' {'.png'} 'gif' {'.gif'} 'webp' {'.webp'} 'svg' {'.svg'} default {''} }
              if ($ext) { Rename-Item -LiteralPath $outPath ($outPath + $ext); $outPath += $ext }
          }
          Write-Ok ("Saved: $outPath ({0:N1} KB)" -f ((Get-Item -LiteralPath $outPath).Length / 1KB))
      } catch { Write-Err "Download failed: $($_.Exception.Message)" }
      Read-Close; break
  }

  # ---- Dev ----
  'npm' {
      $folder = Get-Target $Target; Assert-Tool 'npm' | Out-Null
      Write-Banner "npm tools  -  $folder"
      $scripts = @{}; $pkg = Join-Path $folder 'package.json'
      if (Test-Path -LiteralPath $pkg) { try { (Get-Content -LiteralPath $pkg -Raw | ConvertFrom-Json).scripts.PSObject.Properties | ForEach-Object { $scripts[$_.Name] = $_.Value } } catch {} }
      Write-Host '  1 install   2 ci   3 run build   4 run dev   5 run start   6 update   7 audit fix   8 outdated'
      $map = @{}; $i = 10
      if ($scripts.Count) { Write-Info 'package.json scripts:'; foreach ($s in ($scripts.Keys | Sort-Object)) { Write-Host "  $i  npm run $s" -ForegroundColor DarkYellow; $map["$i"] = $s; $i++ } }
      $c = Read-Host '  Choose'; Push-Location $folder
      switch ($c) { '1'{npm install} '2'{npm ci} '3'{npm run build} '4'{npm run dev} '5'{npm run start} '6'{npm update} '7'{npm audit fix} '8'{npm outdated} default { if ($map.ContainsKey($c)) { npm run $map[$c] } else { Write-Warn 'Invalid choice.' } } }
      Pop-Location; Read-Close; break
  }
  'docker' {
      $folder = Get-Target $Target; Assert-Tool 'docker' | Out-Null
      $compose = (Test-Path (Join-Path $folder 'docker-compose.yml')) -or (Test-Path (Join-Path $folder 'compose.yaml'))
      $clip = (Get-Clipboard -Raw).Trim(); $isImg = $clip -match '^[\w./-]+(:[\w.-]+)?$' -and $clip.Length -lt 200
      Write-Banner "Docker tools  -  $folder"
      Write-Host ("  1 pull ({0})   2 run   3 build -t <tag>   4 images   5 ps -a" -f $(if ($isImg) { $clip } else { '<manual>' }))
      if ($compose) { Write-Host '  6 compose up -d   7 compose down   8 compose logs -f   9 compose build' }
      $c = Read-Host '  Choose'; Push-Location $folder
      switch ($c) {
          '1' { $img = if ($isImg) { $clip } else { Read-Host '  Image' }; docker pull $img }
          '2' { $img = if ($isImg) { $clip } else { Read-Host '  Image' }; docker run -it --rm $img }
          '3' { $tag = Read-Host '  Tag'; docker build . -t $tag }
          '4' { docker images } '5' { docker ps -a }
          '6' { if ($compose) { docker compose up -d } } '7' { if ($compose) { docker compose down } }
          '8' { if ($compose) { docker compose logs -f } } '9' { if ($compose) { docker compose build } }
          default { Write-Warn 'Invalid choice.' }
      }
      Pop-Location; Read-Close; break
  }

  # ---- Remote ----
  'ssh' {
      $folder = Get-Target $Target; $cfg = Get-RemoteConfig; if (-not $cfg) { Read-Close; break }
      $ssh = Assert-Tool 'ssh'
      $port = if ($cfg.ssh_port) { $cfg.ssh_port } else { 22 }
      $rel = $folder -replace '^[A-Za-z]:\\','' -replace '\\','/'
      $remote = if ($cfg.remote_root) { "$($cfg.remote_root)/$rel" } else { '' }
      Write-Banner 'SSH'; Write-Info "Host: $($cfg.ssh_host)"; Write-Info "Remote: $remote"
      $a = @('-p', "$port")
      if ($cfg.ssh_key -and (Test-Path -LiteralPath $cfg.ssh_key)) { $a += @('-i', $cfg.ssh_key) }
      if ($remote) { $a += @('-t', $cfg.ssh_host, "cd '$remote' && exec `$SHELL") } else { $a += @($cfg.ssh_host) }
      Start-Process $ssh -ArgumentList $a -WindowStyle Normal; break
  }
  'upload' {
      $folder = Get-Target $Target; $cfg = Get-RemoteConfig; if (-not $cfg) { Read-Close; break }
      $port = if ($cfg.ssh_port) { $cfg.ssh_port } else { 22 }
      $rel = $folder -replace '^[A-Za-z]:\\','' -replace '\\','/'
      $remote = if ($cfg.remote_root) { "$($cfg.remote_root)/$rel" } else { "~/$rel" }
      Write-Banner 'Upload'; Write-Info "$folder -> $($cfg.ssh_host):$remote"
      $scp = Find-Tool 'scp'; if (-not $scp) { Write-Err 'scp not found (install OpenSSH client).'; Read-Close; break }
      $a = @('-r','-P', "$port"); if ($cfg.ssh_key -and (Test-Path -LiteralPath $cfg.ssh_key)) { $a += @('-i', $cfg.ssh_key) }
      $a += @($folder, "$($cfg.ssh_host):$remote")
      & $scp @a
      if ($LASTEXITCODE -eq 0) { Write-Ok 'Upload completed.' } else { Write-Err ("Upload exit " + $LASTEXITCODE) }
      Read-Close; break
  }
  'deploy' {
      $folder = Get-Target $Target; $cfg = Get-RemoteConfig; if (-not $cfg) { Read-Close; break }
      $port = if ($cfg.ssh_port) { $cfg.ssh_port } else { 22 }
      $name = [System.IO.Path]::GetFileName($folder)
      $remote = if ($cfg.remote_root) { "$($cfg.remote_root)/$name" } else { "~/$name" }
      Write-Banner 'Deploy'; Write-Info "$folder -> $($cfg.ssh_host):$remote"
      $scp = Find-Tool 'scp'; if (-not $scp) { Write-Err 'scp not found (install OpenSSH client).'; Read-Close; break }
      $a = @('-r','-P', "$port"); if ($cfg.ssh_key -and (Test-Path -LiteralPath $cfg.ssh_key)) { $a += @('-i', $cfg.ssh_key) }
      $a += @($folder, "$($cfg.ssh_host):$remote")
      & $scp @a
      if ($LASTEXITCODE -eq 0) { Write-Ok 'Deploy completed.' } else { Write-Err ("Deploy exit " + $LASTEXITCODE) }
      Read-Close; break
  }

  # ---- Other ----
  'virustotal' {
      $t = Get-Target $Target; $cfg = Load-Config
      Write-Banner 'VirusTotal scan'; Write-Info "Target: $t"
      $key = if ($cfg -and $cfg.virustotal_api_key -and $cfg.virustotal_api_key -ne 'YOUR_KEY_HERE') { $cfg.virustotal_api_key } else { '' }
      if (-not $key) { Write-Warn 'No API key in config.json (virustotal_api_key). Opening the website for manual upload.'; Start-Process 'https://www.virustotal.com/gui/home/upload'; Read-Close; break }
      $upload = $t; $tmp = ''
      if (Test-Path -LiteralPath $t -PathType Container) { $tmp = Join-Path $env:TEMP ("vt-" + ([System.IO.Path]::GetFileName($t)) + "-" + [guid]::NewGuid().ToString('N') + '.zip'); Compress-Archive -Path $t -DestinationPath $tmp -Force; $upload = $tmp }
      try {
          $size = (Get-Item -LiteralPath $upload).Length
          if ($size -gt 681574400) { Write-Err 'File exceeds VirusTotal 650 MB limit.'; break }
          $http = [System.Net.Http.HttpClient]::new(); $http.DefaultRequestHeaders.Add('x-apikey', $key)
          $fs = [System.IO.File]::OpenRead($upload); $fc = [System.Net.Http.StreamContent]::new($fs)
          $fc.Headers.ContentDisposition = [System.Net.Http.Headers.ContentDispositionHeaderValue]::new('form-data')
          $fc.Headers.ContentDisposition.Name = '"file"'; $fc.Headers.ContentDisposition.FileName = '"' + ([System.IO.Path]::GetFileName($upload)) + '"'
          $mp = [System.Net.Http.MultipartFormDataContent]::new(); $mp.Add($fc)
          $endpoint = if ($size -le 33554432) { 'https://www.virustotal.com/api/v3/files' } else { (Invoke-RestMethod -Uri 'https://www.virustotal.com/api/v3/files/upload_url' -Headers @{ 'x-apikey'=$key } -TimeoutSec 30).data }
          $resp = $http.PostAsync($endpoint, $mp).Result; $body = $resp.Content.ReadAsStringAsync().Result
          $fs.Dispose(); $http.Dispose()
          if (-not $resp.IsSuccessStatusCode) { throw "HTTP $([int]$resp.StatusCode): $body" }
          $id = ($body | ConvertFrom-Json).data.id
          Write-Ok "Uploaded. Analysis: $id"; Start-Process "https://www.virustotal.com/gui/file-analysis/$id"
      } catch { Write-Err "Upload failed: $_"; Start-Process 'https://www.virustotal.com/gui/home/upload' }
      finally { if ($tmp -and (Test-Path -LiteralPath $tmp)) { Remove-Item -LiteralPath $tmp -Force -EA SilentlyContinue } }
      Read-Close; break
  }
  'shorten' {
      $u = (Get-Clipboard -Raw).Trim()
      if (-not $u -or $u -notmatch '^https?://') { Write-Err 'Clipboard is empty or not a URL.'; Start-Sleep 2; break }
      Write-Banner 'Shorten URL'; Write-Info "Original: $u"
      try {
          $short = (Invoke-WebRequest -Uri ('https://tinyurl.com/api-create.php?url=' + [System.Uri]::EscapeDataString($u)) -UseBasicParsing -TimeoutSec 10).Content.Trim()
          if ($short -notmatch '^https?://') { throw "Unexpected response: $short" }
          Set-Clipboard -Value $short; Write-Ok "Short: $short (copied)"
      } catch { Write-Err "Failed: $($_.Exception.Message)" }
      Start-Sleep 2; break
  }

  # ---- Unlocker (prodigious) ----
  'unlock' {
      $t = Get-Target $Target
      # Handle-level surgery (close handles in other processes) needs admin + SeDebug.
      $admin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
      if (-not $admin) {
          Write-Banner 'Unlock File'; Write-Info "Target: $t"
          Write-Warn 'Elevating - forcing locks open needs administrator...'
          $self = (Get-Process -Id $PID).Path
          try { Start-Process $self -Verb RunAs -ArgumentList ('-NoProfile -ExecutionPolicy Bypass -File "' + $PSCommandPath + '" unlock --target "' + $t + '"') }
          catch { Write-Err 'Elevation cancelled.'; Read-Close }
          break
      }
      Initialize-Unlocker
      [DevTools.Native]::EnableDebug()
      Write-Banner 'Unlock File  (prodigious)'
      Write-Info "Target: $t"
      $isDir = Test-Path -LiteralPath $t -PathType Container
      $paths = @($t); if ($isDir) { $paths += @(Get-ChildItem -LiteralPath $t -File -Recurse -Force -EA SilentlyContinue | Select-Object -First 2000 -ExpandProperty FullName) }
      $crit = @('System', 'Registry', 'smss', 'csrss', 'wininit', 'winlogon', 'services', 'lsass', 'svchost', 'dwm', 'MemCompression')

      Write-Step 'Scanning (Restart Manager + system handle table)...'
      $rm = @(Get-FileLockers $paths)
      $rmPids = @($rm | ForEach-Object { $_.Pid })
      $handles = @(Get-HandleLockers $t $rmPids)
      $lockerNames = @{}
      foreach ($r in $rm) { $lockerNames[$r.Pid] = $r.Name }
      foreach ($h in $handles) { if (-not $lockerNames.ContainsKey($h.Pid)) { $pp = Get-Process -Id $h.Pid -EA SilentlyContinue; $lockerNames[$h.Pid] = if ($pp) { $pp.ProcessName } else { 'pid ' + $h.Pid } } }

      Write-Host ''
      if ($lockerNames.Count -eq 0) {
          Write-Ok 'Nothing currently holds an open lock.'
          Write-Info 'If it still will not delete it is attributes/permissions - use option 3.'
      } else {
          Write-Warn ("Locked by {0} process(es):" -f $lockerNames.Count)
          foreach ($procId in $lockerNames.Keys) {
              $nm = $lockerNames[$procId]
              $tag = if ($crit -contains $nm -or $procId -le 4) { '   (system - protected)' } else { '' }
              Write-Host ("       " + (Get-Arrow) + " " + $nm + "   pid " + $procId + $tag) -ForegroundColor Yellow
          }
          Write-Info ("Direct file handles found: " + $handles.Count)
      }
      Write-Host ''
      Write-Host '   1  Unlock           close handles in place; escalate to kill only if needed' -ForegroundColor Green
      Write-Host '   2  Unlock + DELETE  whatever it takes, then remove (reboot-delete fallback)' -ForegroundColor Yellow
      Write-Host '   3  Take ownership + clear read-only / system / hidden'
      Write-Host '   4  Reveal in Explorer'
      Write-Host '   0  Cancel'
      $choice = Read-Host '   Choose'

      function Invoke-Prodigious([bool]$Delete) {
          # 1) force-close the matching handles in place (unlock without killing the app)
          $c1 = @(Get-HandleLockers $t $rmPids -Close).Count
          if ($c1 -gt 0) { Write-Ok ("force-closed $c1 file handle(s)") }
          if (-not (Test-PathUnlocked $t)) {
              # 2) broad sweep across every process (catch lockers RM did not report)
              $c2 = @(Get-HandleLockers $t $null -Close).Count
              if ($c2 -gt 0) { Write-Ok ("force-closed $c2 more handle(s) (deep scan)") }
          }
          if (-not (Test-PathUnlocked $t)) {
              # 3) still held (loaded module / mapped section) -> terminate non-critical lockers
              foreach ($procId in $lockerNames.Keys) {
                  $nm = $lockerNames[$procId]
                  if ($crit -contains $nm -or $procId -le 4) { Write-Warn ("kept system process $nm"); continue }
                  if (Get-Process -Id $procId -EA SilentlyContinue) {
                      Stop-Process -Id $procId -Force -EA SilentlyContinue
                      if ($nm -ieq 'explorer') { Start-Process explorer.exe }
                      Write-Ok ("terminated $nm  pid $procId")
                  }
              }
          }
          # fix access-denied: take ownership + clear attributes
          $own = @('/f', $t); if ($isDir) { $own += @('/r', '/d', 'y') }; & takeown @own 2>&1 | Out-Null
          $me = "$env:USERDOMAIN\$env:USERNAME"; $ic = @("$t", '/grant', "${me}:F"); if ($isDir) { $ic += @('/t', '/c', '/q') }; & icacls @ic 2>&1 | Out-Null
          $at = @('-r', '-s', '-h', "$t"); if ($isDir) { $at += @('/s', '/d') }; & attrib @at 2>&1 | Out-Null

          if (Test-PathUnlocked $t) { Write-Ok 'File is now UNLOCKED.' } else { Write-Warn 'A kernel/critical holder remains.' }

          if ($Delete) {
              try { Remove-Item -LiteralPath $t -Recurse -Force -ErrorAction Stop; Write-Ok "Deleted: $t" }
              catch {
                  Write-Warn ('Delete still blocked: ' + $_.Exception.Message)
                  if ([DevTools.RM]::DeleteOnReboot($t)) { Write-Ok 'Scheduled for deletion on the next reboot.' } else { Write-Err 'Could not schedule reboot-delete.' }
              }
          }
      }

      switch ($choice) {
          '1' { Invoke-Prodigious $false }
          '2' { Invoke-Prodigious $true }
          '3' {
              $own = @('/f', $t); if ($isDir) { $own += @('/r', '/d', 'y') }; & takeown @own 2>&1 | Out-Null
              $me = "$env:USERDOMAIN\$env:USERNAME"; $ic = @("$t", '/grant', "${me}:F"); if ($isDir) { $ic += @('/t', '/c', '/q') }; & icacls @ic 2>&1 | Out-Null
              $at = @('-r', '-s', '-h', "$t"); if ($isDir) { $at += @('/s', '/d') }; & attrib @at 2>&1 | Out-Null
              Write-Ok 'Ownership taken + attributes cleared.'
          }
          '4' { Start-Process explorer.exe ('/select,"' + $t + '"') }
          default { }
      }
      Read-Close; break
  }

  # ---- Meta ----
  'doctor' {
      Write-Banner 'devtools toolchain'
      foreach ($t in '7z','git','yt-dlp','npm','docker','ssh','scp') {
          $p = Find-Tool $t
          if ($p) { Write-Ok ("{0,-8} {1}" -f $t, $p) } else { Write-Warn ("{0,-8} not found" -f $t) }
      }
      break
  }
  { $_ -in 'menu','install','uninstall' } {
      $sub = if ($_ -eq 'menu') { if ($Rest.Count -ge 1) { $Rest[0] } else { 'help' } } else { $_ }
      $map = @{ install = 'install.ps1'; uninstall = 'uninstall.ps1' }
      if ($map.ContainsKey($sub)) { & (Join-Path $PSScriptRoot ('menu\' + $map[$sub])) }
      else { Write-Info 'Usage: devtools.ps1 install | uninstall' }
      break
  }
  default {
      Write-Banner 'devtools-space engine'
      Write-Host '  Commands:' -ForegroundColor Cyan
      Write-Host '    extract-here  extract-folder  zip  7z  7z-split  open'
      Write-Host '    copy-tree  copy-folders  copy-files  copy-sizes  copy-contents'
      Write-Host '    clone [--url U]  open-repo'
      Write-Host '    video  image  npm  docker'
      Write-Host '    ssh  upload  deploy  virustotal  shorten  unlock'
      Write-Host '    doctor  menu install|uninstall  help'
      Write-Host ''
      Write-Info 'Flags:  --target <path>   --url <github-url>'
  }
}
