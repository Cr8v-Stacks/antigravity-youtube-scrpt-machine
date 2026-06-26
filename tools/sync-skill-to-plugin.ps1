# sync-skill-to-plugin.ps1
# Run this after making any changes to the skill files in the workspace.
# It syncs the master copy to both the active Antigravity plugin and the original Human Minds directory.
#
# Usage: Right-click > Run with PowerShell
#        OR in a terminal: .\tools\sync-skill-to-plugin.ps1

$source = "C:\Users\HP\Documents\Antigravity Youtube Scrpt Machine\skills\youtube-content-machine"
$plugin = "C:\Users\HP\.gemini\config\plugins\youtube-content-machine-plugin\skills\youtube-content-machine"
$humanMinds = "C:\Users\HP\Documents\Human Minds Youtube Content Machine\skills\youtube-content-machine"

Write-Host "Syncing skill to plugin..." -ForegroundColor Cyan
robocopy $source $plugin /E /IS /IT
Write-Host ""

Write-Host "Syncing skill to Human Minds directory..." -ForegroundColor Cyan
robocopy $source $humanMinds /E /IS /IT
Write-Host ""

Write-Host "Done. Running validator on plugin copy..." -ForegroundColor Cyan
python "$plugin\scripts\quick_validate.py"
Write-Host ""
Write-Host "Sync complete." -ForegroundColor Green
