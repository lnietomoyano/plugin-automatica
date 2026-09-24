# Skill `ejercicio-automatica` — cómo bajarla y usarla

Esta skill resuelve de punta a punta los ejercicios de Fundamentos de Automática
(GRAFCET/GEMMA) y, la primera vez, **Claude te monta el ordenador solo**: comprueba si
tienes Python, si no lo instala; crea la carpeta de trabajo; te ofrece instalar Obsidian;
prepara las librerías; y te hace las preguntas necesarias. Tú solo apruebas los pasos.

## Lo único que tienes que hacer tú

### 1. Tener Claude Code
Instala la app de Claude Code (escritorio) e inicia sesión.

### 2. Bajar la skill y ponerla en su sitio
Descarga la carpeta `ejercicio-automatica` y cópiala dentro de tu proyecto, en:
```
<tu carpeta>\.claude\skills\ejercicio-automatica\
```
Si no existe `.claude\skills\`, créala. (Puede ser cualquier carpeta; luego Claude te crea
la de trabajo definitiva.)

### 3. Arrancar
Abre Claude Code en esa carpeta y escribe:
```
/ejercicio-automatica
```
La **primera vez**, Claude te preguntará y hará la instalación (Python, carpeta, Obsidian,
librerías) — solo tienes que ir diciendo «sí» y aprobar los comandos. Te pedirá tu **nombre
y nº de matrícula** para el informe.

Las **siguientes veces** ya no instala nada: escribes `/ejercicio-automatica`, pegas el
enunciado (texto, PDF o imagen) y lo resuelve.

---

## Hacerla PÚBLICA (que cualquiera la instale por su cuenta)
Para que se «baje» sin pasártela a mano, se publica como **plugin de Claude Code** en un
repositorio de GitHub que actúa de *marketplace*:
1. Sube esta skill a un repo público de GitHub con la estructura de plugin
   (`.claude-plugin/marketplace.json` + la skill dentro de `skills/`).
2. Cualquiera la instala con, en Claude Code:
   ```
   /plugin marketplace add TU_USUARIO/TU_REPO
   /plugin install ejercicio-automatica
   ```
3. Al instalarla, la skill queda disponible y, al usarla la primera vez, hace la
   auto-instalación del entorno igual que arriba.

> Si quieres esta vía, hay que crear el repo (necesita tu cuenta de GitHub). La estructura
> de plugin se prepara aparte; pídelo y se deja lista para subir.
