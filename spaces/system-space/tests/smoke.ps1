<#  smoke.ps1 — verify the System engine loads and the safety helpers behave.  #>
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot -Parent
$fail = 0
. (Join-Path $root 'bin/System-Common.ps1')   # load helpers into script scope
function Check($name,[scriptblock]$test){ try{ if(& $test){ Write-Host "  ok   $name" } else { Write-Host "  FAIL $name" -ForegroundColor Red; $script:fail++ } } catch { Write-Host "  FAIL $name :: $($_.Exception.Message)" -ForegroundColor Red; $script:fail++ } }

Check 'engine exists'        { Test-Path (Join-Path $root 'bin/system.ps1') }
Check 'helpers exist'        { Test-Path (Join-Path $root 'bin/System-Common.ps1') }
Check 'helpers dot-source'   { . (Join-Path $root 'bin/System-Common.ps1'); $true }
Check 'context present'      { Test-Path (Join-Path $root '.navig/context.md') }
Check 'manifest valid json'  { Get-Content (Join-Path $root '.navig/space.manifest.json') -Raw | ConvertFrom-Json | Out-Null; $true }

# functional: same-volume detection + inventory on a temp tree
$tmp = Join-Path $env:TEMP ("sys_smoke_" + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Force $tmp | Out-Null
'x' | Out-File (Join-Path $tmp 'a.txt'); New-Item -ItemType File (Join-Path $tmp 'empty.bin') | Out-Null
Check 'inventory counts'     { (Get-Inventory $tmp).Files -ge 2 }
Check 'zero-byte detected'   { (Get-Inventory $tmp).ZeroByte -ge 1 }
Check 'same-volume true'     { Test-SameVolume $tmp (Join-Path $tmp 'x') }
Remove-Item -LiteralPath $tmp -Recurse -Force -ErrorAction SilentlyContinue

if($fail){ Write-Host "`n$fail check(s) failed" -ForegroundColor Red; exit 1 } else { Write-Host "`nall checks passed" -ForegroundColor Green }
