"""
PLANTILLA GENÉRICA de simulación GEMMA (adaptar a cada ejercicio).

Máquina de ejemplo mínima: un cilindro de doble efecto A (A+ extiende, A- retrae)
con finales de carrera a0 (retraído) y a1 (extendido), y un sensor de pieza `p`.
Sirve para arrancar cualquier ejercicio: SUSTITUYE la física y los actuadores por
los del enunciado, pero MANTÉN la estructura (clase Sim separada del dibujo).

Ejecutar la ventana interactiva:  python sim_plantilla.py
Los tests headless viven en test_plantilla.py (no importan matplotlib de ventana).
"""

# ----------------------------------------------------------------------------
# MOTOR (clase Sim): estado GEMMA + física. NADA de dibujo aquí -> testeable.
# ----------------------------------------------------------------------------
class Sim:
    DT = 0.1          # paso de tiempo
    SPEED = 2.0       # velocidad del cilindro (unidades/seg)

    def __init__(self):
        self.reset()

    def reset(self):
        self.mode = "A1"      # modo GEMMA activo: A1,F1,A2,D1 (+F2/F3 si aplica)
        self.xA = 0.0         # posición cilindro A: 0=retraído(a0), 1=extendido(a1)
        self.cmdA = 0         # orden al actuador: +1 = A+, -1 = A-, 0 = parado
        self.piece = False    # hay pieza en el puesto
        self.stop_requested = False
        self.fault = False    # defecto activo (D1)
        self.step_phase = 0   # subetapa dentro de F1 (0=avanzar, 1=retroceder)

    # --- finales de carrera (derivados de la física) ---
    @property
    def a0(self): return self.xA <= 0.001
    @property
    def a1(self): return self.xA >= 0.999

    # --- botones del panel (los llama la GUI o el test) ---
    def press_marcha(self):
        if self.mode in ("A1", "A2") and not self.fault:
            self.mode = "F1"; self.stop_requested = False

    def press_paro(self):          # A2 = parada pedida a fin de ciclo
        if self.mode == "F1":
            self.stop_requested = True

    def press_pe(self):            # seta de emergencia -> D1
        self.fault = True; self.mode = "D1"

    def press_rearme(self):
        # OJO (bug típico): manejar el rearme ANTES del return de emergencia en step().
        if self.mode == "D1":
            self.fault = False; self.cmdA = -1  # llevar a casa
            self.mode = "A6_rearme"

    def set_piece(self, v): self.piece = bool(v)

    # --- física: mueve el cilindro según cmdA ---
    def _fisica(self):
        self.xA += self.cmdA * self.SPEED * self.DT
        self.xA = max(0.0, min(1.0, self.xA))

    # --- un paso de la máquina de estados ---
    def step(self):
        # 1) EMERGENCIA / rearme (máxima prioridad) --------------------------
        if self.mode == "D1":
            self.cmdA = 0
            self._fisica()
            return
        if self.mode == "A6_rearme":       # volviendo a casa tras el fallo
            self.cmdA = -1
            self._fisica()
            if self.a0:
                self.cmdA = 0; self.mode = "A1"
            return

        # 2) CONDUCCIÓN normal ----------------------------------------------
        if self.mode == "A1":
            self.cmdA = -1 if not self.a0 else 0     # asegurar estado inicial

        elif self.mode == "F1":
            if self.step_phase == 0:                 # avanzar con pieza
                if self.piece:
                    self.cmdA = +1
                    if self.a1:
                        self.step_phase = 1
                else:
                    self.cmdA = 0
            else:                                    # retroceder = fin de ciclo
                self.cmdA = -1
                if self.a0:
                    self.step_phase = 0
                    if self.stop_requested:
                        self.mode = "A2"             # parada pedida fin de ciclo

        elif self.mode == "A2":
            self.cmdA = 0                            # retiene estado, parado

        self._fisica()

    # --- estado legible para el panel/tests ---
    def status(self):
        return {"mode": self.mode, "xA": round(self.xA, 2),
                "a0": self.a0, "a1": self.a1, "piece": self.piece,
                "stop": self.stop_requested, "fault": self.fault}


# ----------------------------------------------------------------------------
# DIBUJO / PANEL (solo se ejecuta al lanzar la ventana; NO se importa en tests)
# ----------------------------------------------------------------------------
def run_gui():
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Button

    sim = Sim()
    fig, ax = plt.subplots(figsize=(9, 5))
    plt.subplots_adjust(bottom=0.28)
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")

    # elementos de la planta (dibujo mínimo: un cilindro que crece con xA)
    cuerpo = plt.Rectangle((1, 2.5), 3, 1, fc="#cfd8dc", ec="#455a64", zorder=1)
    vastago = plt.Rectangle((4, 2.8), 0.2, 0.4, fc="#455a64", zorder=2)
    ax.add_patch(cuerpo); ax.add_patch(vastago)
    txt = ax.text(5, 5, "", fontsize=11, zorder=5)      # zorder alto: SIEMPRE encima

    def redibuja():
        vastago.set_width(0.2 + 3 * sim.xA)
        s = sim.status()
        txt.set_text(f"GEMMA: {s['mode']}   a0={s['a0']} a1={s['a1']} "
                     f"pieza={s['piece']} fallo={s['fault']}")
        fig.canvas.draw_idle()

    def tick(_):
        sim.step(); redibuja()

    timer = fig.canvas.new_timer(interval=100)
    timer.add_callback(tick, None); timer.start()

    # botones
    def boton(x, label, cb):
        b = Button(plt.axes([x, 0.12, 0.13, 0.07]), label); b.on_clicked(cb); return b
    b1 = boton(0.05, "Marcha", lambda e: sim.press_marcha())
    b2 = boton(0.20, "Paro",   lambda e: sim.press_paro())
    b3 = boton(0.35, "Pieza",  lambda e: sim.set_piece(not sim.piece))
    b4 = boton(0.50, "PE",     lambda e: sim.press_pe())
    b5 = boton(0.65, "Rearme", lambda e: sim.press_rearme())
    b6 = boton(0.80, "Reset",  lambda e: sim.reset())
    plt.show()


if __name__ == "__main__":
    run_gui()
