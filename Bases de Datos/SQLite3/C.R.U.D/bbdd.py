'''
C.R.U.D.:  Create, Read, Update, Delete
'''

#IMPORTS ------------------------------------------------------------------------------
import sqlite3

#MAIN ------------------------------------------------------------------------------
conexion = sqlite3.connect("BaseDatos.db")

try:
    conexion.execute("create table articulos (codigo integer primary key autoincrement,"
                     "descripcion text,"
                     "precio real)")
    print("Se ha creado la tabla artículos con éxito...")

except sqlite3.OperationalError:
    print("La tabla artículos existe...")

conexion.close()