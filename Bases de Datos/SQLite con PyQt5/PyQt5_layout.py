'''
PyQt5 - Layout
'''

'''# Layout absoluto -------------------------------------------------------------------------------------
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle('Layout PyQT-5')
    w.resize(250, 120)

    lblName = QLabel("Nombre:", w)
    lblName.move(20, 20)

    lblPass = QLabel("Contraseña:", w)
    lblPass.move(20, 50)

    txtName = QLineEdit(w)
    txtName.setPlaceholderText("Nombre de usuario")
    txtName.move(100, 15)

    txtPass = QLineEdit(w)
    txtPass.setPlaceholderText("Contraseña de usuario")
    txtPass.move(100, 45)

    btnLogin = QPushButton("Login", w)
    btnLogin.move(20, 80)
    btnLogin.resize(218, 30)

    w.show()

    sys.exit(app.exec_())'''

'''# Layout Box -------------------------------------------------------------------------------------
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle('Layout PyQT-5')
    w.resize(250, 120)

    vbox = QVBoxLayout()
    vbox.setSpacing(20)

    for n in range(5):
        if n == 2:
            hbox = QHBoxLayout()
            for m in range(3):
                hbox.addWidget(QPushButton("Button #" + str(m)))
            vbox.addLayout(hbox)
        else:
            vbox.addWidget(QPushButton("Button #" + str(n)))

    w.setLayout(vbox)
    w.show()

    sys.exit(app.exec_())'''

# Layout Grid -------------------------------------------------------------------------------------
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle('Layout PyQT-5')
    w.resize(250, 120)

    lblName = QLabel("Nombre:")
    txtName = QLineEdit()
    txtName.setPlaceholderText("Nombre de usuario")

    lblPass = QLabel("Contraseña:")
    txtPass = QLineEdit(w)
    txtPass.setPlaceholderText("Contraseña de usuario")

    grid = QGridLayout()
    grid.addWidget(lblName, 0, 0)
    grid.addWidget(txtName, 0, 1)
    grid.addWidget(lblPass, 1, 0)
    grid.addWidget(txtPass, 1, 1)

    btnLogin = QPushButton("Login", w)
    grid.addWidget(btnLogin, 2, 0, 1, 2)

    w.setLayout(grid)
    w.show()

    sys.exit(app.exec_())