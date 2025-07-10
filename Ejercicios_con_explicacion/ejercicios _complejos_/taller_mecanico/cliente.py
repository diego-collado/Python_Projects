# cliente.py

# IMPORTS ---------------------------------------------------------------
from datos import taller # Importamos un determinado elemento de un archivo completo
from vehiculo import agregar_vehiculo

# FUNCTIONS -------------------------------------------------------------
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