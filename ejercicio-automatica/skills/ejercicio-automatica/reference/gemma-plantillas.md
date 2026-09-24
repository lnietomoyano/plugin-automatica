# Plantillas GEMMA y panel de control (referencia autocontenida del curso)

Conocimiento base del curso, embebido aquí para que la skill NO dependa de la memoria
personal. Numeración de etapas convenida — reutilizar en todos los ejercicios.

## Numeración estándar de los 6 grafcets
- **GPRODUCCIÓN (GPROD/G0/G100):** etapas `0` (inicial/reposo `E0`) .. `n`. Marco fijo:
  `0 —c.i.·X101→ 1 —[bloque sombreado, se rediseña por ejercicio]→ n+1`, y al final
  **divergencia en O**: `X102 → 0` (para), `X101 → 1` (sigue). El bloque sombreado es lo
  que se adapta a cada planta. Divergencias en Y para puestos/actuadores simultáneos.
- **GCONDUCCIÓN (GCOND):** `100 [A1] · 101 [F1] · 102 [A2] · 103 [F2] · 105 [F3]`
  (el Transfer usa `104` como puente de vaciado antes de F3).
  `100 —val·(AUT+CaC)·X51→ 101 —(v̄al·CaC / pedir parada)→ 102 —Xfin_prod→ 100`.
  A1 fuerza producción a reposo: `F/GPRODUCCIÓN:{0}`. D1 NO añade etapa aquí; la
  emergencia la mete GSEGURIDAD forzando.
- **GSEGURIDAD:** `20..23`. `20 [E20, inicial doble] —e→ 21 [D1: F/GSERVICIO:{50},
  F/GCONDUCCIÓN:{100}, F/GPRODUCCIÓN:{0} + luz "en fallo"] —ē→ 22 [A5] —rearme→ 23 [A6]
  —c.i.→ 20`. Va en OB40 (máxima prioridad). `e` = condición de emergencia (adaptar por
  ejercicio, p. ej. `PE + G_error + P_error`).
- **GREARME/GREARMADO:** `70..75`. `70 —X22→ 71 [acciones rearme]…75 —=1→ 70`. Disparado
  por X22 (A5). Suele llevar los actuadores a casa.
- **GPINICIO (puesta en estado inicial):** `60..65`. `60 —X75·rearme→ 61…65 —=1→ 60` (A6).
- **GSERVICIO:** `50..51`. `50 [INICIO] —conexión→ 51 [SERVICIO/E51] —desconexión→ 50`.
  `X51` (servicio activo) se usa en la transición de arranque de GCOND.

## Panel de control (señales estándar)
Servicio (en servicio), Marcha/Paro (en funcionamiento), Verificación, Seguridad
(en marcha / en fallo). Selectores: `Val` (validación/marcha); modo
`MAN / AUT / CaC (ciclo a ciclo) / CIERRE`; `Verificar: Orden / SIN_ORDEN / TEST`;
`Rearme`; **Paro de Emergencia (PE, seta)**.
Acrónimos: `c.i.` = condiciones iniciales; `CaC` = ciclo a ciclo; `Xk` = etapa k activa.

## Modos GEMMA (resumen)
- Familia F (funcionamiento): F1 producción normal · F2 marcha de preparación (llenar en
  vacío) · F3 marcha de cierre (vaciar) · F4/F5 verificación (con/ sin orden) · F6 marcha de test.
- Familia A (paradas): A1 parada en estado inicial · A2 parada pedida fin de ciclo ·
  A5 preparación para rearme tras defecto · A6 puesta en estado inicial · A7 puesta en servicio.
- Familia D (defecto): D1 parada de emergencia · D2 diagnóstico · D3 producción degradada.

## Implementación PLC S7-1500 (por si el enunciado lo pide)
OB1 = GCONDUCCIÓN, GPRODUCCIÓN, GSERVICIO, GREARME, GPINICIO;
**OB40 (alarmas, máx. prioridad) = GSEGURIDAD.**
