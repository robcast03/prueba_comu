<?php
// Recibir datos del servidor Flask
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Recibir datos JSON
    $json_data = file_get_contents('php://input');
    $data = json_decode($json_data);

    // Verificar si la decodificación fue exitosa
    if ($data !== null) {
        // Obtener el número enviado desde el servidor Flask
        $numero = $data->numero;

        // Hacer algo con el número (almacenarlo en una variable, por ejemplo)
        $almacenar_numero = $numero;

        // Puedes imprimir el número para verificar
        echo "Número recibido en PHP: " . $almacenar_numero;
    } else {
        // Manejar el caso en el que la decodificación JSON falla
        echo "Error al decodificar los datos JSON";
    }
} else {
    // Manejar el caso en el que la solicitud no es de tipo POST
    echo "Solo se permiten solicitudes POST";
}
?>

