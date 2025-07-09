# Archivo weather.py

# IMPORTS ------------------------------------------------------
import requests
from .config import API_KEY, BASE_URL

# FUNCTIONS ----------------------------------------------------
def get_weather(city):
    """
    Consulta la API de OpenWeatherMap para obtener datos meteorológicos.
    Argumentos (args):
        city (str): Nombre de la ciudad.
    Retorno:
        dict: Datos del clima o mensaje de error.
    """
    if not API_KEY:
        return {"error": "API_KEY no configurada."}

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        return {
            "ciudad": data["name"],
            "temperatura": data["main"]["temp"],
            "sensacion": data["main"]["feels_like"],
            "clima": data["weather"][0]["description"],
            "humedad": data["main"]["humidity"],
            "viento": data["wind"]["speed"]
        }

    except requests.exceptions.HTTPError:
        return {"error": f"Ciudad '{city}' no encontrada."}
    except requests.exceptions.RequestException:
        return {"error": "Error de conexión con la API."}