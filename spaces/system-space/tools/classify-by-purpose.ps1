<#
  classify-by-purpose.ps1 — file a dump into purpose buckets, copy-only, emit a manifest.
  Source-safe (copies, leaves original), -LiteralPath throughout, excludes regenerable deps.

  Usage:
    classify-by-purpose.ps1 -Source <dir> -Dest <dir> [-Apply]
  Edit $rules (regex -> bucket) and $userOwned / $junk for your domain.
#>
[CmdletBinding()]
param(
  [Parameter(Mandatory)][string]$Source,
  [Parameter(Mandatory)][string]$Dest,
  [switch]$Apply
)
Set-StrictMode -Version Latest
$XD   = @('node_modules','.git','vendor','dist','build','.next','.nuxt','target','.output','.cache')
# regex (matched against file/folder Name, case-insensitive) -> purpose bucket. First match wins.
$rules = [ordered]@{
  'dork|osint|recon|sublist3r|nmap|scan'        = 'osint-security'
  'chatgpt|gpt|llm|openai|claude|librechat'     = 'ai-llm'
  'scrap|crawl|spider|downloader|yt-dlp|coub'   = 'scraping-downloaders'
  'webrtc|chat|messenger|telegram|video.?call'  = 'chat-messaging'
  'react|vue|nuxt|next|svelte|landing|ecommerce'= 'web-frontend'
  'laravel|django|express|fastapi|api|backend'  = 'backend'
  'electron|tauri|desktop'                      = 'desktop-apps'
  'flutter|android|ios|capacitor|mobile'        = 'mobile'
  'ahk|autohotkey|automation|macro'             = 'automation'
}
$userOwned = @('@me','@mine')          # route operator's own code out of inspiration
$junk      = @('__pycache__','desktop.ini','Thumbs.db','.DS_Store')

function Bucket($name){ foreach($k in $rules.Keys){ if($name -match $k){ return $rules[$k] } }; return 'misc' }

$manifest = Join-Path $Dest '_manifest.tsv'
if(-not(Test-Path -LiteralPath $Dest)){ if($Apply){New-Item -ItemType Directory -Force $Dest|Out-Null} }
$rows = @("item`tbucket`tsource")
Get-ChildItem -LiteralPath $Source -Force -ErrorAction SilentlyContinue | ForEach-Object {
  $n = $_.Name
  if($junk -contains $n){ return }
  $b = if($userOwned | Where-Object { $n -like $_ }){ '_review-yours' } else { Bucket $n }
  $target = Join-Path (Join-Path $Dest $b) $n
  $rows += "$n`t$b`t$($_.FullName)"
  if($Apply){
    $bd = Join-Path $Dest $b; if(-not(Test-Path -LiteralPath $bd)){New-Item -ItemType Directory -Force $bd|Out-Null}
    if(-not(Test-Path -LiteralPath $target)){
      if($_.PSIsContainer){ & robocopy $_.FullName $target /E /R:0 /W:0 /MT:8 /NFL /NDL /NP /NJH /NJS /XD @XD | Out-Null }
      else { Copy-Item -LiteralPath $_.FullName -Destination $target -Force }
    }
    Write-Host "  [$b] $n"
  } else { Write-Host "  [DRY] [$b] $n" }
}
if($Apply){ $rows | Out-File $manifest -Encoding utf8; Write-Host "`n  manifest -> $manifest" }
else { Write-Host "`n  (dry-run; add -Apply to copy + write manifest)" }
