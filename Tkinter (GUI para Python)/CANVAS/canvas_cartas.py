'''
Presionando un botón, aparecerá una carta aleatoria, es decir, sacamos una carta al azar
'''

# IMPORTS
import tkinter as tk
from tkinter import ttk
import random

# CLASS
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk() # creación de ventana

        # Creación y colocación de botón
        self.boton = ttk.Button (self.ventana, text="Mezclar", command=self.mezclar)
        self.boton.grid(column=0, row=0)

        # Creación y colocación de zona Canvas
        self.canvas = tk.Canvas(self.ventana, width=300, height=500, background="black")
        self.canvas.grid(column=0, row=1)

        # Carga de las imágenes externas (cartas)
        # Formatos reconocidos de la clase PhotoImage son: GIF, PNG, PGM y PPM
        self.archivo1 = tk.PhotoImage(file="carta1.png") # se ha de indicar el path (ruta) completo
        self.archivo2 = tk.PhotoImage(file="carta2.png")
        self.archivo3 = tk.PhotoImage(file="carta3.png")

        # llamada a una carta "previa" que esté en pantalla antes de mezclar
        self.canvas.create_image(50, 100, image=self.archivo1, anchor="nw")
        '''
        Anchor determina el vértice superior que, en este caso, es el superior izquierdo
        Los valores posibles del parámetro anchor son: 
            "n", "ne", "e", "se", "s", "sw", "w", "nw" y "center"
        '''

        self.ventana.mainloop()

    def mezclar(self):
        valor = random.randint(1,3)

        if (valor == 1):
            self.canvas.create_image(50, 100, image=self.archivo1, anchor="nw")

        if (valor == 2):
            self.canvas.create_image(50, 100, image=self.archivo2, anchor="nw")

        if (valor == 3):
            self.canvas.create_image(50, 100, image=self.archivo3, anchor="nw")

# MAIN
aplicacion1 = Aplicacion()