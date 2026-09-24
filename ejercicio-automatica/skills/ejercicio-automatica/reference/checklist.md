# Checklist anti-errores — OBLIGATORIO antes de dar por bueno un ejercicio

Errores históricos que este checklist previene: import roto / fichero fantasma en el
informe (Fase 1 embotellado); figuras con solapes por no mirarlas y texto sin `zorder`
sobre panel (Transfer); comandos con `;` que fallan en cmd.

## 1. Test headless
- Ejecuta `venv_auto\Scripts\python.exe test_[caso].py`.
- Debe haber varios escenarios que recorran TODO el ciclo GEMMA (arranque, normal, parada
  fin de ciclo, cierre/vaciado, y emergencia/rearme si el diseño lo incluye).
- **TODOS pasan.** Reporta el resultado real. Si algo falla, corrige el motor `Sim`, no el test.
- El test NO debe importar tkinter/matplotlib de ventana: la clase `Sim` va en un módulo
  aparte (o importable) para testear sin pantalla.

## 2. Mirar las figuras (no entregar a ciegas)
- Renderiza y **MIRA con Read**: cada GRAFCET, la figura de la planta, y **al menos un
  fotograma de la ventana de simulación**.
- Corrige hasta que NO haya: textos/etiquetas solapados entre sí o con líneas/cajas; texto
  cortado por los bordes; elementos montados unos sobre otros.
- Reglas de dibujo:
  - Etiquetas preferiblemente de una línea y por cuadrante.
  - En matplotlib, **todo texto/símbolo dentro de un panel debe llevar `zorder` mayor** que
    el relleno del panel (si no, queda oculto).
  - Numera TODAS las transiciones; separa bien las ramas paralelas.

## 3. Coherencia de ficheros
- Los `import` apuntan a ficheros que existen (una única fuente de verdad para el motor `Sim`).
- Los nombres de fichero citados en el informe coinciden EXACTAMENTE con los ficheros reales
  de la carpeta (sin fantasmas). Revisa la tabla de entregables contra `dir` de la carpeta.

## 4. GEMMA coherente
- A1 → arranque / estado inicial.
- F2 → llena / prepara en vacío.
- F1 → producción normal.
- A2 → parada a fin de ciclo (retiene estado).
- F3 → cierre (vacía la máquina y vuelve a A1).
- D1 / GSEGURIDAD → solo si el enunciado lo pide; fuerza reinicio y engancha rearme.
