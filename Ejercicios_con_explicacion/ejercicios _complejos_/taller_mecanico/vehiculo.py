# vehiculo.py


# IMPORTS ---------------------------------------------------------------
from datos import taller # Importamos un determinado elemento de un archivo completo

# FUNCTIONS -------------------------------------------------------------
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