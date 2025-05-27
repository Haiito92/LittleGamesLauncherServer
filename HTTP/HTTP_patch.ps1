Write-Output "Start of patch update build process."
Write-Output "Fetching all branches.`n"

cd ../
git fetch origin
git checkout master

Write-Output "Merging dev into master..."
git merge --no-ff origin/dev -m "Merge dev into main - patch update"
Write-Output "`n"

cd HTTP

Write-Output "`nChecking current build version..."
$versionFile = "version.txt"
$version = Get-Content $versionFile
Write-Output "Current version: $version`n"

Write-Output "Incrementing patch..."
$versionParts = $version -split '\.'

[int]$patch = [int]$versionParts[2]
$patch++
$versionParts[2] = $patch.ToString()

$newVersion = $versionParts -join '.'
Write-Output "New version: $newVersion`n"

Write-Output "Writing new version to: ""$versionFile""..."
Set-Content -Path $versionFile -Value $newVersion
Write-Output "New version written.`n"

# Write-Output "Building project..."
# pyinstaller --onefile serverHTTP.py
# Write-Output "`n"

cd ../

Write-Output "Adding changes..."
git add .
Write-Output "Committing changes..."
git commit -m "Bump patch version to $newVersion and build"
Write-Output "`n"

Write-Output "Setting and Pushing tag..."
git tag v$newVersion
git push origin v$newVersion
Write-Output "`n"

Write-Output "Pushing changes to origin master..."
git push
Write-Output "`n"

Write-Output "End of patch update build process."