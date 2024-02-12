'''
Introducir el nombre de usuario y clave en controles de tipo Entry.
Si se ingresa las cadena (usuario: juan, clave="abc123"), mostrar en el título de la ventana el
mensaje "Correcto" en caso contrario mostrar el mensaje "Incorrecto".

Para mostrar ** cuando se ingresa la clave debemos pasar en el parámetro 'show' el carácter a
mostrar: show="*"
'''
#IMPORTS
import tkinter as tk

#CLASS
class Login:
    def __init__(self):
        # Ventana Padre -------------------------------------------------------------------
        self.ventana = tk.Tk()
        self.ventana.geometry("350x350")

        # Carga de icono ------------------------------------------------------------------
        icono = tk.PhotoImage(file="monete.png")# Carga del icono en PNG
        self.ventana.iconphoto(True, icono) # Inserción del PNG en la ventana
        #self.ventana.iconbitmap("monete.ico") # ICO solo para Windows

        '''# Con varios tamaños de icono
        icono_chico = tk.PhotoImage(file="monete2.png")
        icono_grande = tk.PhotoImage(file="monete.png")

        self.ventana.iconphoto(False, icono_chico, icono_grande)'''

        # Etiquetas de introducción de usuario y password ---------------------------------
        self.etiq_user = tk.Label(self.ventana, text="USUARIO ")
        self.etiq_password = tk.Label(self.ventana, text="PASSWORD ")

        # Colocación de etiquetas
        self.etiq_user.grid(column=0, row=0)
        self.etiq_password.grid(column=1, row=0)

        # Creación de variables asociadas a los inputs ------------------------------------
        self.usuario = tk.StringVar()
        self.contrasenna = tk.StringVar()

        # Inputs para introducción de valores
        self.entrada_user = tk.Entry(self.ventana, width=20, textvariable=self.usuario)
        self.entrada_pass = tk.Entry(self.ventana, width=20, textvariable=self.contrasenna, show="*")

        # Colocación de los inputs en pantalla
        self.entrada_user.grid(column=0, row=1)
        self.entrada_pass.grid(column=1, row=1)

        # Creación y colocación de botón ---------------------------------------------------
        self.boton_entrar = tk.Button(self.ventana, text="Acceder al sistema...", command=self.ingresar)
        self.boton_entrar.grid(column=1, row=2)

        # Arranque de ventana completa
        self.ventana.mainloop()

    def ingresar(self):
        if (self.usuario.get() == "Juan") and (self.contrasenna.get() == "abc123"):
            self.ventana.title("Acceso concecido y Correcto")
        else:
            self.ventana.title("Acceso no permitido, usuario o password incorrectos")


#MAIN
loguear = Login()