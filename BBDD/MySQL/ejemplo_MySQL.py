'''
1º acción con MySQL: conectar la BBDD

import mysql.connector # importación del módulo de conexión y manejo de conexiones para MySQL
# creamos una conexión con nuestra BBDD
conexion = mysql.connector.connect(host="localhost", user="admministrador", passwd="guOG=L;uc}")

# posicionamos el cursor
cursor = conexion.cursor()

# ejecutamos un script SQL
cursor.execute("show databases")

# imprimir en pantalla las BBDDs que tengamos disponibles
for bases in cursor:
    print(bases)
# cierre de la conexión con BBDD
conexion.close()'''

'''
2º acción con MySQL: conectar a una BBDD determinada para listar tablas

import mysql.connector
conexion = mysql.connector.connect(host="localhost",
                                   user="admministrador",
                                   passwd="guOG=L;uc}",
                                   database="base_articulos")
# al añadir un argumento más a la conexión, trabajamos y utilizamos una BBDD determinada
cursor = conexion.cursor()
cursor.execute("show tables")
for tables in cursor:
    print(tables)
conexion.close()'''

'''
3º acción con MySQL: conectar a una BBDD determinada para insertar filas en la tabla

import mysql.connector
conexion = mysql.connector.connect(host="localhost",
                                   user="admministrador",
                                   passwd="guOG=L;uc}",
                                   database="base_articulos")
cursor = conexion.cursor()
sql = "insert into articulos(descripcion, precio) values (%s,%s)"
# máscara %s: aquí se sustituye por el valor que le paso al execute
datos = ("Orbea Nata", 3250.85)
cursor.execute(sql, datos)
datos = ("Orbea Plátano", 6250.85)
cursor.execute(sql, datos)
datos = ("Orbea Fresa", 2250.85)
cursor.execute(sql, datos)
datos = ("Orbea Vaso", 8050.85)
cursor.execute(sql, datos)

conexion.commit()# se hacen todos los insert en su correspondiente lugar
conexion.close()'''

'''
4º acción con MySQL: mostrar los datos de una tabla

import mysql.connector
conexion = mysql.connector.connect(host="localhost",
                                   user="admministrador",
                                   passwd="guOG=L;uc}",
                                   database="base_articulos")
cursor = conexion.cursor()
cursor.execute("select codigo,descripcion,precio from articulos")
for fila in cursor:
    print(fila)
conexion.close()'''

'''
5º acción con MySQL: borrado y modificación de filas

import mysql.connector
conexion = mysql.connector.connect(host="localhost",
                                   user="admministrador",
                                   passwd="guOG=L;uc}",
                                   database="base_articulos")
cursor = conexion.cursor()
cursor.execute("delete from articulos where codigo=1")# borrado de un registro
cursor.execute("update articulos set precio=9675.35 where codigo=3")
conexion.commit()
cursor.execute("select codigo,descripcion,precio from articulos")
for fila in cursor:
    print(fila)
conexion.close()'''