# contacto.py --> define las clases y métodos que vamos a utilizar en la agenda

# CLASS -----------------------------------------------
class Contacto:

    # 1.- Método constructor
    def __init__(self, nombre:str, telefono:str, email:str = ""):
    # nombre y telefono son str obligatoriamente. Además, email es str y siempre tiene vacío si no se mete información
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    # 2.- Métodos (funciones) de la clase Contacto
    
    # Método mágico: dunder method - double underscore
    # Define cómo se muestra un objeto como texto
    def __str__(self):
        return f"{self.nombre} | Tlf: {self.telefono} | Email: {self.email or 'N/A'}"