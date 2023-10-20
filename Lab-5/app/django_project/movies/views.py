from django.shortcuts import render
from .services import generate_request

def index(request):
    return render(request, 'index.html',{'generos':generate_request()}) #Se manda a establecer la conexion con la pagina,
                                                                        #si esta retorna un codigo 200 (OK), significa que se establecio
                                                                        #la conexion correctamente, luego mandamos los generos
                                                                        #como parametro a index.html