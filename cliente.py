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
    numero = request.form['numero']
    data = {'numero': numero}
    
    # Cambia la dirección IP y el puerto según tu configuración del servidor
    url = 'http://192.168.0.100:80/enviar_numero'  
    
    response = requests.post(url, json=data)
    return 'Número enviado: {}'.format(numero)

if __name__ == '__main__':
    app.run(debug=True)

