function agregarFila() {
    /*Document.getElementById().onClick = AgregarFila();
        Con esto, se puede llamar a la funcion del script al presionar un boton
            El cual liberara un evento onClick, que ejecutara la funcion
            No es ocupada ahora, pero se puede uusar mas adelante y/o probarla con esta misma funcion en index.html
    */
    var nombre = document.getElementById("nombre").value; //Obtiene elemento del formulario con el name "nombre"
    //Probando Cambio de color al campo de nombre
    //var nfont = document.getElementById("nombre");
    //nfont.style.color = "blue";
    console.log(nombre);
    
    var apellido = document.getElementById("apellido").value; //Obtiene elemento del formulario con el name "apellido"
    console.log(apellido);
    //apellido.style.color = "blue";
    alert(nombre+" "+apellido); //EVENTO DE ALERTA, NO ES NECESARIO, SOLO PARA PROBAR QUE FUNCIONA
    var tablaCuerpo = document.getElementById("tablaCuerpo"); //Obtiene el elemento del DOM con el id "tablaCuerpo"
    var nuevaFila = tablaCuerpo.insertRow(tablaCuerpo.rows.length);

    var celdaId = nuevaFila.insertCell(0); // Index 0 de la tabla donde ira el ID
    var celdaNombre = nuevaFila.insertCell(1); // Index 1 de la tabla donde ira el nombre
    var celdaApellido = nuevaFila.insertCell(2); // Index 2 de la tabla donde ira el apellido

    // En una aplicación real, podrías asignar un valor único para cada nueva fila
    var nuevoId = tablaCuerpo.rows.length;
    
    celdaId.innerHTML = nuevoId; //estableciendo el contenido HTML; El "id" de la nueva fila se incrementará en función del número total de filas en la tabla
    celdaNombre.innerHTML = nombre; //Agrega el nombre a la nueva celda
    celdaApellido.innerHTML = apellido; //Agrega el apellido a la nueva celda

    // Vacio los campos del formulario
    document.getElementById("nombre").value = "";
    document.getElementById("apellido").value = "";
    
    //Probando elementos DOM
    alert(document.body.firstElementChild.nodeName);
    document.body.style.backgroundImage = "url('fondo.png')";
}