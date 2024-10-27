from api.api import creacion_api
from clases.Futbolista import comparar_jugadores
from funciones.funciones import seleccionar_jugador_oculto, introduce_futbolista, buscar_futbolista, comprobar_victoria

if __name__ == "__main__":
    jugadores = creacion_api()
    if jugadores:
        jugador_oculto = seleccionar_jugador_oculto(jugadores)
        print(jugador_oculto.nombre)
        victoria = False
        while not victoria:
            nombre_intento = introduce_futbolista(jugadores)
            if nombre_intento:
                jugador_intento = buscar_futbolista(jugadores, nombre_intento)
                print(f"{jugador_intento.__str__()}")
                coincidencias = comparar_jugadores(jugador_intento, jugador_oculto)
                print(
                    f"Dorsal: {coincidencias['dorsal']} - Edad: {coincidencias['edad']} - Equipo: {coincidencias['equipo']}"
                    f" - Nacionalidad: {coincidencias['nacionalidad']} - Pierna: {coincidencias['pie']} "
                    f"- Posición: {coincidencias['posicion']}")
                victoria = comprobar_victoria(jugador_intento, jugador_oculto)
    else:
        print("No hay jugadores")

print("Fin del juego")
