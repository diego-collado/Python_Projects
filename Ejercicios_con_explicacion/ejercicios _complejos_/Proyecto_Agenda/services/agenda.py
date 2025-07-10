# agenda.py --> define la lógica de la agenda

# CLASS -----------------------------------------------
class Agenda:

    # 1.- Método constructor
    def __init__(self):
        self.contactos = [] # Se crea la agenda como tal, tipo lista
    
    # 2.- Métodos de la clase Agenda
    def agregar_contacto(self, contacto):
        self.contactos.append(contacto) # añadimos el contacto con append a la lista de contactos
        print(f"Contacto '{contacto.nombre}' agregado")

    def eliminar_contacto(self, nombre):
        for contact in self.contactos:
            # si encuentra el contacto, borramos el nombre que corresponda
            if (contact.nombre.lower() == nombre.lower()):
                self.contactos.remove(contact) #borramos el contacto que hemos encontrado
                print(f"Contacto '{nombre}' borrado de la agenda")
                return
        print(f"Contacto '{nombre}' no encontrado...")
    
    def buscar_contacto(self, nombre):
        encontrados = [contact for contact in self.contactos if nombre.lower() in contact.nombre.lower()]
        '''
        la anterior versión es lo mismo que esta, pero más corta:
        
        for contact in self.contactos:
            if (contact.nombre.lower() == nombre.lower()):
        Todo esto, devuelve True si está y False si no está
        Encontrados, realmente, es un lista de elementos
        '''
        if encontrados:
            print("Contactos encontrados")
            for enc in encontrados:
                print(f"- {enc}")
        
        else:
            print (f"No existen contactos con el nombre {nombre}, lo sentimos")

    def listar_contactos(self):
        if not self.contactos:# si no hay de "donde tirar"...
            print(f"La agenda está completamente vacía")
        else:
            print(f"\n-- Lista de Contactos --\n\n")
            for contact in self.contactos:
                print(f"- {contact}")