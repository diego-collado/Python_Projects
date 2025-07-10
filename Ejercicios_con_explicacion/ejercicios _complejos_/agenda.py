'''
Crear una agenda gestionada mediante un CRUD, lo que nos posibilita:
    - Create - Read - Update - Delete

¿Qué es lo que necesito?
1.- Creación de un menú de opciones:
    · opción agregar    · opción borrar todo    · opción borrar posición
    · opción editar     · opción mostrar todo   · opción mostrar posición

2.- ¿Dónde guardamos los datos? Ni más ni menos que en una LISTA.
    agenda [contacto1[nombre, teléfono], contacto2[nombre, teléfono]...]
'''

# creación e inicialización de variables ----------------------------
agenda = [] # lista donde se guardará la agenda
salir = False # condición para poder salir del programa

while not salir:
    # Mientras que salir no tenga valor TRUE... Sigo repitiendo
    print("MENÚ DE OPCIONES\n\n")
    print("1.- Agregar contacto")
    print("2.- Mostrar contacto")
    print("3.- Buscar contacto")
    print("4.- Eliminar contacto")
    print("5.- Salir")

    opcion = input("Selecciona una opción:  ")

    # Agregar contacto a la agenda
    if (opcion == "1"):
        nombre = input("Introduce nombre: ")
        telefono = input("Introduce teléfono: ")

        agenda.append([nombre, telefono])
        print("Contacto agredado!!")
    
    # Mostrar contacto a la agenda
    elif (opcion == "2"):
        if not agenda:
            print("¡¡Cuidado, la agenda está vacía!!")
        else:
            for i,contacto in enumerate(agenda, 1):
                print(f"{i}. {contacto[0]} {contacto[1]}") 
                # imprimir Nombre y teléfono a la vez
    
    # Buscar contacto a la agenda
    elif (opcion == "3"):
        nombre_buscado = input("Introduce el nombre a buscar: ")
        encontrado = False

        # recorremos "toita" la agenda
        for contacto in agenda:
            # lista.lower() = pon el contenido a minúsculas
            if contacto[0].lower() == nombre_buscado.lower():
                print(f"Encontrado: {contacto[0]} - {contacto[1]}") 
                encontrado = True
            if not encontrado:
                print("Contacto inexistente...")

    elif (opcion == "4"):
        nombre_eliminar = input("Introduce el nombre a eliminar: ")
        nueva_agenda = []
        eliminado = False

        for contacto in agenda:
            if contacto[0].lower() != nombre_eliminar.lower():
                nueva_agenda.append(contacto)
            else:
                eliminado = True
        agenda = nueva_agenda
        
        if eliminado: # eliminado está en TRUE
            print("Contacto eliminado...")
        else:
            print("Contacto a eliminar no encontrado...")

    # Salir de la agenda
    elif (opcion == "5"):
        print("Está ud. saliendo de esta maravillosa agenda...")
        salir = True
    
    # Eliminando posibles fallos y usuarios "malignos"
    else:
        print("Opción no válidad, por favor, deja de hacer el moñas...")