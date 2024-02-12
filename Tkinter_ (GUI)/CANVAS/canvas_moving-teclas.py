'''
Programa que moverá un cuadrado construido en Canvas que se moverá con las teclas de flecha:
    - desplamiento de X píxels
    - movimiento según la flecha seleccionada
'''
# IMPORTS
import tkinter as tk

# CLASS
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()  # determinar la creación de la ventana

        # creación del área Canvas
        self.canvas = tk.Canvas(self.ventana, width=600, height=400, background="pink")
        self.canvas.grid(column=0, row=0)

        # creación del elemento dentro del área Canvas
        self.cuadrado = self.canvas.create_rectangle(150,10,200,60, fill="blue")

        # controlando eventos: teclas
        self.ventana.bind("<KeyPress>", self.presionaTeclas)

        self.ventana.mainloop() # arranque de ventana y área Canvas

    def presionaTeclas(self,evento):
        if evento.keysym == 'Right':
            self.canvas.move(self.cuadrado, 5, 0)
        if evento.keysym == 'Left':
            self.canvas.move(self.cuadrado, -5, 0)
        if evento.keysym == 'Down':
            self.canvas.move(self.cuadrado, 0, 5)
        if evento.keysym == 'Up':
            self.canvas.move(self.cuadrado, 0, -5)

# MAIN
aplicacion1 = Aplicacion()