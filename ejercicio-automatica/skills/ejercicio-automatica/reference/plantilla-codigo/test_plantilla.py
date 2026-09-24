"""
PLANTILLA de test headless (adaptar por ejercicio).
Importa SOLO la clase Sim -> no abre ventana, corre sin pantalla.
Ejecutar:  python test_plantilla.py   (debe imprimir 'TODOS LOS TESTS PASAN')
"""
from sim_plantilla import Sim


def correr(sim, n):
    for _ in range(n):
        sim.step()


def test_arranque_estado_inicial():
    s = Sim()
    correr(s, 20)
    assert s.mode == "A1" and s.a0, "A1 debe dejar el cilindro en casa (a0)"


def test_ciclo_normal_con_pieza():
    s = Sim()
    s.press_marcha(); s.set_piece(True)
    llego_a1 = False
    for _ in range(40):                 # varios ciclos avanzar/retroceder
        s.step()
        if s.a1:
            llego_a1 = True
    assert s.mode == "F1", "con pieza y sin paro debe seguir en F1"
    assert llego_a1, "en F1 con pieza el cilindro debe extenderse hasta a1"


def test_parada_fin_de_ciclo_A2():
    s = Sim()
    s.press_marcha(); s.set_piece(True)
    correr(s, 15)                       # a mitad de ciclo
    s.press_paro()                      # pedir parada
    correr(s, 40)
    assert s.mode == "A2", "tras pedir paro debe terminar el ciclo y quedar en A2"


def test_emergencia_y_rearme():
    s = Sim()
    s.press_marcha(); s.set_piece(True)
    correr(s, 10)
    s.press_pe()
    assert s.mode == "D1" and s.fault, "PE debe forzar D1"
    correr(s, 5)
    s.press_rearme()
    correr(s, 40)
    assert s.mode == "A1" and not s.fault, "tras rearme vuelve a A1 sin fallo"


if __name__ == "__main__":
    fallos = 0
    for nombre, fn in list(globals().items()):
        if nombre.startswith("test_") and callable(fn):
            try:
                fn(); print(f"  OK  {nombre}")
            except AssertionError as e:
                fallos += 1; print(f" FALLA {nombre}: {e}")
    print("TODOS LOS TESTS PASAN" if fallos == 0 else f"{fallos} TEST(S) FALLAN")
