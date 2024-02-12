'''
Implementar 3 controles de tipo Radiobutton con las etiquetas 'Rojo', 'Verde' y 'Azul'.
Cuando se presione un botón cambiar el color de fondo del formulario.
Si consideramos que la variable ventana es un objeto de la clase Tk, si queremos que el fondo sea de color
rojo debemos llamar al método configure y en el parámetro bg indicar un string con el color a activar
("red", "green" o "blue"): bg="red"

REFERENCIA DE COLORES: https://www.delftstack.com/img/Python/python%20colors.webp

IMPORTACIÓN DE COLORES:  colorama  -->
from colorama import *
init()

Fore.color_en_mayusculas --> Cambiar color
Back.color_en_mayusculas --> Cambiar el fondo
Style.estilo_en_mayusculas --> Cambiar el estilo

Style.RESET_ALL --> reseteo de cualquier tipo de estilo para poder implementar el mío propio
'''
#IMPORTS
import tkinter as tk

#CLASS
class Cambiante:

    def __init__(self):
        # Ventana --------------------------------------------------------------------
        self.ventana = tk.Tk()
        self.ventana.title("Colour-Cambiante")
        self.ventana.config(bg="pink")
        self.ventana.resizable(0,0)# Prohibimos el manejo del tamaño

        # Área de selección ----------------------------------------------------------
        self.seleccion = tk.IntVar()
        self.seleccion.set(1)# Se deja pre-seteado a 1, es decir, el color básico/base

        # Radio Button ---------------------------------------------------------------

        # Creación de los radiobutton
        self.boton_radio1 = tk.Radiobutton(self.ventana, text="Rojo", variable=self.seleccion, value=1)
        self.boton_radio2 = tk.Radiobutton(self.ventana, text="Verde", variable=self.seleccion, value=2)
        self.boton_radio3 = tk.Radiobutton(self.ventana, text="Azul", variable=self.seleccion, value=3)

        # Colocación de los radiobutton
        self.boton_radio1.grid(column=0, row=0)
        self.boton_radio2.grid(column=0, row=1)
        self.boton_radio3.grid(column=0, row=2)

        # Botón de activación ---------------------------------------------------------
        self.boton_activar = tk.Button(self.ventana, text="aCTiVaR CoLoR", command=self.activar)
        self.boton_activar.grid(column=0, row=3)

        # Creación y arranque de la ventana -------------------------------------------
        self.ventana.mainloop()

    def activar(self):
        if (self.seleccion.get() == 1):
            self.ventana.configure(bg="red")
        elif (self.seleccion.get() == 2):
            self.ventana.configure(bg="green")
        elif (self.seleccion.get() == 3):
            self.ventana.configure(bg="blue")

#MAIN
cambiar = Cambiante()