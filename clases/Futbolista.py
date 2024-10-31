class Futbolista:

    def __init__(self, dorsal, edad, equipo, nacionalidad, nombre, pie, posicion):
        self.dorsal = dorsal
        self.edad = edad
        self.equipo = equipo
        self.nacionalidad = nacionalidad
        self.nombre = nombre
        self.pie = pie
        self.posicion = posicion

    def __str__(self):
        return f"Dorsal: {self.dorsal} - Edad: {self.edad} - Equipo: {self.equipo} - Nacionalidad: {self.nacionalidad} - Pierna: {self.pie} - Posición {self.posicion}"


def tachar_valor(valor):
    # Cambia el formato del texto para los prints (tacha lo incorrecto).
    return ''.join([char + '\u0336' for char in str(valor)])


def comparar_numeros(coincidencias, jugador_intento, jugador_oculto):
    # Modifica el diccionario con las pistas para que los números te indiquen si son menores o mayores.
    dorsal_intento = int(jugador_intento.dorsal)
    dorsal_oculto = int(jugador_oculto.dorsal)
    edad_intento = int(jugador_intento.edad)
    edad_oculto = int(jugador_oculto.edad)

    if dorsal_oculto > dorsal_intento:
        coincidencias['dorsal'] = f"{tachar_valor(jugador_intento.dorsal)} ↑"
    elif dorsal_oculto < dorsal_intento:
        coincidencias['dorsal'] = f"{tachar_valor(jugador_intento.dorsal)} ↓"
    if edad_oculto > edad_intento:
        coincidencias['edad'] = f"{tachar_valor(jugador_intento.edad)} ↑"
    elif edad_oculto < edad_intento:
        coincidencias['edad'] = f"{tachar_valor(jugador_intento.edad)} ↓"
    return coincidencias


def comparar_jugadores(jugador_intento, jugador_oculto):
    # Compara los atributos de dos jugadores y devuelve un diccionario con las coincidencias y pistas.
    intento_dic = vars(jugador_intento)
    oculto_dic = vars(jugador_oculto)
    coincidencias = {}
    for clave, valor in intento_dic.items():
        if clave in oculto_dic:
            if valor == oculto_dic[clave]:
                coincidencias[clave] = valor
            else:
                coincidencias[clave] = ''.join([char + '\u0336' for char in valor])
    coincidencias = comparar_numeros(coincidencias, jugador_intento, jugador_oculto)
    return coincidencias
