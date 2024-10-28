from random import randint
from clases.Futbolista import Futbolista


def seleccionar_jugador_oculto(jugadores):
    # Selecciona un jugador oculto (es el que hay que adivinar)
    indice_random = randint(0, len(jugadores) - 1)
    jugador_oculto = jugadores[indice_random]
    return Futbolista(jugador_oculto['Dorsal'], jugador_oculto['Edad'], jugador_oculto['Equipo'],
                      jugador_oculto['Nacionalidad'], jugador_oculto['Nombre'], jugador_oculto['Pie'],
                      jugador_oculto['Posicion'])


def introduce_futbolista(jugadores):
    # Solicita al usuario que introduzca el nombre de un futbolista.
    nombre_correcto = False
    while not nombre_correcto:
        entrada_jugador = str(input(f"Jugador: "))
        for jugador in jugadores:
            if entrada_jugador.lower() == jugador['Nombre'].lower():
                return entrada_jugador
        print("Nombre de jugador inválido")
    return None


def buscar_futbolista(jugadores, nombre):
    # Busca un futbolista por nombre en la lista de jugadores y lo devuelve como objeto Futbolista.
    for jugador in jugadores:
        if jugador['Nombre'].lower() == nombre.lower():
            return Futbolista(jugador['Dorsal'], jugador['Edad'], jugador['Equipo'],
                              jugador['Nacionalidad'], jugador['Nombre'], jugador['Pie'],
                              jugador['Posicion'])
    return None


def comprobar_victoria(jugador_intento, jugador_oculto):
    # Comprueba si el intento del usuario coincide con el jugador oculto.
    if jugador_intento.nombre == jugador_oculto.nombre:
        print(f"Ganaste, era {jugador_oculto.nombre}.")
        return True
    else:
        print("Inténtalo de nuevo")
        return False
