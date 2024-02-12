'''
Tkinter Modo PRO:

Panel de pestañas: realmente es una división de la propia ventana, de modo que podemos tener X botones en la
pestaña 1, varios label/getters en otra y así...
'''
#IMPORTS
import tkinter as tk
from tkinter import ttk # https://docs.python.org/es/3.10/library/tkinter.ttk.html

#CLASS
class App(ttk.Frame): # Frame --> lo mismo que agrupación/grupo de elementos (botones, inputs...)

    def __init__(self, ventana_principal):
        # Tomamos los valores de la ventana que hemos envíado a la función -------
        super().__init__(ventana_principal)
        ventana_principal.title("Panel de pestañeo")

        # Creación de panel de pestañas ------------------------------------------
        self.panel_pestanna = ttk.Notebook(self)

        # Creación del contenido de cada pestaña ---------------------------------
        self.etiqueta_web = ttk.Label(self.panel_pestanna, text="kobalto.es")
        self.etiqueta_foro = ttk.Label(self.panel_pestanna, text="underc0de.org/foro")

        # Añadiendo pestañas al panel con su respectivo texto --------------------
        self.panel_pestanna.add(self.etiqueta_web, text="Web", padding=20)
        self.panel_pestanna.add(self.etiqueta_foro, text="Foro", padding=20)

        self.panel_pestanna.pack(padx=10, pady=10)
        self.pack()

#MAIN
ventana_principal = tk.Tk() # Creación de ventana principal fuera del Class
app = App(ventana_principal)
app.mainloop()