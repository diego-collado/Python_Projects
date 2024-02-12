'''
Confeccionar una aplicación que permita introducir un entero por teclado y al presionar un botón muestre
dicho valor elevado al cuadrado en una Label.
'''
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Entrando valores")

        self.label1 = tk.Label(self.ventana, text="Introduce númnero: ")
        self.label1.grid(column=0, row=0)

        self.dato = tk.StringVar()#recoger datos que se introducen por teclado
        self.entrada = tk.Entry(self.ventana, width=10, textvariable=self.dato)
        self.entrada.grid(column=0, row=2)

        self.boton = tk.Button(self.ventana, text="Calcular cuadrado", command=self.calcular)
        self.boton.grid(column=0, row=5)

        self.label2 = tk.Label(self.ventana, text="Resultado")
        self.label2.grid(column=0, row=8)

        self.ventana.mainloop()

    def calcular(self):
        valor = int(self.dato.get())#método para poder recoger el valor del "input" que hemos marcado como entrada
        cuadrado = valor * valor
        self.label2.configure(text=cuadrado)#en label2, le ponemos el resultado "a capón"

#MAIN
app = Aplicacion()