'''
PyQt5 - items
'''
'''
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QComboBox, QStyleFactory, QListWidget, \
    QTableWidget, QTableWidgetItem, QListWidgetItem


class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        QApplication.setStyle(QStyleFactory.create('Fusion'))

        # -------------- QCOMBOBOX ----------------------
        cbx = QComboBox()
        # agregar lista de nombres de estilos disponibles
        cbx.addItems(QStyleFactory.keys())
        # responder al evento cambio de texto
        cbx.currentTextChanged.connect(self.textChanged)
        # seleccionar el ultimo elemento
        cbx.setItemText(4, 'Fusion')

        # -------------- QLISTWIDGET ---------------------
        items = ['Ubuntu', 'Linux', 'Mac OS', 'Windows', 'Fedora', 'Chrome OS', 'Android', 'Windows Phone']

        self.lv = QListWidget()
        self.lv.addItems(items)
        self.lv.itemSelectionChanged.connect(self.itemChanged)

        # -------------- QTABLEWIDGET --------------------
        self.table = QTableWidget(10, 3)
        # establecer nombre de cabecera de las columnas
        self.table.setHorizontalHeaderLabels(['Nombre', 'Edad', 'Nacionalidad'])
        # evento producido cuando cambia el elemento seleccionado
        self.table.itemSelectionChanged.connect(self.tableItemChanged)
        # alternar color de fila
        self.table.setAlternatingRowColors(True)
        # seleccionar solo filas
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        # usar seleccion simple, una fila a la vez
        self.table.setSelectionMode(QTableWidget.SingleSelection)

        table_data = [
            ("Alice", 15, "Panama"),
            ("Dana", 25, "Chile"),
            ("Fernada", 18, "Ecuador")
        ]

        # agregar cada uno de los elementos al QTableWidget
        for i, (name, age, city) in enumerate(table_data):
            self.table.setItem(i, 0, QTableWidgetItem(name))
            self.table.setItem(i, 1, QTableWidgetItem(str(age)))
            self.table.setItem(i, 2, QTableWidgetItem(city))

        vbx = QVBoxLayout()
        vbx.addWidget(QPushButton('PyQT-5'))
        vbx.setAlignment(Qt.AlignTop)
        vbx.addWidget(cbx)
        vbx.addWidget(self.lv)
        vbx.addWidget(self.table)

        self.setWindowTitle("Items View")
        self.resize(362, 320)
        self.setLayout(vbx)

    def textChanged(self, txt):
        QApplication.setStyle(QStyleFactory.create(txt))

    def itemChanged(self):
        item = QListWidgetItem(self.lv.currentItem())
        print("Sistema seleccionado: ", item.text())

    def tableItemChanged(self):
        name, age, city = self.table.selectedItems()
        print("Data:", name.text(), age.text(), city.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ejm = Example()
    ejm.show()
    sys.exit(app.exec_())'''

'''
PyQt5 - diágolos
'''

import sys

from PyQt5.QtCore import Qt, QDir
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog, QVBoxLayout, QPushButton, QFileDialog, QColorDialog, \
    QFontDialog, QMessageBox


class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)

        btn0 = QPushButton('Mostrar QInputDialog')
        btn0.clicked.connect(self.showIntDialog)

        btn1 = QPushButton('Mostrar QFileDialog')
        btn1.clicked.connect(self.buscarArchivo)

        btn2 = QPushButton('Mostrar QColorDialog')
        btn2.clicked.connect(self.buscarColor)

        btn3 = QPushButton('Mostrar QFontDialog')
        btn3.clicked.connect(self.cambiarFuente)

        btn4 = QPushButton('Mostrar QMessageBox')
        btn4.clicked.connect(self.showDialog)

        vbox = QVBoxLayout()
        vbox.addWidget(btn0)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addStretch(0)

        self.setLayout(vbox)
        self.setWindowTitle("Cuadros de Dialogo")
        self.resize(250, 320)

    def buscarArchivo(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Buscar Archivo')#, QDir.homePath(), "All Files (*);;Text Files (*.txt)")
        if file:
            print("Archivo seleccionado: ", file)

    def showIntDialog(self):
        value, ok = QInputDialog.getText(self, "getText()", "Como te llamas:")
        if ok and value != '' : print('Nombre:', value)

        value, ok = QInputDialog.getInt(self, "getInt()", "Dime Tu Edad:", 18, 1, 150)
        if ok : print('Edad:', value)

        value, ok = QInputDialog.getDouble(self, "getDouble()", "Cuanto Pesas:")
        if ok : print('Peso:', value)

        items = ("Perro", "Gato", "Aves", "Serpientes", "Otros")
        value, ok = QInputDialog.getItem(self, "getItem()", "Mascota favorita:", items, 2)
        if ok : print('Mascota:', value)

    def buscarColor(self):
        color = QColorDialog.getColor(Qt.red, self)
        if color.isValid():
            self.setPalette(QPalette(color))

    def cambiarFuente(self):
        font, ok = QFontDialog.getFont(self)
        if ok:
            self.setFont(font)

    def showDialog(self):
        # QMessageBox.warning(self, "Warning Dialog", "Peligro Alto Voltage")
        reply = QMessageBox.critical(self, "QMessageBox.critical()",
                "Error irrecuperable en la aplicacion \n que desea hacer para proceder.",
                QMessageBox.Abort | QMessageBox.Retry | QMessageBox.Ignore)
        if reply == QMessageBox.Abort:
            print("Abortar la mision")
        elif reply == QMessageBox.Retry:
            print("Intentar nuevamente")
        else:
            print("Nada por ahora")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Example()
    dialog.show()
    sys.exit(app.exec_())