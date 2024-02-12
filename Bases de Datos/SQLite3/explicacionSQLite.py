'''
BBDD (Base de Datos) un conjunto de diferentes tipos de datos, agrupados en un solo elemento: la BBDD
Tipos:
    - SQL           - MySQL             - PostgreSQL
    - Oracle        - SQLServer         - MariaDB

En este caso, la mayor parte de estos "lenguajes de BBDD" son de tipo relacional, es decir, relacionamos
los datos que tenemos dentro:

nº identificación, nº tlf, nombre, apellidos, email, dirección, cumpleaños... = 1 registro (1 persona en mi móvil)

SQL = Structure Query Language (Lenguaje de Consulta Estructurado)

BBDD para Python (está dentro del paquete instalado en el sistema) --> SQLite3
SQLite es Open Source

Registro ======= es casi lo mismo que un diccionario de Python

¿Qué hacer al enfrentarnos a una BBDD? ------------------------------------------------------------
1.- conectar:
    a.- comprobamos si tenemos conexión
    b.- comprobamos qué privilegios tenemos sobre la BBDD
    c.- si tenemos privilegios, pasamos a la siguiente fase, sino, el propio gestor nos "echa"
2.- realizar operaciones:
    a.- crear tablas: estructuras básicas que recogen registros del mismo tipo
    b.- insertar datos en las tablas
    c.- recuperar datos (visualizar o mostrar)
    d.- borrar datos/tablas/BBDD completa
    e.- actualizar tablas o registros
3.- cerrar conexión:
    a.- "echar abajo" el sistema, para que no haya acceso desde fuera de mis "dominios"
    b.- punto y final, BBDD "protegida"

Tipos de datos que puedo utilizar en una BBDD --------------------------------------------------------
    - NULL: se da cuando se produce un error o se crea un campo sin contenido dentro (nulo)
    - INTEGER: enteros (TINYINT, SMALLINT, MEDIUMINT, BIGINT, UNSIGNED BIG INT, INT2 y INT8)
    - REAL: reales (con coma flotante) -(DOUBLE, DOUBLE PRECISION y FLOAT)
    - TEXT: cadena de texto, almacenada usando una codificación (UTF-8) - CHARACTER(20), VARCHAR(255),
    VARYING CHARACTER(255), NCHAR(55), NATIVE CHARACTER(70), NVARCHAR(100), TEXT y
    CLOB - Objetos grandes de caracteres (CLOB) / Objetos grandes de caracteres de doble byte (DBCLOB)
    - NUMERIC: (DECIMAL(10,5), BOOLEAN, DATE y DATETIME)
    - BLOB: el formato puro (RAW en fotografía o disco duro sin formato)
    Objetos binarios grandes (BLOB)
    - NONE: no existe, no es nada, pero molesta mogollón... Siempre sucede cuando no existe algo en la tabla X

A tener muy muy muy muy en cuenta a la hora de trabajar con las BBDD -----------------------------------

    1.- Necesitamos un PK (Primary Key), que es un campo por el cual podremos encontrar el dato que nos interese:
        ejemplo --> ¿Cómo me encuentra la policia nacional en su BBDD? por mi DNI o NIE, a través del cual aparecen
        el resto de mis datos como dirección, email, teléfono...
        Cada tabla tiene una PK sí, sí o sí
    2.- autoincrement sirve para poder poner código de forma que automáticamente se vayan incrementando
'''

#1ª FASE: CREACIÓN DE TABLA/S -------------------------------------------------------------------------------
#IMPORTS
'''import sqlite3

# MAIN
conexion = sqlite3.connect("base_ejemplo")# conexión a la BBDD

try:
    #SQL: CREATE TABLE nombre (campos....)
    conexion.execute("""create table articulos (
        codigo_articulo integer primary key autoincrement,
        descripcion varchar(200),
        precio float);""")

    print("Se ha creado la tabla ARTÍCULOS con éxito")

except sqlite3.OperationalError as oe:
    print("Error en la gestión:",oe)

conexion.close() # cierre de la conexión

#2ª FASE: INSERTAR DATOS EN TABLA/S --------------------------------------------------------------------------
#IMPORTS
import sqlite3

# MAIN
conexion = sqlite3.connect("base_ejemplo")# conexión a la BBDD

#SQL: INSERT INTO tablaX (campo1, campo2) VALUES (dato), (dato);
conexion.execute("""insert into articulos (descripcion, precio) values (?,?);""",("BMW", 108000.50))
conexion.execute("""insert into articulos (descripcion, precio) values (?,?);""",("Mercedes", 118000.50))
conexion.execute("""insert into articulos (descripcion, precio) values (?,?);""",("AMG", 188000.50))

conexion.commit()# inserta los datos en la BBDD (grabación de datos en la BBDD)
conexion.close()# cierre de la conexión con la BBDD

#3ª FASE: RECUPERAR DATOS DE LA/S TABLA/S --------------------------------------------------------------------
#IMPORTS
import sqlite3

# MAIN
conexion = sqlite3.connect("base_ejemplo")# conexión a la BBDD

#SQL: SELECT * FROM tablaX --
cursor = conexion.execute("""select codigo_articulo, descripcion, precio from articulos;""")# recupera toooodos los registros

for registro in cursor:
    print(registro)

conexion.close()# cierre de la conexión con la BBDD

#4ª FASE: RECUPERAR DATOS DETERMINADOS DE LA/S TABLA/S ------------------------------------------------------------
#IMPORTS
import sqlite3

# MAIN
conexion = sqlite3.connect("base_ejemplo")# conexión a la BBDD

codigo_pedido = int(input("Introduce el código del artículo: "))

#SQL: SELECT * FROM tablaX --
cursor = conexion.execute("""select descripcion, precio from articulos where codigo_articulo=?;""",(codigo_pedido,))
# recupera el registro con el código insertado

registro = cursor.fetchone() # se utiliza para devolver una sola fila de resultados de una consulta SQL

if (registro != None):# si hay contenido, imprime
    print(registro)

else:
    print(f"El artículo con el código {codigo_pedido} no existe...")

conexion.close()# cierre de la conexión con la BBDD'''

#4ª FASE BIS: RECUPERAR DATOS DETERMINADOS DE LA/S TABLA/S ---------------------------------------------------------
#IMPORTS
import sqlite3

# MAIN
conexion = sqlite3.connect("base_ejemplo")# conexión a la BBDD

precio = float(input("Introduce el precio del artículo: "))

cursor = conexion.execute("""select descripcion from articulos where precio<=?""",(precio,))

registros = cursor.fetchall()# captura los registros que coincidan con lo que pedimos

if (len(registros) > 0):
    for registro in registros:
        print(registro)

else:
    print("No hay artículos con el precio introducido o menor")


conexion.close()# cierre de la conexión con la BBDD