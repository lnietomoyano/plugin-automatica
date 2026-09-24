# Instalación asistida — Claude prepara el equipo SOLO (primera vez)

Guía que Claude EJECUTA la primera vez. Regla de oro en cada paso:
**1) comprobar → 2) si ya está, saltar → 3) si falta, instalar (con permiso del usuario) →
4) verificar que quedó bien.** No instales nada sin comprobar antes. Explica cada comando
antes de lanzarlo; el usuario tendrá que aprobarlo.

Detecta el sistema operativo al empezar. Los comandos de abajo son para **Windows
(PowerShell)**; si es Mac/Linux, usa los equivalentes de la sección final.

---

## Paso 1 · Python
**Comprobar:**
```
py --version ; if (-not $?) { python --version }
```
- Si imprime **3.11 o superior** → ya está, salta al Paso 2.
- Si no hay Python o es viejo → instalar.

**Instalar (preferido, winget):**
```
winget install -e --id Python.Python.3.12
```
**Si no hay winget** (comprobar con `winget --version`), descarga oficial silenciosa:
```
Invoke-WebRequest https://www.python.org/ftp/python/3.12.7/python-3.12.7-amd64.exe -OutFile "$env:TEMP\py_setup.exe" ; Start-Process "$env:TEMP\py_setup.exe" -ArgumentList '/quiet InstallAllUsers=0 PrependPath=1 Include_pip=1' -Wait
```
**Verificar** (abre una terminal NUEVA para que tome el PATH):
```
py --version
```
Si sigue sin encontrarse, pídele al usuario que cierre y reabra Claude Code / la terminal.

## Paso 2 · Carpeta de trabajo (AUTOMATICA)
**Preguntar:** «¿Tienes ya una carpeta para los ejercicios de Automática? Si no, te creo una.
¿Dónde la quieres — en el Escritorio (`Desktop\AUTOMATICA`) o en otro sitio?»
**Comprobar / crear:**
```
$carpeta = "$env:USERPROFILE\Desktop\AUTOMATICA" ; if (-not (Test-Path $carpeta)) { New-Item -ItemType Directory -Path $carpeta | Out-Null } ; $carpeta
```
Usa la ruta que elija el usuario. Guárdala para `datos-equipo.md`.

## Paso 3 · Obsidian (opcional, para leer el informe .md bonito)
**Preguntar:** «¿Tienes Obsidian instalado? Sirve para ver el informe. Es opcional; si
quieres te lo instalo.»
**Comprobar:**
```
winget list --id Obsidian.Obsidian ; if (-not $?) { Test-Path "$env:LOCALAPPDATA\Obsidian\Obsidian.exe" }
```
**Instalar (si quiere):**
```
winget install -e --id Obsidian.Obsidian
```
Si no lo quiere, continúa — el informe es un `.md` que se abre con cualquier editor.

## Paso 4 · Entorno virtual + librerías
Dentro de la carpeta de trabajo:
```
cd $carpeta ; python -m venv venv_auto ; venv_auto\Scripts\python.exe -m pip install --upgrade pip ; venv_auto\Scripts\python.exe -m pip install numpy scipy matplotlib control pyqt6
```
**Verificar** (debe imprimir OK):
```
venv_auto\Scripts\python.exe -c "import numpy,scipy,matplotlib,control,PyQt6; print('OK librerias')"
```

## Paso 5 · Datos del alumno
Pregunta: **nombre y nº de matrícula** (y de un segundo autor si hay pareja).
Escribe TODO lo recogido en `datos-equipo.md` (carpeta, ruta de Python =
`<carpeta>\venv_auto\Scripts\python.exe`, SO, autores). Así no se vuelve a preguntar.

## Paso 6 · Listo → a los ejercicios
Confirma en una línea que el entorno está montado y verificado, y dile:
«Ya está todo. Pégame el enunciado del ejercicio (texto, PDF o imagen) y lo resuelvo.»
A partir de aquí sigue el flujo normal del `SKILL.md` (Fase 0 en adelante).

---

## Equivalentes Mac / Linux
- Python: comprobar `python3 --version`; instalar con `brew install python` (Mac) o el gestor
  de paquetes de la distro (`sudo apt install python3 python3-venv python3-pip`, etc.).
- Obsidian: `brew install --cask obsidian` (Mac) o descarga desde obsidian.md.
- venv: `python3 -m venv venv_auto && source venv_auto/bin/activate && pip install numpy scipy matplotlib control pyqt6`.
- Ruta de Python del venv: `<carpeta>/venv_auto/bin/python`.
