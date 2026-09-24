# Publica los cambios de la skill en GitHub.
# Uso:  .\publicar.ps1 "mensaje del cambio"   (el mensaje es opcional)
param([string]$mensaje = "")

$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot   # la carpeta de este script (plugin-automatica)

if ([string]::IsNullOrWhiteSpace($mensaje)) {
    $mensaje = "Actualizacion skill " + (Get-Date -Format "yyyy-MM-dd HH:mm")
}

git add -A
# ¿hay algo que subir?
git diff --cached --quiet
if ($LASTEXITCODE -eq 0) {
    Write-Host "No hay cambios que publicar." -ForegroundColor Yellow
    return
}
git commit -m $mensaje
git push
Write-Host "`nPublicado: https://github.com/lnietomoyano/plugin-automatica" -ForegroundColor Green
