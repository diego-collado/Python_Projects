'''
Chatbot con memoria local y que use Google Gemini cuando no sepa la respuesta: 
    · Buscará primero en el archivo local (memoria.json)
    · Si no sabe, utilizaremos una API de Google Gemini, es decir, un "puente" de comunicaciones
    para poder "trastear" con aplicaciones que no son nuestras y que están online
    · Guarde la respuesta de Google Gemini para futuras consultas que hagamos

Secret API Key: AIzaSyBGdVymQav4pWhu1ILBjEJQbhEUoyqKnIQ

¿Se necesita algo más?
pip install google-genai
'''
# IMPORTS ----------------------------------------------------------------
import json # https://docs.python.org/es/3/library/json.html
import os # https://docs.python.org/es/3.13/library/os.html
import google.generativeai as genai

# VARIABLES/ARCHIVOS GLOBALES --------------------------------------------
genai.configure(api_key = "AIzaSyBGdVymQav4pWhu1ILBjEJQbhEUoyqKnIQ")
MEMORIA_FILE = "memoria.json"

# PRECARGAS --------------------------------------------------------------
# Cargaremos el archivo si existe ··············
if os.path.exists(MEMORIA_FILE):
    with open(MEMORIA_FILE, "r") as file:
        memoria = json.load(file) # cargamos el archivo en cuestión
# creamos el archivo si no existe
else:
    memoria = {} # se crea un archivo completamente vacío

# FUNCTIONS --------------------------------------------------------------
def guardar_memoria():
    # abrimos en modo escritura nuestro archivo
    with open(MEMORIA_FILE, "w") as file: 
        json.dump(memoria, file, indent=2) # grabamos el archivo como tal, indentación de 2 espacios

def obtener_respuesta_local(pregunta):
    pregunta = pregunta.lower() # evitamos problemas, todo a minúsculas
    return memoria.get(pregunta) # retornamos la respuesta que estaba guardada en local

def obtener_respuesta_gpt(pregunta):
    try:
        # damos la info a Google Gemini para comenzar
        model = genai.GenerativeModel("gemini-2.5-pro")
        respuesta = model.generate_content(pregunta)
        contenido = respuesta.text.strip()
        return contenido
    
    except Exception as e:
        return f"Error al conectar con Google Gemini: {e}"

def responder(pregunta):
    # 1.- primero investigamos en el archivo local
    respuesta = obtener_respuesta_local(pregunta)
    # 2.- dependiendo de si está o no, nos vamos a Google Gemini
    if respuesta:
        return respuesta
    else: # aquí es cuando vamos a "la Interné" a preguntar a Google Gemini
        respuesta = obtener_respuesta_gpt(pregunta)
        if not respuesta.startswith("Error"):
            memoria[pregunta] = respuesta # grabamos lo que nos dice Google Gemini en el archivo
            guardar_memoria()
        return respuesta

print("Bot con memoria + GPT (de toda la vida), escribe 'salir' para terminar...\n\n")

# MAIN -------------------------------------------------------------------
while True:
    entrada = input("Humano: ").strip()

    if entrada.lower() in ["salir","adios","chao"]:
        print("¡¡Hasta luego, noruego!!")
        break

    # hablando con el bot como tal
    respuesta = responder(entrada)
    print ("Bot: ", respuesta)