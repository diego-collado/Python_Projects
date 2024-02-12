'''
Captura de eventos: moviendo figuras con ratón
'''

# IMPORTS
import tkinter as tk

# CLASS
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk() # determinar la creación de la ventana

        # creación del área Canvas
        self.canvas = tk.Canvas(self.ventana, width=900, height=500, background="pink")
        self.canvas.grid(column=0, row=0)

        # determinación de los archivos de trabajo (imágenes)
        archivo1 = tk.PhotoImage(file="carta1.png")
        self.canvas.create_image(30,100,image=archivo1, anchor="nw", tags="movil")
        archivo2 = tk.PhotoImage(file="carta2.png")
        self.canvas.create_image(400, 100, image=archivo2, anchor="nw", tags="movil")

        # acciones con botones del ratón en elementos Canvas
        self.canvas.tag_bind("movil", "<ButtonPress-1>", self.presionBoton)
        self.canvas.tag_bind("movil", "<Button1-Motion>", self.mover)

        # controlando otros elementos
        self.carta_seleccionada = None

        self.ventana.mainloop()# arranque de la ventana y demás elementos

    def presionBoton(self, evento):
        carta = self.canvas.find_withtag(tk.CURRENT) # seleccionamos la carta que se esté clickando en el área Canvas
        self.carta_seleccionada = (carta, evento.x, evento.y) # datos de la carta escogida y sus coordenadas

    def mover(self, evento):
        x, y = evento.x, evento.y # datos del movimiento a la carta
        carta, x1, y1 = self.carta_seleccionada
        self.canvas.move(carta, x - x1, y - y1) # movimiento de la carta
        self.carta_seleccionada = (carta, x, y) # carta nueva

# MAIN
aplicacion1 = Aplicacion()