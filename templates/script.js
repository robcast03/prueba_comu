function enviarNumero() {
    var numero = document.getElementById("numero").value;
    var url = 'http://192.168.0.100 :80/enviar_numero';
    
    // Utiliza la función fetch para enviar la solicitud al servidor
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'numero=' + numero,
    })
    .then(response => response.text())
    .then(data => {
        alert('Número enviado: ' + data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
