'''
Realizar las siguientes nuevas acciones en nuestro CRUD:
    1. Recuperar el valor del campo auto_increment en un insert
    2. Inserción de múltiples filas en una tabla
    3. Área para creación de una base de datos y tablas nuevas
    4. Área para borrar una base de datos
    5. Borrar una tabla y crear otra con el mismo nombre
'''

'''# 1. Recuperar el valor del campo auto_increment en un insert
import mysql.connector
conexion = mysql.connector.connect(host="localhost",
                                   user="admministrador",
                                   passwd="guOG=L;uc}",
                                   database="base_articulos")
cursor = conexion.cursor()
cursor.execute("insert into articulos (descripcion, precio) values (%s,%s)", ("Orbea patata",5000))
conexion.commit()

print(f"ID último artículo: {cursor.lastrowid}")
conexion.close()

# 1. Recuperar el valor del campo auto_increment en un insert (DaríoVersión)
cursor.execute("select last_insert_id() ")'''

'''# 2. Inserción de múltiples filas en una tabla
import mysql.connector
conexion = mysql.connector.connect(host="localhost",
                                   user="admministrador",
                                   passwd="guOG=L;uc}",
                                   database="base_articulos")
cursor = conexion.cursor()
filas=[ ("orbea puñeta", 4506.25), ("orbea quetevea",9085.25), ("Orbea la fea",9344.25), ("orbea laTraca",10000.25) ]
sql = "insert into articulos (descripcion, precio) values (%s,%s)"
cursor.executemany(sql,filas)# se insertan más de 1 una fila a la vez
conexion.commit()
conexion.close()'''

'''# 3. Área para creación de una base de datos y tablas nuevas
import mysql.connector
conexion = mysql.connector.connect(host="localhost",
                                   user="root",
                                   passwd="")
cursor = conexion.cursor()
cursor.execute("create database base2")# crear bbdd
cursor.execute("use base2")# usar bbdd
cursor.execute("""create table usuarios (nombre varchar(35) primary key, clave varchar(30))""")
conexion.commit()
conexion.close()'''

# 4. Área para borrar una base de datos
import mysql.connector
conexion = mysql.connector.connect(host="localhost",
                                   user="root",
                                   passwd="")
cursor = conexion.cursor()
cursor.execute("drop database if exists base2")# borrar bbdd
conexion.commit()
conexion.close()

# 5. Borrar una tabla y crear otra con el mismo nombre
...
cursor.execute("drop table if exists usuarios")# borrar tabla usuarios
cursor.execute("create table usuarios (nombre varchar(35) primary key, clave varchar(30))")
...