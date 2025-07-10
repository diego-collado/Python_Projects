# servicio.py

# IMPORTS ---------------------------------------------------------------
from datos import taller # Importamos un determinado elemento de un archivo completo

# FUNCTIONS -------------------------------------------------------------

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