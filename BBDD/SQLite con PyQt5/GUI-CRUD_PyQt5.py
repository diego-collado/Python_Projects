'''
PyQt5: permite crear GUI con Python, permitiendo separar la parte gráfica de la lógica de programación.
Pasos a realizar:
    1.- pip install PyQt5
    2.- pip install pyqt5-tools
'''

# IMPORTS
import sys # https://docs.python.org/es/3/library/sys.html
from PyQt5.QtSql import * # importación de SQL para PyQt5
from PyQt5.QtCore import Qt, QModelIndex # cargamos el core de PyQt5 (incluyendo el modelo tipo para los items)
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QHBoxLayout, QLineEdit, QLabel, QGridLayout

# CLASS
class PYQT_BD(QWidget):
    # método de creación del sistema ########################################################################
    def __init__(self, parent=None):
        super(PYQT_BD, self).__init__(parent)

        # creación de la tabla (organización de datos) ------------------------------------------------------
        self.table = QTableWidget(0,3) # creación de tabla con 3 columnas
        self.table.setHorizontalHeaderLabels(['ID', 'Nombre', 'Apellidos']) # asignamos el contenido de fila de títulos
        self.table.setAlternatingRowColors(True) # alternar los colores en las filas, según se vayan creando

        # ¿Qué puedo y no puedo hacer? Permisos de QTableWidget
        self.table.setEditTriggers(QTableWidget.NoEditTriggers) # permitir o no la edición individual de las celdas
        self.table.setSelectionBehavior(QTableWidget.SelectRows) # permite obtener valores pinchando en la columna 0
        self.table.setSelectionMode(QTableWidget.SingleSelection) # permite la selección de un único elemento (por defecto permite la selección múltiple)

        # Campos de introducción de datos: inputs -----------------------------------------------------------
        # Campo ID
        self.labelID = QLabel("ID: ")
        self.txtID = QLineEdit()
        self.txtID.setPlaceholderText("Número único, idenficativo del usuario")

        # Campo Nombre
        self.labelName = QLabel("Nombre: ")
        self.txtName = QLineEdit()
        self.txtName.setPlaceholderText("Nombre del usuario")

        # Campo Apellidos
        self.labelSurname = QLabel("Apellido: ")
        self.txtSurname = QLineEdit()
        self.txtSurname.setPlaceholderText("Apellido del usuario")

        # Layout, donde se colocan todos los widgets --------------------------------------------------------
        grid = QGridLayout() # creación del layout como tal, perteneciente al grid de PyQt5

        # añadiendo widgets: ID
        grid.addWidget(self.labelID, 0,0)
        grid.addWidget(self.txtID, 0, 1)

        # añadiendo widgets: Nombre
        grid.addWidget(self.labelName, 1, 0)
        grid.addWidget(self.txtName, 1, 1)

        # añadiendo widgets: Apellidos
        grid.addWidget(self.labelSurname, 2, 0)
        grid.addWidget(self.txtSurname, 2, 1)

        # Botones, acciones en nuestro layout --------------------------------------------------------------

        # botón de carga y mostrado de datos
        btnCargar = QPushButton('Cargar Datos')
        btnCargar.clicked.connect(self.cargarDatos) # función que se ejecuta al hacer clic en el botón

        # botón de agregar nuevos datos
        btnInsertar = QPushButton('Insertar Datos')
        btnInsertar.clicked.connect(self.insertarDatos)  # función que se ejecuta al hacer clic en el botón

        # botón de carga y mostrado de datos
        btnEliminar = QPushButton('Eliminar Datos')
        btnEliminar.clicked.connect(self.eliminarDatos)  # función que se ejecuta al hacer clic en el botón

        # creación de frame para insertar los botones
        hbx = QHBoxLayout() # creación de un frame para inserción de los botones
        # inserción de botones en layout
        hbx.addWidget(btnCargar)
        hbx.addWidget(btnInsertar)
        hbx.addWidget(btnEliminar)

        # creación del entorno visual (título, ...) ---------------------------------------------------------
        vbx = QVBoxLayout() # creación del entorno visual
        vbx.addLayout(grid) # se añade el grid creado (inputs)
        vbx.addLayout(hbx) # se añaden los botones

        vbx.setAlignment(Qt.AlignTop) # alineación del conjunto en la parte superior

        vbx.addWidget(self.table) # se añade a la tabla

        # parámetros para la ventana
        self.setWindowTitle("PyQT v.5 - BBDD para SQLite") # título de la ventana
        self.resize(450, 425) # tamaño de la ventana
        self.setLayout(vbx) # layout que se cargará en la ventana

# METHODS
    # Recuperar datos a la BBDD ############################################################################
    def cargarDatos(self, event): # se recibe un evento del ratón
        index = 0

        # 1.- creación de instancia del Query
        query = QSqlQuery()

        # 2.- ejecución de SQL
        query.exec_("select * from personas")

        # 3.- iteración de datos recibidos en la lectura, organizados en la tabla
        while query.next():
            ids = query.value(0) # campo ID
            nombre = query.value(1) # campo Nombre
            apellido = query.value(2)  # campo Apellidos

            # organización en la tabla
            self.table.setRowCount(index + 1) # comenzamos en la fila 0 hasta finalizar el "array"
            self.table.setItem(index, 0, QTableWidgetItem(str(ids))) # se inserta la ID, convertidas en string
            self.table.setItem(index, 1, QTableWidgetItem(nombre)) # se inserta el nombre
            self.table.setItem(index, 2, QTableWidgetItem(apellido)) # se inserta el apellido

            index += 1 # cada iteracción, pasa a la siguiente fila

    # Insertar datos a la BBDD ############################################################################
    def insertarDatos(self, event):
        # obtención de valores de los campos de texto
        ids = int(self.txtID.text())
        nombre = self.txtName.text()
        apellido = self.txtSurname.text()

        # ejecución de query
        query = QSqlQuery() # creación de la instancia de query
        query.exec_("insert into personas values ({0}, '{1}', '{2}')".format(ids, nombre, apellido))

    # Eliminar datos a la BBDD ############################################################################
    def eliminarDatos(self, event):
        # fila seleccionada para eliminar
        selected = self.table.currentIndex() # se selecciona aquella posición en la que se encuentre el índice
        if not selected.isValid() or len(self.table.selectedItems()) < 1:
            return

        # valor de la tabla
        ids = self.table.selectedItems()[0] # se seleccionan las IDs, primera columna

        # ejecución de query
        query = QSqlQuery()  # creación de la instancia de query
        query.exec_("delete from personas where id = " + ids.text()) # elimina la fila cuyo ID es el idéntico al seleccionado

        # borrado de fila
        self.table.removeRow(selected.row())
        self.table.setCurrentIndex(QModelIndex()) # deja el índice en el lugar correcto

    # Gestión de la BBDD ##################################################################################
    # 1.- Creación de la BBDD
    def db_connect(self, filename, server): # se reciben tanto el nombre del fichero SQL como el host
        db = QSqlDatabase.addDatabase(server) # creación de la BBDD en el host
        db.setDatabaseName(filename) # asignación de nombre a la BBDD

        # en caso de error, "romper el cristal"
        if not db.open():
            QMessageBox.critical(None, "Error de apertura de la BBDD. Click para salir cancelando...", QMessageBox.Cancel)
            return False
        return True

    # 2.- Creación de la tabla personas en la BBDD
    def db_create(self):
        # creación de la tabla
        query = QSqlQuery() # creación de la instancia de query
        query.exec_("create table personas(id int primary key, "
                    "firstname varchar(20), lastname varchar(20))")

        # inserción de datos de "prueba"
        query.exec_("insert into personas values(101, 'Diego', 'Collado')")
        query.exec_("insert into personas values(102, 'David', 'Moreno')")
        query.exec_("insert into personas values(103, 'Cristina', 'Boscá')")
        query.exec_("insert into personas values(104, 'Kéru', 'Sánchez')")
        query.exec_("insert into personas values(105, 'Nacho', 'Gómez Hermosura')")

    # 3.- Ejecución de la BBDD
    def init(self, filename, server):
        import os # importación de módulo para trabajar con el sistema operativo

        # rompa el cristal si tenemos un error
        if not os.path.exists(filename):
            self.db_connect(filename, server) # llamada para conexión con BBDD
            self.db_create() # creación de la BBDD
        else:
            self.db_connect(filename, server) # reconexión con BBDD

# MAIN
if __name__ == '__main__':
    app = QApplication(sys.argv) # Creamos una instancia de "QApplication"
    ejemplo = PYQT_BD() # Instancia de nuestra clase "PYQT_DB"
    # Llamamos al metodo "init": base de datos llamada 'personas', de tipo 'SQLite'
    ejemplo.init('personas', 'QSQLITE')
    ejemplo.show() # Ejecutamos la ventana
    sys.exit(app.exec_()) # Cerramos el proceso





