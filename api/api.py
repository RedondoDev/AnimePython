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
         "Edad": "27", "Nacionalidad": "España", "Dorsal": "24"}]
    return jsonify(jugadores)

# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)

# Consumo de API
def hacer_peticion():
    url = "http://127.0.0.1:5000/goldle/jugadores"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la petición: {e}")
        return []