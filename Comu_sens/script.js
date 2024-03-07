// script.js
function activarServidor() {
    // Realizar la solicitud POST al servidor Flask cuando se hace clic en el botón
    var xhr = new XMLHttpRequest();
    var url = 'http://192.168.0.7/enviar_numero';
    var data = {'numero': 42};

    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if (xhr.status == 200) {
                console.log('Conectado');
            } else {
                console.log('Error al conectar al servidor');
            }
        }
    };

    xhr.send(JSON.stringify(data));
}

