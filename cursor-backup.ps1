# Cursor Complete Backup Script
# Date: 2026-03-06
# Description: Backup all Cursor settings, extensions, rules, skills, and MCP configurations

param(
    [string]$BackupPath = "",
    [switch]$IncludeProjects = $false
)

# Output functions
function Write-Step {
    param([string]$Message)
    Write-Host ">>> " -ForegroundColor Cyan -NoNewline
    Write-Host $Message -ForegroundColor White
}

function Write-Success {
    param([string]$Message)
    Write-Host "[OK] " -ForegroundColor Green -NoNewline
    Write-Host $Message -ForegroundColor White
}

function Write-ErrorMsg {
    param([string]$Message)
    Write-Host "[ERROR] " -ForegroundColor Red -NoNewline
    Write-Host $Message -ForegroundColor White
}

function Write-InfoMsg {
    param([string]$Message)
    Write-Host "[INFO] " -ForegroundColor Yellow -NoNewline
    Write-Host $Message -ForegroundColor White
}

# Start
Clear-Host
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  Cursor Complete Backup Script" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Set backup path
if ($BackupPath -eq "") {
    $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $BackupPath = Join-Path $PSScriptRoot "cursor-backup-$timestamp"
}

Write-Step "Backup Path: $BackupPath"
Write-Host ""

# Create backup folder
try {
    New-Item -Path $BackupPath -ItemType Directory -Force | Out-Null
    Write-Success "Backup folder created"
} catch {
    Write-ErrorMsg "Failed to create backup folder: $_"
    exit 1
}

# Define paths
$CursorUserPath = "$env:APPDATA\Cursor\User"
$SkillsPath = "C:\Users\$env:USERNAME\.cursor\skills-cursor"
$ProjectPath = "c:\Users\sharp\OneDrive\문서\gitLocal\report"

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  Step 1: Backup Settings Files" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan

# Backup settings.json
$settingsSource = Join-Path $CursorUserPath "settings.json"
$settingsDest = Join-Path $BackupPath "settings.json"

if (Test-Path $settingsSource) {
    try {
        Copy-Item -Path $settingsSource -Destination $settingsDest -Force
        $size = (Get-Item $settingsDest).Length
        Write-Success "settings.json backed up ($size bytes)"
    } catch {
        Write-ErrorMsg "Failed to backup settings.json: $_"
    }
} else {
    Write-InfoMsg "settings.json not found"
}

# Backup keybindings.json
$keybindingsSource = Join-Path $CursorUserPath "keybindings.json"
$keybindingsDest = Join-Path $BackupPath "keybindings.json"

if (Test-Path $keybindingsSource) {
    try {
        Copy-Item -Path $keybindingsSource -Destination $keybindingsDest -Force
        $size = (Get-Item $keybindingsDest).Length
        Write-Success "keybindings.json backed up ($size bytes)"
    } catch {
        Write-ErrorMsg "Failed to backup keybindings.json: $_"
    }
} else {
    Write-InfoMsg "keybindings.json not found"
}

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  Step 2: Backup Extensions List" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan

try {
    $extensionsFile = Join-Path $BackupPath "extensions-list.txt"
    $extensions = & code --list-extensions
    $extensions | Out-File -FilePath $extensionsFile -Encoding UTF8
    $count = ($extensions | Measure-Object).Count
    Write-Success "Extensions list backed up ($count extensions)"
} catch {
    Write-ErrorMsg "Failed to backup extensions list: $_"
}

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  Step 3: Backup Agent Skills" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan

if (Test-Path $SkillsPath) {
    try {
        $skillsBackupPath = Join-Path $BackupPath "skills-cursor"
        Copy-Item -Path $SkillsPath -Destination $skillsBackupPath -Recurse -Force
        $skillCount = (Get-ChildItem $skillsBackupPath -Directory | Measure-Object).Count
        Write-Success "Agent Skills backed up ($skillCount skills)"
        
        # List skills
        Get-ChildItem $skillsBackupPath -Directory | ForEach-Object {
            Write-Host "  - " -ForegroundColor Gray -NoNewline
            Write-Host $_.Name -ForegroundColor Gray
        }
    } catch {
        Write-ErrorMsg "Failed to backup Agent Skills: $_"
    }
} else {
    Write-InfoMsg "Agent Skills folder not found"
}

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  Step 4: Backup Cursor Rules" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan

if (Test-Path $ProjectPath) {
    try {
        $rulesSource = Join-Path $ProjectPath ".cursor"
        $rulesDest = Join-Path $BackupPath "project-cursor-rules"
        
        if (Test-Path $rulesSource) {
            Copy-Item -Path $rulesSource -Destination $rulesDest -Recurse -Force
            $ruleCount = (Get-ChildItem $rulesDest -Recurse -File | Measure-Object).Count
            Write-Success "Cursor Rules backed up ($ruleCount files)"
        } else {
            Write-InfoMsg "No .cursor folder in project"
        }
    } catch {
        Write-ErrorMsg "Failed to backup Cursor Rules: $_"
    }
} else {
    Write-InfoMsg "Project path not found"
}

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  Step 5: Backup MCP Server Settings" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan

$mcpSource = Join-Path $CursorUserPath "globalStorage"

if (Test-Path $mcpSource) {
    try {
        $mcpDest = Join-Path $BackupPath "globalStorage"
        Copy-Item -Path $mcpSource -Destination $mcpDest -Recurse -Force
        $mcpSize = (Get-ChildItem $mcpDest -Recurse -File | Measure-Object -Property Length -Sum).Sum
        $mcpSizeMB = [math]::Round($mcpSize / 1MB, 2)
        Write-Success "MCP server settings backed up ($mcpSizeMB MB)"
    } catch {
        Write-ErrorMsg "Failed to backup MCP settings: $_"
    }
} else {
    Write-InfoMsg "MCP server settings not found"
}

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  Step 6: Create Backup Info File" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan

$backupInfo = @"
Cursor Environment Backup Information
======================================

Backup Date: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
Account: $env:USERNAME
Computer: $env:COMPUTERNAME
Windows: $((Get-CimInstance Win32_OperatingSystem).Caption)

Backup Contents:
----------------
- settings.json
- keybindings.json
- Extensions list ($count extensions)
- Agent Skills (5 skills)
- Cursor Rules (project)
- MCP server settings

Restore Instructions:
---------------------
PowerShell command:
.\cursor-restore.ps1 -BackupPath "$BackupPath"

Or manual restore:
See cursor-backup-restore-guide.md

Notes:
------
- Username may differ on new account
- Python path may need adjustment
- SSH server addresses need verification
- Git config must be set separately

"@

$infoFile = Join-Path $BackupPath "README.txt"
$backupInfo | Out-File -FilePath $infoFile -Encoding UTF8
Write-Success "Backup info file created"

Write-Host ""
Write-Host "======================================" -ForegroundColor Green
Write-Host "  Backup Complete!" -ForegroundColor Green
Write-Host "======================================" -ForegroundColor Green
Write-Host ""
Write-Success "Backup Path: $BackupPath"
Write-Host ""

# Calculate total size
$totalSize = (Get-ChildItem $BackupPath -Recurse -File | Measure-Object -Property Length -Sum).Sum
$totalSizeMB = [math]::Round($totalSize / 1MB, 2)

Write-Host "Total backup size: " -NoNewline
Write-Host "$totalSizeMB MB" -ForegroundColor Yellow

Write-Host ""
Write-InfoMsg "Restore instructions:"
Write-Host "  1. Automatic: .\cursor-restore.ps1 -BackupPath `"$BackupPath`"" -ForegroundColor Gray
Write-Host "  2. Manual: See cursor-backup-restore-guide.md" -ForegroundColor Gray
Write-Host ""

# Open backup folder option
$openFolder = Read-Host "Open backup folder? (Y/N)"
if ($openFolder -eq "Y" -or $openFolder -eq "y") {
    explorer $BackupPath
}

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
