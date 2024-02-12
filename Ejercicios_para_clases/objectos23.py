'''
ARCHIVO DE PROCESAMIENTO DE OBJETOS------------------------------------------------------

Crear una clase que administre una agenda personal. Se debe almacenar el nombre, teléfono y mail
Debe mostrar un menú con las siguientes opciones:
    1.- Carga de un contacto en la agenda.
    2.- Listado completo de la agenda.
    3.- Consulta ingresando el nombre de la persona.
    4.- Modificación de su teléfono y mail.
    5.- Finalizar programa.
'''
# CLASS
class Agenda:
    # 1.- Utilizamos el constructor para crear el objeto en cuestión
    def __init__(self):
        self.contactos = {}  # 2.- definir el tipo de dato que necesitamos, es decir, lo que se va a utilizar

    '''
    ¿Porqué un diccionario?
        Fácil, el diccionario es un dato que nos permite controlar lo que tenemos por una clave.
        Ejemplo: ¿Cómo accedo a vuestros datos de Seguridad Social? con el DNI/NIE

        Diccionario = {clave: valor, clave: valor}
    '''

    # 3.- definimos el menú en cuestión, que en este caso, es un método de Agenda
    def menu(self):
        opcion = 0

        while opcion != 5:
            print("1. Carga de contacto en la agenda")
            print("2. Listar contactos (agenda completa)")
            print("3. Consultar datos por nombre")
            print("4. Modificar datos de un contacto")
            print("5. Finalizar este maravilloso Pograma")

            opcion = int(input("Introduce tu elección: "))

            if (opcion == 1):
                self.cargar()  # 4.- llamamos a los métodos que necesitemos
            elif (opcion == 2):
                self.listar()
            elif (opcion == 3):
                self.consultar()
            elif (opcion == 4):
                self.modificar()
            elif (opcion == 5):
                print("Bye, Bye, BaBy!!")
                break;
            else:
                print("¡¡eRRoR, eSTa oPCióN No eXiSTe!!")

    # 5.- codificamos los métodos (funciones) que vamos a utilizar en el menú
    def cargar(self):
        nombre = input("Introduce el nombre de la persona: ")
        telefono = input("Introduce el teléfono de la persona: ")
        mail = input("Introduce el email de la persona: ")

        # 6.- ¿Cómo escribimos los datos en diccionario? self.diccionario[clave]=(valor1, valor2)
        self.contactos[nombre] = (telefono, mail)
        print("_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_")

    def listar(self):
        print("Listado Completo de mi Agenda Hackerística:\n")
        # "dame todos los nombres (claves) que estén en mi Agenda (diccionario)
        for nombre in self.contactos:
            print(f"Contacto: {nombre}\n Tlf: {self.contactos[nombre][0]}\n "
                  f"email: {self.contactos[nombre][1]}")
            print("-----------------------------------------")
        print("_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_")

    def consultar(self):
        nombre = input("Introduce el nombre de la persona a consultar: ")

        # buscamos el contacto en el diccionario
        if nombre in self.contactos:
            print(f"Contacto encontrado: {nombre}\n Tlf: {self.contactos[nombre][0]}\n "
                  f"email: {self.contactos[nombre][1]}")
        else:
            print("Lo sentimos, el contacto en cuestión está apagado y fuera de nuestra cobertura")
        print("_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_")

    def modificar(self):
        nombre = input("Introduce el nombre de la persona a modificar: ")

        if nombre in self.contactos:
            telefono = input("Introduce de nuevo el teléfono de la persona: ")
            mail = input("Introduce de nuevo el email de la persona: ")

            self.contactos[nombre] = (telefono, mail)
        else:
            print("Lo sentimos, el contacto en cuestión está apagado y fuera de nuestra cobertura")

        print("_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_")