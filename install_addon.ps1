# run script by ".\install_addon.ps1"
# open blender with & 'c:\Program Files\Blender Foundation\Blender 4.4\blender.exe'

# Configuration
$BlenderVersion = "4.4"
$AddonName = "Default_Setup"
$BlenderPath = "$env:APPDATA\Blender Foundation\Blender\$BlenderVersion"
$ExtensionPath = "$BlenderPath\extensions\user_default\$AddonName"
$ZipPath = ".\$AddonName.zip"

# Print current configuration
Write-Host "=== Addon Cleanup Script ==="
Write-Host "Blender Version: $BlenderVersion"
Write-Host "Addon Name: $AddonName"
Write-Host "Target Path: $ExtensionPath"

# Clean up old installation
if (Test-Path $ExtensionPath) {
    Write-Host "`nRemoving existing installation..."
    Remove-Item -Path $ExtensionPath -Recurse -Force
    Write-Host "Addon removed successfully!"
} else {
    Write-Host "`nNo existing installation found."
}

# Create temp directory for proper structure
$TempDir = ".\temp_build"
Write-Host "`nPreparing files..."

# Clean up any existing temp directory
if (Test-Path $TempDir) {
    Remove-Item $TempDir -Recurse -Force
}

# Create temp directory
New-Item -ItemType Directory -Path $TempDir -Force | Out-Null

# Copy files maintaining structure
Copy-Item "*.py" -Destination $TempDir
Copy-Item "Operators" -Destination $TempDir -Recurse
Copy-Item "Panels" -Destination $TempDir -Recurse
Copy-Item "blender_manifest.toml" -Destination $TempDir

# Create zip file
Write-Host "`nCreating zip file..."
if (Test-Path $ZipPath) {
    Remove-Item $ZipPath -Force
}
Compress-Archive -Path "$TempDir\*" -DestinationPath $ZipPath -Force
Write-Host "Zip file created at: $(Resolve-Path $ZipPath)"

# Clean up temp directory
Remove-Item $TempDir -Recurse -Force

Write-Host "`n=== Cleanup Complete ==="
Write-Host "You can now install the addon through Blender's preferences using the zip file"

# Ask for confirmation before launching Blender
$launch = Read-Host "`nDo you want to launch Blender? (y/n)"
if ($launch -eq 'y' -or $launch -eq 'Y') {
    Write-Host "Launching Blender with console..."
    & 'c:\Program Files\Blender Foundation\Blender 4.4\blender.exe' -con
} else {
    Write-Host "Blender launch skipped."
}