'''
Implementar un programa que permita introducir 2 números en controles de tipo Entry para, posteriormente,
sumar ambos valores ingresados y mostrar la suma en una Label al presionar un botón.
'''
import tkinter as tk

class App:
    def __init__(self):
        # Ventana
        self.ventana = tk.Tk()

        # Etiquetas decoración de valores
        self.etiquetaV1 = tk.Label(self.ventana, text="Introduce el primer valor: ")
        self.etiquetaV2 = tk.Label(self.ventana, text="Introduce el segundo valor: ")

        self.etiquetaV1.grid(column=0, row=0)
        self.etiquetaV2.grid(column=1, row=0)

        # Toma de datos
        self.dato1=tk.IntVar()
        self.entrada1 = tk.Entry(self.ventana, width=25, textvariable=self.dato1)
        self.entrada1.grid(column=0, row=1)

        self.dato2 = tk.IntVar()
        self.entrada2 = tk.Entry(self.ventana, width=25, textvariable=self.dato2)
        self.entrada2.grid(column=1, row=1)

        # Botón para obtener resultados
        self.boton = tk.Button(self.ventana, text="Sumar", command=self.sumar)
        self.boton.grid(column=0, row=4)

        self.resultado = tk.Label(self.ventana, text="Resultado")
        self.resultado.grid(column=0, row=5)

        # Llamada para arranque de ventana
        self.ventana.mainloop()
    def sumar(self):
        suma = self.dato1.get() + self.dato2.get()
        self.resultado.configure(text=suma)
#MAIN
apli = App()