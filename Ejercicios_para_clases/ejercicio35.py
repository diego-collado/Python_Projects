'''
Mostrar los botones del 1 al 5.
Cuando se presiona mostrar en una Label todos los botones presionados hasta ese momento.
'''

import tkinter as tk

class Aplicacion:

    #creación e inicialización de ventana/etiqueta/botones
    def __init__(self):
        self.datos = ""

        self.ventana1 = tk.Tk()  # llamada para creación de ventana
        self.ventana1.title("Botones & Valores")  # título de la ventana

        # Button (botón) que hemos llamada boton1, boton2...
        self.boton1 = tk.Button(self.ventana1, text="Botón 1", command=self.presion1)
        self.boton1.grid(column=0, row=0)
        self.boton2 = tk.Button(self.ventana1, text="Botón 2", command=self.presion2)
        self.boton2.grid(column=1, row=0)
        self.boton3 = tk.Button(self.ventana1, text="Botón 3", command=self.presion3)
        self.boton3.grid(column=2, row=0)
        self.boton4 = tk.Button(self.ventana1, text="Botón 4", command=self.presion4)
        self.boton4.grid(column=3, row=0)
        self.boton5 = tk.Button(self.ventana1, text="Botón 5", command=self.presion5)
        self.boton5.grid(column=4, row=0)

        # Label, que en este caso, nos mostrará los datos de clickado
        self.label1 = tk.Label(self.ventana1, text=self.datos)
        self.label1.grid(column=5, row=5)

        # Carga de la ventana en el monitor
        self.ventana1.mainloop()

    def presion1(self):
        self.datos = self.datos + " 1"
        self.label1.configure(text=self.datos)

    def presion2(self):
        self.datos = self.datos + " 2"
        self.label1.configure(text=self.datos)

    def presion3(self):
        self.datos = self.datos + " 3"
        self.label1.configure(text=self.datos)

    def presion4(self):
        self.datos = self.datos + " 4"
        self.label1.configure(text=self.datos)

    def presion5(self):
        self.datos = self.datos + " 5"
        self.label1.configure(text=self.datos)

#MAIN
App = Aplicacion()