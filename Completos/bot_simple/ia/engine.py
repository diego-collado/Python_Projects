# Archivo engine.py

# IMPORTS --------------------------------------------------------
import json
import os
from utils.helpers import cargar_conocimiento, normalizar_texto

# GLOBAL VARS ----------------------------------------------------
MEMORIA_PATH = "memoria.json"
CONOCIMIENTO_PATH = "conocimiento.txt"

# CLASS ----------------------------------------------------------
class SimpleBot:
    def __init__(self):
        self.memoria = self.cargar_memoria()
        self.conocimiento = cargar_conocimiento(CONOCIMIENTO_PATH)

    def cargar_memoria(self):
        if os.path.exists(MEMORIA_PATH):
            with open(MEMORIA_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def guardar_memoria(self):
        with open(MEMORIA_PATH, "w", encoding="utf-8") as f:
            json.dump(self.memoria, f, ensure_ascii=False, indent=2)

    def responder(self, entrada):
        entrada_norm = normalizar_texto(entrada)

        if entrada_norm in self.memoria:
            return self.memoria[entrada_norm]

        for pregunta, respuesta in self.conocimiento.items():
            if entrada_norm == normalizar_texto(pregunta):
                self.memoria[entrada_norm] = respuesta
                self.guardar_memoria()
                return respuesta

        respuesta = input("No sé cómo responder eso. ¿Qué debería decir? → ").strip()
        if respuesta:
            self.memoria[entrada_norm] = respuesta
            self.guardar_memoria()
            return "¡Gracias! He aprendido algo nuevo."
        return "Ok, lo dejo sin aprender esta vez."
