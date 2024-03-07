from flask import Flask, request

app = Flask(__name__)

@app.route('/enviar_numero', methods=['POST'])
def enviar_numero():
    numero = request.json.get('numero')
    # Aquí puedes agregar el código para enviar el número a través de WiFi
    # Por ejemplo, podrías usar sockets para enviar el número a otro dispositivo en la red
    print("Número recibido:", numero)
    return 'Número recibido: {}'.format(numero)

if __name__ == '__main__':
    app.run(host='192.168.0.163', port=80)  # Ejecutar la aplicación en todas las interfaces en el puerto 80

