from flask import Flask, jsonify
import requests


app = Flask(__name__)

# Creación de API
@app.route('/goldle/jugadores', methods=['GET'])
def obtener_lista():
    jugadores = [
        # Atlético de Madrid
        {"Nombre": "Jan Oblak", "Equipo": "Atlético de Madrid", "Pie": "Derecha", "Posicion": "POR", "Edad": "31",
         "Nacionalidad": "Eslovenia", "Dorsal": "13"},
        {"Nombre": "Juan Musso", "Equipo": "Atlético de Madrid", "Pie": "Derecha", "Posicion": "POR", "Edad": "30",
         "Nacionalidad": "Argentina", "Dorsal": "1"},
        {"Nombre": "José Giménez", "Equipo": "Atlético de Madrid", "Pie": "Derecha", "Posicion": "DEF",
         "Edad": "29", "Nacionalidad": "Uruguay", "Dorsal": "2"},
        {"Nombre": "César Azpilicueta", "Equipo": "Atlético de Madrid", "Pie": "Derecha", "Posicion": "DEF",
         "Edad": "35", "Nacionalidad": "España", "Dorsal": "3"},
        {"Nombre": "Rodrigo De Paul", "Equipo": "Atlético de Madrid", "Pie": "Derecha", "Posicion": "MED",
         "Edad": "30", "Nacionalidad": "Argentina", "Dorsal": "5"},
        {"Nombre": "Koke", "Equipo": "Atlético de Madrid", "Pie": "Derecha", "Posicion": "MED", "Edad": "32",
         "Nacionalidad": "España", "Dorsal": "6"},
        {"Nombre": "Antoine Griezmann", "Equipo": "Atlético de Madrid", "Pie": "Izquierda", "Posicion": "DEL",
         "Edad": "33", "Nacionalidad": "Francia", "Dorsal": "7"},
        {"Nombre": "Pablo Barrios", "Equipo": "Atlético de Madrid", "Pie": "Derecha", "Posicion": "MED",
         "Edad": "21", "Nacionalidad": "España", "Dorsal": "8"},
        {"Nombre": "Alexander Sørloth", "Equipo": "Atlético de Madrid", "Pie": "Derecha", "Posicion": "DEL",
         "Edad": "28", "Nacionalidad": "Noruega", "Dorsal": "9"},
        {"Nombre": "Ángel Correa", "Equipo": "Atlético de Madrid", "Pie": "Derecha", "Posicion": "DEL",
         "Edad": "29", "Nacionalidad": "Argentina", "Dorsal": "10"},
        {"Nombre": "Thomas Lemar", "Equipo": "Atlético de Madrid", "Pie": "Izquierda", "Posicion": "MED",
         "Edad": "28", "Nacionalidad": "Francia", "Dorsal": "11"},
        {"Nombre": "Samuel Lino", "Equipo": "Atlético de Madrid", "Pie": "Derecha", "Posicion": "DEL", "Edad": "24",
         "Nacionalidad": "Brasil", "Dorsal": "12"},
        {"Nombre": "Marcos Llorente", "Equipo": "Atlético de Madrid", "Pie": "Derecha", "Posicion": "MED",
         "Edad": "29", "Nacionalidad": "España", "Dorsal": "14"},
        {"Nombre": "Clément Lenglet", "Equipo": "Atlético de Madrid", "Pie": "Izquierda", "Posicion": "DEF",
         "Edad": "29", "Nacionalidad": "Francia", "Dorsal": "15"},
        {"Nombre": "Nahuel Molina", "Equipo": "Atlético de Madrid", "Pie": "Derecha", "Posicion": "DEF",
         "Edad": "26", "Nacionalidad": "Argentina", "Dorsal": "16"},
        {"Nombre": "Rodrigo Riquelme", "Equipo": "Atlético de Madrid", "Pie": "Derecha", "Posicion": "DEL",
         "Edad": "24", "Nacionalidad": "España", "Dorsal": "17"},
        {"Nombre": "Axel Witsel", "Equipo": "Atlético de Madrid", "Pie": "Derecha", "Posicion": "MED", "Edad": "35",
         "Nacionalidad": "Bélgica", "Dorsal": "20"},
        {"Nombre": "Javi Galán", "Equipo": "Atlético de Madrid", "Pie": "Izquierda", "Posicion": "DEF",
         "Edad": "29", "Nacionalidad": "España", "Dorsal": "21"},
        {"Nombre": "Reinildo Mandava", "Equipo": "Atlético de Madrid", "Pie": "Izquierda", "Posicion": "DEF",
         "Edad": "30", "Nacionalidad": "Mozambique", "Dorsal": "23"},
        {"Nombre": "Robin Le Normand", "Equipo": "Atlético de Madrid", "Pie": "Derecha", "Posicion": "DEF",
         "Edad": "27", "Nacionalidad": "España", "Dorsal": "24"},
        # Real Madrid
        {"Nombre": "Thibaut Courtois", "Equipo": "Real Madrid", "Pie": "Izquierda", "Posicion": "POR", "Edad": "31",
         "Nacionalidad": "Bélgica", "Dorsal": "1"},
        {"Nombre": "Andriy Lunin", "Equipo": "Real Madrid", "Pie": "Derecha", "Posicion": "POR", "Edad": "24",
         "Nacionalidad": "Ucrania", "Dorsal": "13"},
        {"Nombre": "David Alaba", "Equipo": "Real Madrid", "Pie": "Izquierda", "Posicion": "DEF", "Edad": "31",
         "Nacionalidad": "Austria", "Dorsal": "4"},
        {"Nombre": "Antonio Rüdiger", "Equipo": "Real Madrid", "Pie": "Derecha", "Posicion": "DEF", "Edad": "30",
         "Nacionalidad": "Alemania", "Dorsal": "22"},
        {"Nombre": "Nacho Fernández", "Equipo": "Real Madrid", "Pie": "Derecha", "Posicion": "DEF", "Edad": "34",
         "Nacionalidad": "España", "Dorsal": "6"},
        {"Nombre": "Dani Carvajal", "Equipo": "Real Madrid", "Pie": "Derecha", "Posicion": "DEF", "Edad": "32",
         "Nacionalidad": "España", "Dorsal": "2"},
        {"Nombre": "Ferland Mendy", "Equipo": "Real Madrid", "Pie": "Izquierda", "Posicion": "DEF", "Edad": "28",
         "Nacionalidad": "Francia", "Dorsal": "23"},
        {"Nombre": "Fran García", "Equipo": "Real Madrid", "Pie": "Izquierda", "Posicion": "DEF", "Edad": "24",
         "Nacionalidad": "España", "Dorsal": "20"},
        {"Nombre": "Toni Kroos", "Equipo": "Real Madrid", "Pie": "Derecha", "Posicion": "MED", "Edad": "34",
         "Nacionalidad": "Alemania", "Dorsal": "8"},
        {"Nombre": "Luka Modrić", "Equipo": "Real Madrid", "Pie": "Derecha", "Posicion": "MED", "Edad": "38",
         "Nacionalidad": "Croacia", "Dorsal": "10"},
        {"Nombre": "Eduardo Camavinga", "Equipo": "Real Madrid", "Pie": "Izquierda", "Posicion": "MED", "Edad": "21",
         "Nacionalidad": "Francia", "Dorsal": "12"},
        {"Nombre": "Aurélien Tchouaméni", "Equipo": "Real Madrid", "Pie": "Derecha", "Posicion": "MED", "Edad": "24",
         "Nacionalidad": "Francia", "Dorsal": "18"},
        {"Nombre": "Federico Valverde", "Equipo": "Real Madrid", "Pie": "Derecha", "Posicion": "MED", "Edad": "25",
         "Nacionalidad": "Uruguay", "Dorsal": "15"},
        {"Nombre": "Brahim Díaz", "Equipo": "Real Madrid", "Pie": "Izquierda", "Posicion": "MED", "Edad": "24",
         "Nacionalidad": "España", "Dorsal": "21"},
        {"Nombre": "Jude Bellingham", "Equipo": "Real Madrid", "Pie": "Derecha", "Posicion": "MED", "Edad": "21",
         "Nacionalidad": "Inglaterra", "Dorsal": "5"},
        {"Nombre": "Rodrygo", "Equipo": "Real Madrid", "Pie": "Derecha", "Posicion": "DEL", "Edad": "23",
         "Nacionalidad": "Brasil", "Dorsal": "11"},
        {"Nombre": "Vinícius Júnior", "Equipo": "Real Madrid", "Pie": "Derecha", "Posicion": "DEL", "Edad": "24",
         "Nacionalidad": "Brasil", "Dorsal": "7"},
        {"Nombre": "Joselu", "Equipo": "Real Madrid", "Pie": "Derecha", "Posicion": "DEL", "Edad": "34",
         "Nacionalidad": "España", "Dorsal": "9"},
        {"Nombre": "Arda Güler", "Equipo": "Real Madrid", "Pie": "Izquierda", "Posicion": "MED", "Edad": "19",
         "Nacionalidad": "Turquía", "Dorsal": "24"},
        {"Nombre": "Fran González", "Equipo": "Real Madrid", "Pie": "Derecha", "Posicion": "DEF", "Edad": "19",
         "Nacionalidad": "España", "Dorsal": "30"},
        {"Nombre": "Lucas Cañizares", "Equipo": "Real Madrid", "Pie": "Derecha", "Posicion": "POR", "Edad": "21",
         "Nacionalidad": "España", "Dorsal": "26"},
        {"Nombre": "Óscar Rodríguez", "Equipo": "Real Madrid", "Pie": "Izquierda", "Posicion": "MED", "Edad": "25",
         "Nacionalidad": "España", "Dorsal": "31"},
        # FC Barcelona
        {"Nombre": "Marc-André ter Stegen", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "POR", "Edad": "32",
         "Nacionalidad": "Alemania", "Dorsal": "1"},
        {"Nombre": "Iñaki Peña", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "POR", "Edad": "24",
         "Nacionalidad": "España", "Dorsal": "13"},
        {"Nombre": "Ronald Araújo", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "DEF", "Edad": "25",
         "Nacionalidad": "Uruguay", "Dorsal": "4"},
        {"Nombre": "Jules Koundé", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "DEF", "Edad": "25",
         "Nacionalidad": "Francia", "Dorsal": "23"},
        {"Nombre": "Andreas Christensen", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "DEF", "Edad": "28",
         "Nacionalidad": "Dinamarca", "Dorsal": "15"},
        {"Nombre": "Alejandro Balde", "Equipo": "FC Barcelona", "Pie": "Izquierda", "Posicion": "DEF", "Edad": "20",
         "Nacionalidad": "España", "Dorsal": "28"},
        {"Nombre": "Marcos Alonso", "Equipo": "FC Barcelona", "Pie": "Izquierda", "Posicion": "DEF", "Edad": "33",
         "Nacionalidad": "España", "Dorsal": "17"},
        {"Nombre": "Íñigo Martínez", "Equipo": "FC Barcelona", "Pie": "Izquierda", "Posicion": "DEF", "Edad": "32",
         "Nacionalidad": "España", "Dorsal": "5"},
        {"Nombre": "Sergi Roberto", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "MED", "Edad": "31",
         "Nacionalidad": "España", "Dorsal": "20"},
        {"Nombre": "Oriol Romeu", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "MED", "Edad": "32",
         "Nacionalidad": "España", "Dorsal": "18"},
        {"Nombre": "Frenkie de Jong", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "MED", "Edad": "27",
         "Nacionalidad": "Países Bajos", "Dorsal": "21"},
        {"Nombre": "Ilkay Gündogan", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "MED", "Edad": "33",
         "Nacionalidad": "Alemania", "Dorsal": "22"},
        {"Nombre": "Pedri", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "MED", "Edad": "21",
         "Nacionalidad": "España", "Dorsal": "8"},
        {"Nombre": "Gavi", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "MED", "Edad": "19",
         "Nacionalidad": "España", "Dorsal": "6"},
        {"Nombre": "Fermín López", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "MED", "Edad": "20",
         "Nacionalidad": "España", "Dorsal": "32"},
        {"Nombre": "Raphinha", "Equipo": "FC Barcelona", "Pie": "Izquierda", "Posicion": "DEL", "Edad": "27",
         "Nacionalidad": "Brasil", "Dorsal": "11"},
        {"Nombre": "Lamine Yamal", "Equipo": "FC Barcelona", "Pie": "Izquierda", "Posicion": "DEL", "Edad": "16",
         "Nacionalidad": "España", "Dorsal": "27"},
        {"Nombre": "João Félix", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "DEL", "Edad": "24",
         "Nacionalidad": "Portugal", "Dorsal": "14"},
        {"Nombre": "Robert Lewandowski", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "DEL", "Edad": "35",
         "Nacionalidad": "Polonia", "Dorsal": "9"},
        {"Nombre": "Ferran Torres", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "DEL", "Edad": "23",
         "Nacionalidad": "España", "Dorsal": "7"},
        {"Nombre": "Abde Ezzalzouli", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "DEL", "Edad": "22",
         "Nacionalidad": "Marruecos", "Dorsal": "19"},
        {"Nombre": "Ronald Araujo", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "DEF", "Edad": "24",
         "Nacionalidad": "Uruguay", "Dorsal": "4"},
        {"Nombre": "João Cancelo", "Equipo": "FC Barcelona", "Pie": "Derecha", "Posicion": "DEF", "Edad": "29",
         "Nacionalidad": "Portugal", "Dorsal": "2"}
    ]
    return jsonify(jugadores)

# Consumo de API
def creacion_api():
    url = "http://127.0.0.1:5000/goldle/jugadores"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la petición: {e}")
        return []


# Iniciar el servidor
if __name__ == '__main__':
    app.run(port=5000)
