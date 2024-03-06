#import requests

#url = 'http://172.17.38.44/enviar_numero'
#data = {'numero': 42}

#response = requests.post(url, json=data)
#print(response.text)

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar_numero', methods=['POST'])
def enviar_numero():
    numero = request.json.get('numero')
    # Aquí puedes agregar el código para enviar el número a través de WiFi
    # Por ejemplo, podrías usar sockets para enviar el número a otro dispositivo en la red
    print("Número recibido:", numero)
    return 'Número recibido: {}'.format(numero)

if __name__ == '__main__':
    app.run(host='192.168.0.100', port=80)
