# Archivo helpers.py

# FUNCTIONS ------------------------------------------------------
def normalizar_texto(texto):
    return texto.strip().lower()

def cargar_conocimiento(ruta):
    conocimiento = {}
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                if "=>" in linea:
                    pregunta, respuesta = linea.split("=>")
                    conocimiento[pregunta.strip()] = respuesta.strip()
    except FileNotFoundError:
        print(f"Archivo {ruta} no encontrado.")
    return conocimiento
