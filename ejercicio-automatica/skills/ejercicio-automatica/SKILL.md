---
name: ejercicio-automatica
description: >
  Resuelve de principio a fin un ejercicio de Fundamentos de Automática (3.º GIO,
  ETSII-UPM): modelado secuencial GRAFCET (IEC 60848) + guía GEMMA. Úsala SIEMPRE que
  el usuario pase un enunciado (texto, PDF o imagen) de una planta a automatizar
  (clasificador, embotelladora, transfer, empaquetadora, taladradora, etc.) o pida
  "resolver el ejercicio/caso N", "hacer el GRAFCET/GEMMA", "la simulación interactiva"
  o "el informe PEC". Genera los 3 bloques del profesor + informe Obsidian + simulación
  interactiva testeable, con verificación obligatoria antes de entregar.
---

# Resolver ejercicio de Automática (GRAFCET/GEMMA) de punta a punta

Esta skill automatiza el flujo completo que ya usamos en el curso. Es la versión
ejecutable del `PROMPT_MAESTRO.md` + la guía del profesor + el estilo de informe PEC.
Sigue las fases en orden. No te saltes la Fase 4 (verificación).

## Contexto que DEBES cargar antes de empezar
Estos ficheros de referencia (dentro de la skill) hacen que sea **autocontenida**, sin
depender de memorias personales:
- `reference/gemma-plantillas.md`: numeración estándar de los 6 grafcets + panel de control + modos GEMMA.
- `reference/estructura-informe.md`: la estructura EXACTA del informe (secciones 1-7 estilo PEC).
- `reference/checklist.md`: el checklist anti-errores obligatorio.

Si además existen memorias del curso en este equipo (`proyecto-automatica-embotellado`,
`guia-profesor-metodologia`, etc.), úsalas como refuerzo; pero **no las des por hechas**:
en el ordenador de otra persona pueden no existir.

## FASE -2 · Puesta a punto del equipo (SOLO la primera vez) — auto-instalación
Antes de cualquier otra cosa, comprueba si el equipo ya está listo:
- Lee `datos-equipo.md`. **Si ya está relleno (sin `<PENDIENTE>`) y la ruta de Python
  verifica** (`<python> -c "import numpy,matplotlib,control,PyQt6"` imprime sin error) →
  el equipo ya está montado, **salta directo a la Fase 0**.
- **Si es la primera vez** (campos en `<PENDIENTE>` o falla la verificación) → sigue
  **`reference/instalacion-asistida.md`** paso a paso: Claude comprueba e instala lo que
  falte (Python, carpeta de trabajo, Obsidian opcional, venv + librerías), verificando cada
  paso y pidiendo permiso antes de instalar. Al terminar, escribe `datos-equipo.md` con todo
  (carpeta, ruta de Python, SO, autores) y solo entonces pasa a pedir el enunciado.

Regla: no des por hecho nada del equipo del usuario. Comprobar → si falta, instalar con su
permiso → verificar. No hardcodees rutas ni autores.

---

## FASE 0 · Entender el enunciado y planificar (no escribas código todavía)
1. Lee el enunciado ENTERO (si es PDF/imagen, extrae planta, actuadores, sensores y lo que se pide antes de diseñar). Para el PDF del temario existe `Temario\extraer_pdf.ps1` y el texto ya volcado en `Temario\temario_texto.txt`.
2. Identifica el **diseño GEMMA** que pide (p. ej. A1A2F1D1, A1A2F1F2F3…) y qué modos aplican: marchas de inicio/cierre, parada de urgencia D1, rearme, verificación F5/F6.
3. **Reutiliza plantilla**: si hay ejercicios previos, localiza el más parecido en `Ejercicio-*/` y parte de sus `sim_*.py` / `test_*.py` / `fig_*.py`. Si NO hay ninguno (equipo nuevo), parte de `reference/plantilla-codigo/sim_plantilla.py` + `test_plantilla.py` (motor `Sim` genérico ya testeado). En ambos casos, adapta — NO reescribas desde cero.
4. Si algo es ambiguo, decide con criterio de ingeniería y anótalo; no te pares a preguntar salvo que sea imprescindible.

## FASE 1 · Entorno y estructura de ficheros — EXACTO
- Carpeta de trabajo (= vault de Obsidian) = **la raíz del proyecto** desde la que se invoca la skill. En este equipo es `C:\Users\usuario\Desktop\AUTOMATICA`; en otro ordenador será otra ruta → NO la hardcodees, usa la raíz actual.
- Python del venv: `<raíz>\venv_auto\Scripts\python.exe` en Windows (o `<raíz>/venv_auto/bin/python` en Mac/Linux). Debe tener numpy, scipy, matplotlib, control, pyqt6; tkinter OK → hay ventana interactiva. Si no hay venv, usa el `python` disponible y avisa de qué librerías faltan.
- Crea **siempre** una carpeta nueva `Ejercicio-N_Nombre\` con subcarpeta `output_[caso]\` dentro. Estructura de referencia (mira `Ejercicio-3_Transfer\`):
  ```
  Ejercicio-N_Nombre\
    ejercicioN_[caso].md      ← informe Obsidian (secciones 1-7)
    sim_[caso].py             ← simulación interactiva (clase Sim + dibujo)
    test_[caso].py            ← test headless de la máquina de estados
    fig_[caso].py             ← figura técnica de la planta (300 dpi)
    fig_grafcets.py           ← figuras de los GRAFCET
    output_[caso]\            ← PNGs generados (planta + grafcets)
  ```
- Cuando des comandos para copiar, adáptalos al **SO de `datos-equipo.md`**: en Windows, dos versiones cmd (`&&`, `set VAR=x`) y PowerShell (`;`, `$env:VAR="x"`) — nunca mezcles `;` en cmd; en Mac/Linux, bash (`&&`, `export VAR=x`, `python3`, `venv_auto/bin/python`).

## FASE 2 · Diseño y entregable = 3 bloques del profesor
**BLOQUE 1 · Especificación + tabla de E/S**: descripción física (mecánica, actuadores, sensores); tabla exhaustiva de Entradas (panel `Val, AUT/CaC/CIERRE/INICIO, PE, X51…` + sensores de proceso y finales de carrera) y Salidas (actuadores con notación `+/-`); secuencia operativa por fases GEMMA.

**BLOQUE 2 · Modelado GRAFCET (IEC 60848)** con la numeración estándar del curso (ver `reference/gemma-plantillas.md`):
- GPRODUCCIÓN (G0/G100): etapas `0..n`, divergencias en Y (paralelo) y en O (elección).
- GCONDUCCIÓN: `100=A1, 101=F1, 102=A2, 103=F2, 105=F3` (Transfer usa 104 como puente de vaciado). A1 fuerza producción a reposo con `F/GPRODUCCIÓN:{0}`.
- GSEGURIDAD `20-23`, GREARME `70-75`, GPINICIO `60-65`, GSERVICIO `50-51` — solo los que pida el enunciado.
- Tabla de transiciones (nº · receptividad · significado).

**BLOQUE 3 · Simulación interactiva en Python** (NO figura estática pasiva):
- `sim_[caso].py` con `matplotlib` + `matplotlib.widgets.Button`.
- **Separa la lógica en una clase `Sim`** (estado GEMMA + física, `step()`, métodos `press_*`/`set_*`) del dibujo → así se testea sin pantalla. Bug típico a evitar: durante el rearme, manejar la condición ANTES del `return` de emergencia en `step()`.
- Botones del panel según el diseño (Marcha/Inicio, Paro, Cierre, G_error/P_error/Reparar/Rearme si aplica, material ON/OFF, Reset); panel lateral con sensores/condiciones/salidas en vivo.
- Figura técnica de la planta a **300 dpi** (`matplotlib.patches`) + figuras de GRAFCET.
- **GIF: NO por defecto** (es lo más lento). Deja el guion `SIM_DEMO=1` listo; genéralo solo si lo piden.
- Figuras "suficientemente adornadas" (cuentan para NOTA) pero sin barroquismo: presentables y claras, sin adornos que provoquen solapes. No recortes calidad; recorta riesgo.

## FASE 3 · Informe
Redacta `ejercicioN_[caso].md` en Obsidian siguiendo **`reference/estructura-informe.md`** (secciones numeradas 1-7 estilo PEC, tablas de variables exhaustivas, GRAFCET producción/conducción/seguridad, prompt verbatim, conclusiones). Imágenes embebidas con `![[...]]` y tabla de entregables. **No edites `PROMPT_MAESTRO.md`.**

## FASE 4 · VERIFICACIÓN OBLIGATORIA (no entregar sin esto)
Aplica **`reference/checklist.md`** completo. En resumen:
1. Ejecuta `venv_auto\Scripts\python.exe test_[caso].py` → **todos los escenarios pasan**. Reporta el resultado real; si falla, corrige.
2. Renderiza y **MIRA con Read** cada figura (GRAFCET, planta) y **un fotograma de la ventana de simulación**. Corrige hasta que no haya solapes / texto cortado / elementos montados. Regla matplotlib: todo texto dentro de un panel lleva `zorder` mayor que el relleno.
3. Coherencia de ficheros: imports apuntan a ficheros que existen; nombres citados en el informe = ficheros reales de la carpeta (sin fantasmas).
4. GEMMA correcto: A1 arranque; F2 llena/prepara; F1 normal; A2 parada fin de ciclo; F3 cierre/vaciado→A1; D1/seguridad si se pide.

## FASE 5 · Cierre
- Resumen corto en el chat: qué es, el diseño en 4-5 líneas, y confirmación de que el test pasa y las figuras están verificadas.
- **Guarda en memoria** el ejercicio (enunciado, decisiones, entregables) y cualquier error nuevo con su corrección, siguiendo la memoria `flujo-de-trabajo-ejercicios`.
