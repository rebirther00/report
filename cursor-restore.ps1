# Cursor Complete Restore Script
# Date: 2026-03-06
# Description: Restore backed up Cursor settings to new account

param(
    [Parameter(Mandatory=$true)]
    [string]$BackupPath,
    [switch]$SkipExtensions = $false,
    [switch]$SkipMCP = $false
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

function Write-WarningMsg {
    param([string]$Message)
    Write-Host "[WARNING] " -ForegroundColor Yellow -NoNewline
    Write-Host $Message -ForegroundColor Yellow
}

function Write-InfoMsg {
    param([string]$Message)
    Write-Host "[INFO] " -ForegroundColor Yellow -NoNewline
    Write-Host $Message -ForegroundColor White
}

# Start
Clear-Host
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  Cursor Complete Restore Script" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Check backup path
if (-not (Test-Path $BackupPath)) {
    Write-ErrorMsg "Backup path not found: $BackupPath"
    exit 1
}

Write-Step "Backup Path: $BackupPath"
Write-Host ""

# Define paths
$CursorUserPath = "$env:APPDATA\Cursor\User"
$SkillsPath = "C:\Users\$env:USERNAME\.cursor\skills-cursor"

# User confirmation
Write-WarningMsg "This will overwrite existing Cursor settings!"
Write-Host "Current account: " -NoNewline -ForegroundColor Gray
Write-Host "$env:USERNAME" -ForegroundColor Yellow
Write-Host ""
$confirm = Read-Host "Continue? (Y/N)"

if ($confirm -ne "Y" -and $confirm -ne "y") {
    Write-InfoMsg "Restore cancelled"
    exit 0
}

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  Step 1: Restore Settings Files" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan

# Create Cursor User folder if needed
if (-not (Test-Path $CursorUserPath)) {
    try {
        New-Item -Path $CursorUserPath -ItemType Directory -Force | Out-Null
        Write-Success "Cursor User folder created"
    } catch {
        Write-ErrorMsg "Failed to create Cursor User folder: $_"
    }
}

# Restore settings.json
$settingsSource = Join-Path $BackupPath "settings.json"
$settingsDest = Join-Path $CursorUserPath "settings.json"

if (Test-Path $settingsSource) {
    try {
        # Backup existing file
        if (Test-Path $settingsDest) {
            $backupName = "settings.json.backup." + (Get-Date -Format "yyyyMMdd-HHmmss")
            Copy-Item -Path $settingsDest -Destination (Join-Path $CursorUserPath $backupName) -Force
            Write-InfoMsg "Existing settings.json backed up: $backupName"
        }
        
        Copy-Item -Path $settingsSource -Destination $settingsDest -Force
        Write-Success "settings.json restored"
    } catch {
        Write-ErrorMsg "Failed to restore settings.json: $_"
    }
} else {
    Write-WarningMsg "settings.json not found in backup"
}

# Restore keybindings.json
$keybindingsSource = Join-Path $BackupPath "keybindings.json"
$keybindingsDest = Join-Path $CursorUserPath "keybindings.json"

if (Test-Path $keybindingsSource) {
    try {
        # Backup existing file
        if (Test-Path $keybindingsDest) {
            $backupName = "keybindings.json.backup." + (Get-Date -Format "yyyyMMdd-HHmmss")
            Copy-Item -Path $keybindingsDest -Destination (Join-Path $CursorUserPath $backupName) -Force
            Write-InfoMsg "Existing keybindings.json backed up: $backupName"
        }
        
        Copy-Item -Path $keybindingsSource -Destination $keybindingsDest -Force
        Write-Success "keybindings.json restored"
    } catch {
        Write-ErrorMsg "Failed to restore keybindings.json: $_"
    }
} else {
    Write-WarningMsg "keybindings.json not found in backup"
}

if (-not $SkipExtensions) {
    Write-Host ""
    Write-Host "======================================" -ForegroundColor Cyan
    Write-Host "  Step 2: Install Extensions" -ForegroundColor Cyan
    Write-Host "======================================" -ForegroundColor Cyan

    $extensionsFile = Join-Path $BackupPath "extensions-list.txt"
    
    if (Test-Path $extensionsFile) {
        try {
            $extensions = Get-Content $extensionsFile
            $totalCount = ($extensions | Measure-Object).Count
            $installedCount = 0
            $failedCount = 0
            
            Write-InfoMsg "Installing $totalCount extensions..."
            Write-Host ""
            
            foreach ($extension in $extensions) {
                if ($extension.Trim() -ne "") {
                    Write-Host "  Installing: " -NoNewline -ForegroundColor Gray
                    Write-Host "$extension" -ForegroundColor White
                    
                    try {
                        $result = & code --install-extension $extension 2>&1
                        if ($LASTEXITCODE -eq 0) {
                            $installedCount++
                        } else {
                            $failedCount++
                            Write-WarningMsg "    Failed: $extension"
                        }
                    } catch {
                        $failedCount++
                        Write-WarningMsg "    Error: $_"
                    }
                }
            }
            
            Write-Host ""
            Write-Success "Extensions installed (Success: $installedCount, Failed: $failedCount)"
        } catch {
            Write-ErrorMsg "Failed to install extensions: $_"
        }
    } else {
        Write-WarningMsg "Extensions list not found in backup"
    }
} else {
    Write-InfoMsg "Skipping extensions installation (-SkipExtensions)"
}

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  Step 3: Restore Agent Skills" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan

$skillsSource = Join-Path $BackupPath "skills-cursor"

if (Test-Path $skillsSource) {
    try {
        # Create Skills folder
        if (-not (Test-Path $SkillsPath)) {
            New-Item -Path $SkillsPath -ItemType Directory -Force | Out-Null
        }
        
        # Backup existing Skills
        if ((Get-ChildItem $SkillsPath -ErrorAction SilentlyContinue | Measure-Object).Count -gt 0) {
            $backupName = "skills-backup-" + (Get-Date -Format "yyyyMMdd-HHmmss")
            $skillsBackup = Join-Path (Split-Path $SkillsPath) $backupName
            Copy-Item -Path $SkillsPath -Destination $skillsBackup -Recurse -Force
            Write-InfoMsg "Existing Skills backed up: $backupName"
        }
        
        # Restore Skills
        Copy-Item -Path "$skillsSource\*" -Destination $SkillsPath -Recurse -Force
        $skillCount = (Get-ChildItem $SkillsPath -Directory | Measure-Object).Count
        Write-Success "Agent Skills restored ($skillCount skills)"
        
        # List skills
        Get-ChildItem $SkillsPath -Directory | ForEach-Object {
            Write-Host "  - " -ForegroundColor Gray -NoNewline
            Write-Host $_.Name -ForegroundColor Gray
        }
    } catch {
        Write-ErrorMsg "Failed to restore Agent Skills: $_"
    }
} else {
    Write-WarningMsg "Agent Skills not found in backup"
}

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  Step 4: Restore Cursor Rules" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan

$rulesSource = Join-Path $BackupPath "project-cursor-rules"

if (Test-Path $rulesSource) {
    Write-InfoMsg "Cursor Rules must be restored per project"
    Write-Host ""
    Write-Host "  Backup location: " -NoNewline -ForegroundColor Gray
    Write-Host "$rulesSource" -ForegroundColor White
    Write-Host ""
    Write-Host "  Restore instructions:" -ForegroundColor Gray
    Write-Host "    1. Navigate to your project folder" -ForegroundColor Gray
    Write-Host "    2. Copy .cursor folder to project" -ForegroundColor Gray
    Write-Host "    3. Or clone project via Git (auto-included)" -ForegroundColor Gray
    Write-Host ""
    
    $copyRules = Read-Host "Copy Cursor Rules to a project now? (Y/N)"
    if ($copyRules -eq "Y" -or $copyRules -eq "y") {
        $projectPath = Read-Host "Enter project path"
        if (Test-Path $projectPath) {
            try {
                $rulesDest = Join-Path $projectPath ".cursor"
                Copy-Item -Path $rulesSource -Destination $rulesDest -Recurse -Force
                Write-Success "Cursor Rules restored to: $projectPath"
            } catch {
                Write-ErrorMsg "Failed to restore Cursor Rules: $_"
            }
        } else {
            Write-WarningMsg "Project path not found"
        }
    }
} else {
    Write-WarningMsg "Cursor Rules not found in backup"
}

if (-not $SkipMCP) {
    Write-Host ""
    Write-Host "======================================" -ForegroundColor Cyan
    Write-Host "  Step 5: Restore MCP Server Settings" -ForegroundColor Cyan
    Write-Host "======================================" -ForegroundColor Cyan

    $mcpSource = Join-Path $BackupPath "globalStorage"
    $mcpDest = Join-Path $CursorUserPath "globalStorage"

    if (Test-Path $mcpSource) {
        try {
            # Backup globalStorage
            if (Test-Path $mcpDest) {
                $backupName = "globalStorage.backup." + (Get-Date -Format "yyyyMMdd-HHmmss")
                $mcpBackup = Join-Path $CursorUserPath $backupName
                Copy-Item -Path $mcpDest -Destination $mcpBackup -Recurse -Force
                Write-InfoMsg "Existing MCP settings backed up: $backupName"
            }
            
            # Restore MCP settings
            Copy-Item -Path $mcpSource -Destination $mcpDest -Recurse -Force
            Write-Success "MCP server settings restored"
        } catch {
            Write-ErrorMsg "Failed to restore MCP settings: $_"
        }
    } else {
        Write-WarningMsg "MCP server settings not found in backup"
    }
} else {
    Write-InfoMsg "Skipping MCP server settings restore (-SkipMCP)"
}

Write-Host ""
Write-Host "======================================" -ForegroundColor Green
Write-Host "  Restore Complete!" -ForegroundColor Green
Write-Host "======================================" -ForegroundColor Green
Write-Host ""

Write-Success "Cursor environment successfully restored"
Write-Host ""

Write-WarningMsg "Next steps:"
Write-Host "  1. Restart Cursor to apply settings" -ForegroundColor Yellow
Write-Host "  2. Verify Python path and other environment-specific settings" -ForegroundColor Yellow
Write-Host "  3. Check SSH server addresses" -ForegroundColor Yellow
Write-Host "  4. Configure Git user information" -ForegroundColor Yellow
Write-Host ""

Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  Additional Settings Required" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

Write-InfoMsg "Python path check:"
Write-Host "  Current: c:\Users\sharp\AppData\Local\Microsoft\WindowsApps\python3.11.exe" -ForegroundColor Gray
Write-Host "  Verify Python is installed in new environment" -ForegroundColor Gray
Write-Host ""

Write-InfoMsg "Git configuration:"
Write-Host "  git config --global user.name `"Your Name`"" -ForegroundColor Gray
Write-Host "  git config --global user.email `"your.email@example.com`"" -ForegroundColor Gray
Write-Host ""

Write-InfoMsg "SSH remote servers:"
Write-Host "  Check remote.SSH.remotePlatform in settings.json" -ForegroundColor Gray
Write-Host "  Verify server addresses are valid in new environment" -ForegroundColor Gray
Write-Host ""

$restartCursor = Read-Host "Restart Cursor now? (Y/N)"
if ($restartCursor -eq "Y" -or $restartCursor -eq "y") {
    Write-InfoMsg "Restarting Cursor..."
    
    # Stop Cursor processes
    Get-Process | Where-Object { $_.ProcessName -like "*Cursor*" } | Stop-Process -Force
    Start-Sleep -Seconds 2
    
    # Start Cursor (path may vary)
    $cursorPath = "$env:LOCALAPPDATA\Programs\Cursor\Cursor.exe"
    if (Test-Path $cursorPath) {
        Start-Process $cursorPath
        Write-Success "Cursor restarted"
    } else {
        Write-WarningMsg "Cursor executable not found. Please start manually."
    }
}

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
