'''
Chatbot con memoria local y que use ChatGPT cuando no sepa la respuesta: 
    · Buscará primero en el archivo local (memoria.json)
    · Si no sabe, utilizaremos una API de OpenAI (ChatGPT), es decir, un "puente" de comunicaciones
    para poder "trastear" con aplicaciones que no son nuestras y que están online
    · Guarde la respuesta de ChatGPT para futuras consultas que hagamos

¿Se necesita algo más?
pip install openai
'''
# IMPORTS ----------------------------------------------------------------
import json # https://docs.python.org/es/3/library/json.html
import os # https://docs.python.org/es/3.13/library/os.html
import openai 
# https://github.com/openai/openai-python
# https://platform.openai.com/docs/api-reference/introduction

# VARIABLES/ARCHIVOS GLOBALES --------------------------------------------
openai.api_key = os.getenv("")
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
        # damosla info a ChatGPT para comenzar
        respuesta = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", # seleccionamos el modelo con el se va a trabajar
            messages =[ # se parametriza el rol de ChatGPT y le lanzamos la pregunta
                {"role":"system", "content":"Eres un asistente útil y directo."},
                {"role":"user","content":pregunta}
            ],
            temperature = 0.5)
        '''
            · roles que puede asumir desde aquí: 
                - system
                - user
                - assistant
            · temperature: aletoriedad con la que se contesta, es decir, cómo de aleatoria es la 
            generación de texto

            0.0: muy predecible y directo, siempre da la misma respuesta. Utilizado en tareas técnicas
            0.5: equilibrado, algo creativo, pero consistente
            0.7: típico (por defecto), creativo pero con lógica y respuestas variadas... ¡¡Razonables!!
            1.0: muy aleatorio y expresivo, menos predecible
            > 1.0: caótico, totalmente aleatorio, incoherente... Muy útil para ficción y similares
        '''
        # extraemos el texto de la respuesta de ChatGPT, quitando blancos de principio y final
        contenido = respuesta.choices[0].message.content.strip()
        # respuesta.choices: lista de posibles respuestas
        # [0]: se toma la primera, la más probable
        # message: mensaje generado por el modelo 
        # content: se obtiene solo el texto del mensaje (sin más metadata)
        return contenido
    
    except Exception as e:
        return f"Error al conectar con ChatGPT: {e}"

def responder(pregunta):
    # 1.- primero investigamos en el archivo local
    respuesta = obtener_respuesta_local(pregunta)
    # 2.- dependiendo de si está o no, nos vamos a ChatGPT
    if respuesta:
        return respuesta
    else: # aquí es cuando vamos a "la Interné" a preguntar a ChatGPT
        respuesta = obtener_respuesta_gpt(pregunta)

        if not "Error" in respuesta:
            memoria[pregunta.lower()] = respuesta # grabamos lo que nos dice ChatGPT en el archivo
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