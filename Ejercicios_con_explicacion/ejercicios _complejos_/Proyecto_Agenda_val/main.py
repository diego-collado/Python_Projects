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
from models.contacto import Contacto # Importamos la clase contacto desde la carpeta Models
from services.agenda import Agenda # Importamos la agenda desde la carpeta Services
from utils.validaciones import validar_nombre, validar_telefono, validar_email

# Importa la clase Contacto que está definida en el módulo contacto.py, 
# dentro del paquete (carpeta) Models

def mostrar_menu():
    print("======= AGENDA DE CONTACTOS =======")
    print("1.- Agregar contacto")
    print("2.- Buscar contacto")
    print("3.- Eliminar contacto")
    print("4.- Listar contactos")
    print("5.- Salir")
    print("======= ======= =======")

def main():

    # Inicialización
    agenda= Agenda() # llamamos al método constructor de agendas

    while True:
        mostrar_menu()
        opcion = input("Selecciona la opción que desees (1-5): ").strip()

        if opcion == "1":
            while True:
                nombre = input("Introduce nombre: ").strip()
                if validar_nombre(nombre):
                    break
                print("El nombre no me lo puedes dejar vacío...")
        
            while True:
                telefono = input("Introduce telefono: ").strip()
                if validar_telefono(telefono):
                    break
                print("Teléfono inválido... Introduce solo dígitos, mínimo 7 números")
            
            while True:
                email = input("Introduce email: ").strip()
                if validar_email(email):
                    break
                print("Formato de email incorrecto...")

            # "Grabamos los contactos", es decir, los agregamos
            contacto = Contacto(nombre, telefono, email) # se guarda todo en una variable
            agenda.agregar_contacto(contacto)# se envía la variable al agregador

        elif opcion == "2":
            nombre = input("Introduce nombre a buscar: ")
            agenda.buscar_contacto(nombre)

        elif opcion == "3":
            nombre = input("Introduce nombre del contacto a eliminar: ")
            agenda.eliminar_contacto(nombre)
        
        elif opcion == "4":
            agenda.listar_contactos()
        
        elif opcion == "5":
            print("Saliendo de la agenda... ¡¡Hasta luego!!")
            break
        
        else:
            print("¡¡Error, opción inválidad, intentaló de nuevo\n\n")
    
# MAIN -----------------------------------------------
if __name__ == "__main__":
    main()