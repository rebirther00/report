$root = "C:\Users\onest\src\report"
Get-ChildItem $root -Filter "_*.ps1" | ForEach-Object {
    Remove-Item $_.FullName -Force
    Write-Output "Removed: $($_.Name)"
}
$workDir = Join-Path $root "_hwpx_v2_work"
if (Test-Path $workDir) {
    Remove-Item $workDir -Recurse -Force
    Write-Output "Removed: _hwpx_v2_work/"
}
