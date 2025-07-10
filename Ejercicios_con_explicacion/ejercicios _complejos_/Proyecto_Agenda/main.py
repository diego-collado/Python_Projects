# main.py --> archivo de entrada a la Agenda
'''
# 1.- Creamos una clase vacía, es decir, una plantilla
class Perro: #con mayúscula, para identificar que es una clase
    especie = "Mamíferos" # Atributo de clase, es decir, todos los Perros son Mamíferos

    # OBLIGATORIO # OBLIGATORIO # OBLIGATORIO # OBLIGATORIO # OBLIGATORIO #
    # Método constructor: crea los atributos de instancia: son propios de cada objeto
    def __init__(self, nombre, raza): #dentro de self se guarda todo, es decir, es como una carta comodín
        self.nombre = nombre # atributo de instancia, el nombre se guarda en self.nombre
        self.raza = raza # atributo de instancia, la raza se guarda en self.raza

    # YA NO TAN OBLIGATORIO: MÉTODOS (funciones que puedo tener para la clase)
    def ladrar(self):
        print("Guaaaauuuuuuuuuuuuuuuuu")
    
    def caminar(self,pasos):
        print (f"Mi {self.nombre} ha caminado {pasos} pasos")

# -------------------------------------------------------------------------------------- #

# 2.- Creamos un objeto de la clase Perro: coco = Perro() 
mi_perro = Perro("Coco","Caniche") # envío la información para construir cada objeto
mi_perro2 = Perro("Bala", "Labrador")
mi_perro3 = Perro("Chopi","Border Collie")

# 3.- Veamos resultados
print(type(mi_perro))
print(type(mi_perro2))
print(type(mi_perro3))

# 4.- Veamos resultados un poco mejor
print(mi_perro.especie)
print(mi_perro.raza)

# 5.- Ahora, las acciones
mi_perro.ladrar() # llamamos a la función en cuestión
mi_perro.caminar(15000)
# especifico el objeto, con self ya sabe que se llama X y que lo único que hay que pedir son los pasos
'''

# IMPORTS -----------------------------------------------
def main():
    from models.contacto import Contacto # Importamos la clase contacto desde la carpeta Models
    from services.agenda import Agenda # Importamos la agenda desde la carpeta Services

    # Importa la clase Contacto que está definida en el módulo contacto.py, 
    # dentro del paquete (carpeta) Models

    # Inicialización
    agenda= Agenda() # llamamos al método constructor de agendas

    contacto1 = Contacto("Diego Collado","645154916","tresw.es@gmail.com")
    contacto2 = Contacto("Marta Gª","645645645","")

    # Agregamos los contactos a la Agenda
    agenda.agregar_contacto(contacto1)
    agenda.agregar_contacto(contacto2)

    # Hacemos el resto de las funcionalidades
    agenda.listar_contactos()
    agenda.buscar_contacto("Diego Collado")
    agenda.eliminar_contacto("Marta Gª")
    agenda.listar_contactos()

# MAIN -----------------------------------------------
if __name__ == "__main__":
    '''globals().update({
        'Contacto': Contacto, #from models.contacto import Contacto
        'Agenda': Agenda #from services.agenda import Agenda 
    })

    # Esto que se ha codificado es lo mismo que from models.contacto import...'''
    main()