// Configurar la solicitud
$.ajax({
    url: 'http://localhost:8080/',
    method: 'GET',
    dataType: 'json'
  })
    .done(function(data) {
      // Procesar los datos
      console.log(data);
    })
    .fail(function(jqXHR, textStatus, errorThrown) {
      // Manejar el error
      console.error('La solicitud falló: ' + textStatus + ', ' + errorThrown);
    });
  