from django.shortcuts import render
from .models import Course, Student
import requests


def index(request):
    api_key = 'dc5bb44da67289061c5f0125728a5626'
    url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Procesa los datos de la respuesta según tus necesidades
        return render(request, 'index.html', {'movies': data['results']})
    

def error_page(request):
    # Puedes personalizar el mensaje de error aquí si lo deseas
    error_message = "Ocurrió un error."

    return render(request, 'error.html', {'error_message': error_message})
