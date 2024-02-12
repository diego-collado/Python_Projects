'''
Formularios CRUD:
    - lógica de acceso a datos (SQLite)
'''
#IMPORTS ------------------------------------------------------------------------------
import mysql.connector

#CLASS ------------------------------------------------------------------------------
class Articulos:

    # método de conexión a BBDD
    def abrir(self):
        conexion = mysql.connector.connect(host="localhost",
                                           user="admministrador",
                                           passwd="guOG=L;uc}",
                                           database="base_articulos")
        return conexion

    # método de alta de nuevos artículos
    def alta(self, datos):
        conexion = self.abrir()
        cursor = conexion.cursor()
        #sql = "insert into articulos(descripcion,precio) values (?,?)"
        #cursor.execute(sql, datos)
        cursor.execute("insert into articulos(descripcion,precio) values (%s,%s)", datos)
        conexion.commit()
        conexion.close()

    # método de consulta de artículos por precio
    def consulta(self,datos):
        try:
            conexion = self.abrir()
            cursor = conexion.cursor()
            cursor.execute("select descripcion, precio from articulos where codigo=%s", datos)
            return cursor.fetchall()# carga todos los datos de la BBDD
        finally:
            conexion.close()

    # método de recuperación de todos los artículos para listado completo
    def recuperar_todos(self):
        try:
            conexion = self.abrir()
            cursor = conexion.cursor()
            cursor.execute("select codigo,descripcion,precio from articulos")
            return cursor.fetchall()# carga todos los datos de la BBDD
        finally:
            conexion.close()

    # método de baja de artículos
    def baja(self,datos):
        try:
            conexion = self.abrir()
            cursor = conexion.cursor()
            sql = "delete from articulos where codigo=%s"
            cursor.execute(sql, datos)
            conexion.commit()
            return cursor.rowcount  # retornamos la cantidad de filas borradas
        except:
            conexion.close()

    # método de modificación de artículos
    def modificacion(self, datos):
        try:
            conexion = self.abrir()
            cursor = conexion.cursor()
            sql = "update articulos set descripcion=%s, precio=%s where codigo=%s"
            cursor.execute(sql, datos)
            conexion.commit()
            return cursor.rowcount  # retornamos la cantidad de filas modificadas
        except:
            conexion.close()