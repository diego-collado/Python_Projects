'''
Después de dibujar líneas, rectángulos... Debemos utilizar los botones para realizar eventos sobre
una determinada figura.
'''

# IMPORTS
import tkinter as tk
from tkinter import ttk

# CLASS
class Aplicacion:
    def __init__(self):
        # constructores de entorno
        self.ventana = tk.Tk()  # creación de la ventana principal
        self.creaBotones() # llamada a método para la creación de botonera con eventos
        self.canvas = tk.Canvas(self.ventana, width=600, height=400, background="black")  # donde se inicia Canvas
        self.canvas.grid(column=0, row=1)

        # constructores de objetos que estarán en el área Canvas
        self.linea = self.canvas.create_line(0, 0, 100, 50, fill="green")
        self.rectangulo = self.canvas.create_rectangle(150, 10, 300, 110, fill="red")
        self.ovalo = self.canvas.create_oval(400, 100, 500, 150, fill="blue")

        self.canvas.create_rectangle(100, 300, 150, 350, fill="#aaaaaa", tag="cuadrado")
        self.canvas.create_rectangle(200, 300, 250, 350, fill="#555555", tag="cuadrado")
        self.canvas.create_rectangle(300, 300, 350, 350,fill="#cccccc", tag="cuadrado")

        self.ventana.mainloop() # arranque del entorno y objetos

    def creaBotones(self):
        # creación de un frame
        self.labelframe = ttk.Labelframe(self.ventana, text="^ - ^ Opciones ^ - ^")
        self.labelframe.grid(column=0, row=0, sticky="w", padx=5, pady=5)

        # creación de botones
        self.boton1 = ttk.Button(self.labelframe, text="Borrar línea", command=self.borraLinea)
        self.boton1.grid(column=0, row=0, padx=5)

        self.boton2 = ttk.Button(self.labelframe, text="Borrar rectángulo", command=self.borraRectangulo)
        self.boton2.grid(column=1, row=0, padx=5)

        self.boton3 = ttk.Button(self.labelframe, text="Borrar óvalo", command=self.borraOvalo)
        self.boton3.grid(column=2, row=0, padx=5)

        self.boton4 = ttk.Button(self.labelframe, text="Borrar cuadrados", command=self.borraCuadrados)
        self.boton4.grid(column=3, row=0, padx=5)

        self.boton5 = ttk.Button(self.labelframe, text="Borrar TODOS", command=self.borraTodo)
        self.boton5.grid(column=4, row=0, padx=5)

    # MÉTODOS LLAMADOS EN EL CONSTRUCTOR
    def borraLinea(self):
        self.canvas.delete(self.linea)
    def borraRectangulo(self):
        self.canvas.delete(self.rectangulo)
    def borraOvalo(self):
        self.canvas.delete(self.ovalo)
    def borraCuadrados(self):
        self.canvas.delete("cuadrado")
    def borraTodo(self):
        self.canvas.delete(tk.ALL)

# MAIN
aplicacion1 = Aplicacion()