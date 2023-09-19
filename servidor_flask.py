from flask import Flask, request, jsonify

app = Flask(__name__)

carros_file = "carros.txt"

# Ruta para agregar un carro
@app.route('/carros', methods=["POST"])
def agregar_carro():
    data = request.get_json()
    if data:
        carro_info = f"{data['marca']}, {data['color']}, {data['estado']}\n"
        with open(carros_file, 'a+') as archivo:
            archivo.write(carro_info)
        return 'El carro fue agregado'
    else:
        return 'Datos incorrectos', 400

# Ruta para obtener todos los carros guardados
@app.route('/carros', methods=["GET"])
def obtener_carros():
    carros = []
    try:
        with open(carros_file, 'r') as archivo:
            for linea in archivo:
                carro_info = linea.strip()
                marca, color, estado = carro_info.split(", ")
                carros.append({
                    "marca": marca,
                    "color": color,
                    "estado": estado
                })
        return jsonify(carros)
    except FileNotFoundError:
        return 'No hay carros guardados', 404

if __name__ == '__main__':
    app.run(debug=True)

