from api.api import hacer_peticion
from funciones import funciones
from interfaz import interfaz_grafica
from api import api

jugadores = []

if __name__ == "__main__":
    jugadores = hacer_peticion()

if jugadores:
    for jugador in jugadores:
        print(jugador)
else:
    print("No hay jugadores")