#from flask import Flask, request

#app = Flask(__name__)

#@app.route('/enviar_numero', methods=['POST'])
#def enviar_numero():
    #numero = request.json.get('numero')
    # Aquí puedes agregar el código para enviar el número a través de WiFi
    # Por ejemplo, podrías usar sockets para enviar el número a otro dispositivo en la red
    #print("Número recibido:", numero)
    #return 'Número recibido: {}'.format(numero)

#if __name__ == '__main__':
    #app.run(host='172.17.46.84', port=80)  # Ejecutar la aplicación en todas las interfaces en el puerto 80

#from flask import Flask, render_template

#app = Flask(__name__)

#@app.route('/')
#def comu():
    # En este ejemplo, se pasa el número 42 a la plantilla HTML
    #numero = 42
    #return render_template('comu.html', numero=numero)

#if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000, debug=True)

