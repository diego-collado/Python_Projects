'''
Programa que cree un objeto de la clase Canvas y muestre en el título de la ventana la coordenada actual del mouse
dentro del control Canvas y al presionar el botón izquierdo del mouse se dibuje un círculo en dicha posición.

Captura de otros eventos:
    - click derecho y tecla shift: self.canvas1.bind("<Shift Button-1>", self.presion_mouse)
    - click derecho y tecla control:self.canvas1.bind("<Control Button-1>", self.presion_mouse)
    - click izquierdo, teclas shift y control: self.canvas1.bind("<Control Shift Button-1>", self.presion_mouse)
    - click izquierdo, teclas alt, shift y control: self.canvas1.bind("<Control Shift Alt Button-1>", self.presion_mouse)
    - si se sale el ratón de la ventana: self.canvas1.bind("<Leave>", self.salida)
    - doble click izquierdo: self.canvas1.bind("<Double-Button-1>", self.presion_mouse)
'''
#IMPORTS
import tkinter as tk

#CLASS
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()# creación de la ventana principal
        self.canvas = tk.Canvas(self.ventana, width=600, height=400, background="black") # donde se inicia Canvas
        self.canvas.bind("<Motion>", self.mover_mouse) # captura del movimiento
        self.canvas.bind("<Button-1>", self.presion_mouse) # captura del click del ratón
        self.canvas.grid(column=0, row=1)

        self.ventana.mainloop()


    def mover_mouse(self,evento):
        self.ventana.title(str(evento.x) + "-" + str(evento.y))
    def presion_mouse(self, evento):
        self.canvas.create_oval(evento.x-5, evento.y-5, evento.x+5, evento.y+5, fill="red")


#MAIN
aplicacion1 = Aplicacion()