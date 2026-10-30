# joestale 개인 설치: 이 스킬 폴더를 ~/.claude/skills/joestale 로 복사한다 (P15-5).
# 사용:  powershell -NoProfile -File skills/joestale/scripts/install.ps1 -Check
#        powershell -NoProfile -File skills/joestale/scripts/install.ps1 -Apply
#        powershell -NoProfile -File skills/joestale/scripts/install.ps1 -Remove
# 규칙: 기존 설치가 있고 VERSION이 다르면 덮어쓰지 않고 blocked. 먼저 -Remove 후 -Apply.
#       정션/심링크 설치는 하지 않는다(새 세션 로드 확인은 복사본 기준).
param([switch]$Check, [switch]$Apply, [switch]$Remove, [string]$ClaudeHome)

$ErrorActionPreference = 'Stop'
$src = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$home_ = if ($ClaudeHome) { $ClaudeHome } else { Join-Path $HOME '.claude' }
$dst = Join-Path $home_ 'skills\joestale'
$srcVer = (Get-Content (Join-Path $src 'VERSION') -Raw).Trim()
$dstVer = if (Test-Path (Join-Path $dst 'VERSION')) { (Get-Content (Join-Path $dst 'VERSION') -Raw).Trim() } else { $null }
$r = [ordered]@{ action = ''; status = ''; source = $src; sourceVersion = $srcVer; target = $dst; installedVersion = $dstVer; changed = @(); blockers = @() }

function Out-Result { $r | ConvertTo-Json -Compress | Write-Output }

if ($Check) {
  $r.action = 'check'
  if (-not (Test-Path $dst)) { $r.status = 'ready' }
  elseif ($dstVer -eq $srcVer) { $r.status = 'current' }
  else { $r.status = 'blocked'; $r.blockers += "installed $dstVer differs from source $srcVer; run -Remove first" }
  Out-Result; exit 0
}
if ($Remove) {
  $r.action = 'remove'
  if (-not (Test-Path $dst)) { $r.status = 'absent'; Out-Result; exit 0 }
  if (-not (Test-Path (Join-Path $dst 'SKILL.md')) -or -not (Test-Path (Join-Path $dst 'VERSION'))) {
    $r.status = 'blocked'; $r.blockers += 'target is not a joestale install (no SKILL.md/VERSION); not removed'; Out-Result; exit 2
  }
  Remove-Item -Recurse -Force $dst; $r.status = 'removed'; $r.changed += $dst; Out-Result; exit 0
}
if ($Apply) {
  $r.action = 'apply'
  if (Test-Path $dst) {
    if ($dstVer -eq $srcVer) { $r.status = 'current'; Out-Result; exit 0 }
    $r.status = 'blocked'; $r.blockers += "existing install $dstVer preserved; run -Remove first"; Out-Result; exit 2
  }
  New-Item -ItemType Directory -Force (Split-Path $dst) | Out-Null
  Copy-Item -LiteralPath $src -Destination $dst -Recurse
  Get-ChildItem $dst -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force
  $r.status = 'current'; $r.installedVersion = $srcVer; $r.changed += $dst; Out-Result; exit 0
}
Write-Error 'one of -Check / -Apply / -Remove is required'; exit 1
