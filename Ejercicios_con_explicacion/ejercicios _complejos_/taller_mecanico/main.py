# main.py

# IMPORTS ---------------------------------------------------------------
from cliente import agregar_cliente, editar_cliente, eliminar_cliente, ver_historial_cliente
from vehiculo import agregar_vehiculo, eliminar_vehículo, buscar_placa
from servicio import registrar_servicio, ver_historial_vehículo

# FUNCTIONS -------------------------------------------------------------
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
if __name__ == "__main__":
    menu()