'''
Login visual a una BBDD con SQLite3
'''

#IMPORTS
import tkinter
#from CTkMessagebox import *
from tkinter import ttk
import sqlite3
from tkinter.messagebox import showinfo, showerror

# MAIN

# Construcción de la ventana

#ventana
ventana = tkinter.Tk()
ventana.title("-- LOGIN PARA EXPERTOS --")
ventana.geometry("350x150+500+250")

# icono
icono = tkinter.PhotoImage(file="monete.png")
ventana.iconphoto(True, icono)

# cajas - etiquetas + inputs
tkinter.Label(ventana, text="USUARIO:").pack()# etiqueta + centradao (.pack())
caja_user = tkinter.Entry(ventana)
caja_user.pack()

tkinter.Label(ventana, text="PASSWORD:").pack()# etiqueta + centradao (.pack())
caja_pass = tkinter.Entry(ventana, show="*")
caja_pass.pack()

# métodos utilizados para el login
def login():
    # conexión a BBDD e inicialización de lectura
    bd = sqlite3.connect("base_ejemplo")
    cursor = bd.cursor()

    usuario = caja_user.get()
    password = caja_pass.get()

    # comparación de lo que tenemos en la BBDD y lo que estamos poniendo en el input
    cursor.execute("""select * from usuarios where usuario = ? and pass = ?""", (usuario, password))

    if cursor.fetchall():# se recupera la información que sea la que buscamos
        showinfo(title = "Login correcto", message = "Usuario y contraseña correctos")
    else:
        showerror(title="Login incorrecto", message="Usuario o contraseña incorrecta")

    cursor.close()

tkinter.Button(text="LOGUEARSE...", command=login).pack()


ventana.mainloop()