'''
Chatbot con memoria local: 
    · Si el bot no sabe responder, puedes preguntarle y enseñarle
    · Guardaría la pregunta/respuesta en un archivo determinado (memoria.json) para recordar todo
    · En cada uso, seguirá recordando todo lo que se le ha preguntado anteriormente

Estructura del JSON:
{
    "hola":"¡Hola! ¿Cómo estás?,
    "quién eres":"Soy tu bot favorito, aprendo de tí"
}    
'''
# IMPORTS ----------------------------------------------------------------
import json # https://docs.python.org/es/3/library/json.html
import os # https://docs.python.org/es/3.13/library/os.html

# VARIABLES/ARCHIVOS GLOBALES --------------------------------------------
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

def obtener_respuesta(pregunta):
    # 1º: evitamos problemas, todo a minúsculas
    pregunta = pregunta.lower()

    # 2º: comprobamos si está o no la pregunta en la memoria
    if pregunta in memoria:
        return memoria[pregunta] # nos retornaría la pregunta guardada

    else:
        print("No tengo respuesta para esto... ¿Qué debería responder?")
        respuesta = input("Dime la respuesta: ")
        
        memoria[pregunta] = respuesta # añadimos esta contestación a nuestro archivo
        guardar_memoria() # guardado real en el archivo

        return respuesta

print("Bot con memoria, escribe 'salir' para terminar...")

# MAIN -------------------------------------------------------------------
while True:
    entrada = input("Humano: ").strip().lower()

    if entrada in ["salir","adios","chao"]:
        print("¡¡Hasta luego, noruego!!")
        break

    # hablando con el bot como tal
    respuesta = obtener_respuesta(entrada)
    print ("Bot: ", respuesta)