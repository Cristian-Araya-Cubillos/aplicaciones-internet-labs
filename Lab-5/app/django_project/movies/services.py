import requests

def generate_request():
    url = "http://api.filmon.com/api/vod/genres"
    
    #response = requests.get(url, headers=headers, params=querystring)
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['response'] #Si el estatus marca 200(correcto) retorna un json con la respuesta