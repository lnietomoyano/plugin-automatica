# Estructura del informe (estilo PEC, secciones 1-7)

Se lee como una PEC de ingeniería real (puntúa más que el estilo tutorial). Manteniendo
debajo el motor interactivo + tests headless.

**Cabecera:** Título / línea `PEC-N · Fundamentos de Automática · 3.º GIO (UPM) · fecha` /
subtítulo técnico / **autores con nº** (Javier Díez Portaceli 23612, Lucas Nieto Moyano 24634).

**1. Objetivo y especificación:** descripción física + qué se pide + secuencia
(ej. arranque F2 → normal F1 → cierre F3 → A1). Frases cortas, tono informe.

**2. Tablas de variables** (subdividida y exhaustiva — es la mayor diferencia de estilo):
- 2.1 Entradas — sensores de presencia (Puesto/Operación/Símbolo).
- 2.2 Entradas — panel de control: `en_servicio, val, MARCHA/PARO, MAN/AUT/CaC, INICIO, CIERRE, Orden/SIN_ORDEN/TEST, REARME, AU (PE)`.
- 2.3 Entradas — finales de carrera de cada actuador: `a1/a0, b1/b0, …`.
- 2.4 Salidas — actuadores con notación `+/-`: `A+/A-, B+/B-, …`.
- 2.5 Modos GEMMA utilizados (tabla Modo/Significado/Familia): A1, A2, F1, F2, F3, F6, D1, D3…

**3. GRAFCET de producción (G100):** divergencia en Y de puestos simultáneos; `ESPERAR`
en la convergencia = sincronismo; etapas numeradas (0..n); receptividades `RRx` = finales de
carrera/temporizaciones; salida `X102`→etapa 0 (fin) / `/X102`→etapa 1 (nuevo ciclo).
Regla de robustez: puesto desactivado = NO incluir su señal en la transición.

**4. GRAFCET de conducción:** `100 A1 · 101 F1 · 102 A2 · 103 F2 · 104 puente de vaciado · 105 F3`.
Arranque doble: `val·INICIO·X51`→F2 (preparación), `val·(AU+CaC)·X51`→F1 (directo).
CIERRE por etapa puente 104 que reengancha a F1 hasta vaciar, entra F3 con presencias
negadas; retorno a 100 con `cond_INI`.

**5. GRAFCET de seguridad** (jerárquico): D1 (seta `AU`) fuerza reinicio
`G100{INIT} · G50{INIT} · G0{INIT}` y activa rearme A5 + preparación A6.
`GSEGURIDAD (G20)`: 20/21 D1·INIT/22 A5·REARME/23 A6·INICIO.
`GREARME (G70)`: 70/71 REARME/72 REARMADO (`5s/X72`).
`GSERVICIO (G50)`: 50/51 A7 (CONEX/DESCONEX). Marcha de test F6 (selector TEST sin orden:
recorre actuadores individualmente sin pieza).

**6. Prompt del modelo:** reproducir **verbatim** el prompt usado para generar la solución (sin editarlo).

**7. Conclusiones:** recap de los 3 niveles GEMMA (producción/conducción/seguridad) + regla de robustez.

- Pies de figura estilo **"Fig. N — …"**.
- Numeración de grafcets: producción G100, conducción 100-105, GSEGURIDAD G20, GREARME G70, GSERVICIO G50.

## Estética de la animación (si se hace la versión web/HTML opcional)
960×560, ~20 fps, paleta grises suaves + morado de acento + verde para activo, bordes
redondeados. Izquierda: planta esquemática con etiquetas que se ponen VERDES al operar.
Derecha: fila de píldoras "Modo GEMMA activo" (activa en morado), fila de sensores de
presencia (verde), caja de estado con texto, leyenda. Secuencia demo auto A1→F2→F1→F3→A1.
**Mantener siempre debajo la versión interactiva con botones + tests headless.**
