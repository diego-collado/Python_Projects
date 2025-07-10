-- ESTRUCTURA DEL TALLER MECÁNICO --

taller_mecanico/
    |- main.py      # Punto de entrada principal del programa
    |- cliente.py   # Funcionalidades relacionadas con los clientes
    |- vehiculo.py  # Funcionalidades relacionadas con los vehículos
    |- servicio.py  # Funcionalidades relacionadas con los servicios
    |- datos.py     # Estructura principal (diccionario) y almacenamiento de datos

-- CUESTIONES A TENER EN CUENTA --
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
