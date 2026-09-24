# Plugin `ejercicio-automatica` para Claude Code

Skill que resuelve de punta a punta los ejercicios de **Fundamentos de Automática**
(3.º GIO, ETSII-UPM): modelado secuencial **GRAFCET (IEC 60848)** + guía **GEMMA**.
Genera los 3 bloques del profesor (especificación + tabla E/S, GRAFCET de
conducción/producción/seguridad, simulación interactiva testeable) y el informe.

La **primera vez**, Claude comprueba y monta el entorno por ti: Python, carpeta de trabajo,
Obsidian (opcional) y librerías. Solo tienes que aprobar los pasos.

## Instalar (para cualquiera, desde su ordenador)
En Claude Code:
```
/plugin marketplace add USUARIO_GITHUB/NOMBRE_REPO
/plugin install ejercicio-automatica
```
Sustituye `USUARIO_GITHUB/NOMBRE_REPO` por el repo donde subas esto (p. ej.
`lucasnieto/plugin-automatica`).

Después, en cualquier proyecto:
```
/ejercicio-automatica
```
La primera vez monta el entorno y pide tus datos (nombre, matrícula). Luego, cada ejercicio
= pegar el enunciado (texto, PDF o imagen) y Claude lo resuelve.

## Publicar este plugin (una vez)
1. Crea un repositorio **público** en GitHub.
2. Sube el contenido de esta carpeta a la raíz del repo:
   ```
   git init
   git add .
   git commit -m "Plugin ejercicio-automatica"
   git branch -M main
   git remote add origin https://github.com/USUARIO_GITHUB/NOMBRE_REPO.git
   git push -u origin main
   ```
3. Comparte con quien quieras las dos líneas de "Instalar" de arriba con tu usuario/repo.

## Estructura
```
plugin-automatica/                     ← raíz del repo (marketplace)
  .claude-plugin/marketplace.json      ← lista los plugins del marketplace
  ejercicio-automatica/                ← el plugin
    .claude-plugin/plugin.json         ← manifiesto del plugin
    skills/ejercicio-automatica/       ← la skill (SKILL.md + reference/ + plantillas)
```

## Requisitos del usuario final
- Claude Code (app de escritorio o CLI).
- Conexión a internet la primera vez (para instalar Python/librerías si no los tiene).
- Windows, Mac o Linux (los comandos se adaptan al SO).
