#IMPORTS
import requests
import json

# URL de la API
api_url = "http://ip-api.com/json/"

# Definimos los parámetros de respuesta que queremos obtener
parametros = 'status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
data = {"fields": parametros}


def ip_scraping(ip=""):
    # conexión con la API
    res = requests.get(api_url + ip, data=data)
    # Obtención y proceso de la respuesta JSON
    api_json_res = json.loads(res.content)
    return api_json_res


if __name__ == '__main__':
    # Solicitar la entrada de la URL/IP
    ip = input("Introduce dirección IP: ")

    # se llama a la función ip_scraping y se muestran los resultados
    par = parametros.split(",")
    for x in par:
        print(x.upper(), ":")
        print(ip_scraping(ip)[x])
        print("n")