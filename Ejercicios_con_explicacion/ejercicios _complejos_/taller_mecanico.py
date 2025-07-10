'''
Programa que gestiona un taller mecánico.
Funcionalidades que "deberíamos" cumplir:
    - Agregar:
        · clientes
        · vehículos
    - Registrar servicio por vehículo y ver historial de cliente
    - Eliminar vehículo, eliminar cliente y toda su info
    - Buscar vehículo por placa de matrícula
    - Menú 

NOTAS ---------------------------------------------------
pass --> mientras codificas, lo utilizas para construir el esqueleto

ESQUELETO DE UN PROGRAMA
1.- Variables y constantes globales (las conocemos en todo el programa)
2.- Funciones:
    2.1.- se crean 1 única vez, pero se utilizan multitud de veces
    2.2.- podemos crear variables que únicamente se utilizan dentro de la función
3.- Main - programa principal donde se ejecuta absolutamente todo
'''
# GLOBAL VARIABLES --------------------------------------
taller = {
    "clientes":{} # Diccionario de clientes
}

'''
cliente es la clave : {} nuevo es el valor

taller {clave:valor} --> carpeta taller
taller {clave:{clave:valor}} --> carpeta taller, folios de clientes
taller {clientes:{cliente_id:valores_que_tengamos}} --> carpeta talle, folio del cliente "Fulanito de tal", 
tengo toda la información de este cliente

Cada cliente tiene 1 folio con sus cosas, lo que quiere decir que necesitamos
una carpeta para el taller completo
1 folio por cliente: 
    - dentro del folio tengo los datos:
        · dni,nie
        · nombre
        · teléfono
    - vehículos que tiene este cliente
    - otras cosas...

'''
# FUNCTIONS ---------------------------------------------
def menu ():
    while True:
        print("################\n\n#### Taller Mecánico 'Manolito' ####\n\n################")
        print("0.- Editar cliente existente")
        print("1.- Agregar nuevo cliente y vehículo")
        print("2.- Agregar vehículo a cliente ya existente")
        print("3.- Registrar servicio para un vehículo")
        print("4.- Ver historial de servicios de un vehículo")
        print("5.- Ver historial completo de un cliente")
        print("6.- Eliminar vehículo")
        print("7.- Eliminar cliente y todo lo relacionado con él")
        print("8.- Buscar vehículo por placa de matrícula")
        print("9.- Salir")

        opcion = input("\nSelecciona la opción deseada (1-9): ")

        if (opcion == '9'):
            print("Saliendo del sistema...")
            break
        elif (opcion == '0'):
            editar_cliente()
        elif (opcion == '1'):
            agregar_cliente()
        elif (opcion == '2'):
            agregar_vehiculo()
        elif (opcion == '3'):
            registrar_servicio()        
        elif (opcion == '4'):
            ver_historial_vehículo()
        elif (opcion == '5'):
            ver_historial_cliente()
        elif (opcion == '6'):
            eliminar_vehículo()
        elif (opcion == '7'):
            eliminar_cliente()
        elif (opcion == '8'):
            buscar_placa()
        else:
            print("Opción no válida... Intentaló de nuevo...")

def agregar_cliente():
    # 1.- Pedimos los datos que identifican de forma única a mi cliente
    cliente_id = input("Introduce DNI/NIE del cliente: ")

    # 2.- Comprobamos que el cliente no esté dado de alta en mi taller
    if cliente_id in taller["clientes"]:
        print("El cliente ya existe...")
        return # saldría de esta función y se iría al menú
    
    # 3.- Pedimos los datos al cliente, ya que no lo hemos encontrado en el taller
    nombre = input("Introduce el nombre del cliente: ")
    telefono = input("Introduce el teléfono del cliente: ")

    # 4.- Guardamos todos los datos en el taller
    taller["clientes"][cliente_id] = {
        "Nombre":nombre,
        "Teléfono":telefono,
        "Vehículos":{} # al añadir el cliente, se prepara un futuro listado de vehículos
    }
    print("¡¡Cliente agregado correctamente!!")

    # 5.- Ahora, vamos a agregar el vehículo
    agregar_vehiculo(cliente_id) # llamamos a agregar_vehiculo, quien se encargará de tomar los datos del mismo

def agregar_vehiculo(cliente_id=None):
    # Se controla que el vehículo siempre esté asociado a un cliente y que el cliente esté guardado.
    # Si agregamos un vehículo sin pasar por agregar cliente, ¿cómo sabemos a quién pertenece ese vehículo?

    # 1.- Comprobamos que esté el cliente en nuestro taller
    if not cliente_id: # registramos "de nuevo" el cliente... Si no existe, ya sabes, a crear cliente otra vez
        cliente_id = input("Introduce DNI/NIE del cliente: ")
    
    if cliente_id not in taller["clientes"]:
        print("Cliente no encontrado...")
        return
    
    # 2.- Buscamos la matrícula por si acaso el vehículo ya está registrado
    matricula  = input("Introduce la placa de matrícula: ").upper()
    
    # ¿Está mi matrícula asociada a mi ID de cliente?
    '''
    taller --> compruebo ID cliente --> está, compruebo matrícula en el diccionario de vehículos
    '''
    if matricula in taller["clientes"][cliente_id]["vehiculos"]:
        print("Vehículo ya registrado...")
        return
    
    # 3.- Como no existe el vehículo, introducimos los nuevos datos
    marca = input("Introduce marca del vehículo: ")
    modelo = input("Introduce modelo del vehículo: ")
    anio = input("Introduce año del vehículo: ")

    # 4.- Guardamos los datos en nuestro Taller... (diccionario)
    taller["clientes"][cliente_id]["vehiculos"][matricula] = {
        "Marca":marca,
        "Modelo":modelo,
        "Año":anio,
        "servicios":[] # Creamos una nueva lista de servicios para el vehículo
    }
    print ("¡¡Vehículo introducido correctamente!!")


def registrar_servicio():
    # 1.- Comprobar que la matrícula existe
    matricula  = input("Introduce la placa de matrícula: ").upper()

    # 2.- Damos de alta los servicios que se le hacen al vehículo (si existe)
    for cliente_id, cliente in taller["clientes"].items():
        #print("revisando el cliente: ",cliente_id)
        
        if matricula in cliente["vehiculos"]: # si la matrícula existe
            descripcion = input("Introduce servicio a prestar: ")
            precio = float(input("Introduce precio del servicio prestado: "))
            # ¡¡Ahora toca grabar datos!!
            cliente["vehiculos"][matricula]["servicios"].append({
                "Descripcion":descripcion,
                "Precio":precio
            }) # Añadimos descripción y precio para el servicio prestado
            print("¡¡Servicio grabado correctamente!!")
            return
        
    print("Vehículo no encontrado...")

def ver_historial_vehículo():
    # 1.- Comprobar que la matrícula existe
    matricula  = input("Introduce la placa de matrícula: ").upper()

    # 2.- Si tenemos la matrícula, buscamos el vehículo en cuestión
    for cliente in taller["clientes"].values():
        if matricula in cliente["vehiculos"]: # comprobamos que la matrícula está
            vehiculo = cliente["vehiculos"][matricula]
            print(f"\nHistorial de mantenimiento para la matrícula {matricula} - vehículo {vehiculo['Marca']}, {vehiculo['Modelo']}, {vehiculo['Año']}: ")

            # Comprobamos si hay servicios ofrecidos a este vehículo
            if vehiculo["servicios"]: 
                for i, serv in enumerate(vehiculo["servicios"],1): # obligamos a que i empiece en 1
                    print(f"{i}.- {serv['Descripcion']} - {serv['Precio']:.2f}€")
            else:
                print("Vehículo sin servicios registrados...")
            return
    print("¡¡Vehículo no encontrado!!")

def ver_historial_cliente():
    # 1.- Comprobar que el cliente existe
    cliente_id = input("Introduce DNI/NIE del cliente: ")

    # 2.- Si el cliente existe, sacamos el historial
    if cliente_id in taller["clientes"]:
        cliente = taller["clientes"][cliente_id]
        print(f"\nCliente: {cliente['Nombre']} - Teléfono: {cliente['Telefono']} ")

        for matricula, vehiculo in cliente["vehiculos"].items():
            print(f"\nmatrícula {matricula} - vehículo {vehiculo['Marca']}, {vehiculo['Modelo']}")

            # Comprobamos que haya servicios realizados al vehículo
            if vehiculo["servicios"]: 
                for i, serv in enumerate(vehiculo["servicios"],1): # obligamos a que i empiece en 1
                    print(f"{i}.- {serv['Descripcion']} - {serv['Precio']:.2f}€")
            else:
                print("Vehículo sin servicios registrados...")
    else:
        print("¡¡Cliente no encontrado!!")


def eliminar_vehículo():
    # 1.- Comprobar que la matrícula existe
    matricula  = input("Introduce la placa de matrícula: ").upper()

    # 2.- Borramos el vehículo con matrícula dada... ¡¡Solamente ese!!
    for cliente in taller["clientes"].values():
        if matricula in cliente["vehiculos"]:
            del cliente["vehiculos"][matricula] # borramos el vehículo con la matrícula dada
            print("¡¡Vehículo eliminado!!")
            return
        print("¡¡Vehículo no encontrado!!")

def eliminar_cliente():
    # 1.- Comprobar que el cliente existe
    cliente_id = input("Introduce DNI/NIE del cliente: ")

    # 2.- Procedemos a borrar absolutamente todos los datos del cliente en cuestión
    if cliente_id in taller["clientes"]:
        del taller["clientes"][cliente_id] # borramos los datos del cliente con ID la_que_sea
        print("¡¡Cliente y datos completos eliminados!!")
    else:
        print("¡¡Cliente no encontrado!!")

def editar_cliente():
    # 1.- Comprobar que el cliente existe
    cliente_id = input("Introduce DNI/NIE del cliente: ")

    if cliente_id not in taller["clientes"]:
        print("¡¡Cliente no encontrado!!")
        return
    
    cliente = taller["clientes"][cliente_id]
    print(f"Datos actuales cliente: {cliente['Nombre']} - Teléfono: {cliente['Telefono']}")

    nuevo_nombre = input("Introduce el nombre editado (dejar el blanco para NO CAMBIAR): ")
    nuevo_telefono = input("Introduce el teléfono editado (dejar el blanco para NO CAMBIAR): ")

    if nuevo_nombre.strip(): # .strip() quitar los espacios en blanco
        cliente["Nombre"] = nuevo_nombre.strip()
    
    if nuevo_telefono.strip(): # .strip() quitar los espacios en blanco
        cliente["Telefono"] = nuevo_telefono.strip()

    print("Cliente actualizado")

def buscar_placa():
    # 1.- Comprobar que la matrícula existe
    matricula  = input("Introduce la placa de matrícula: ").upper()

    # 2.- Si tenemos la matrícula, buscamos el vehículo en cuestión
    for cliente_id, cliente in taller["clientes"].items():
        if matricula in cliente["vehiculos"]: # comprobamos que la matrícula está
            vehiculo = cliente["vehiculos"][matricula]
            print("# Vehículo encontrado #")
            print(f"Cliente: {cliente['Nombre']} - {cliente['Telefono']}")
            print(f"Matrícula: {matricula}")
            print(f"vehículo {vehiculo['Marca']}, {vehiculo['Modelo']}, {vehiculo['Año']}")
            return            
    
    print("¡¡Vehículo no encontrado!!")

# MAIN --------------------------------------------------
menu()