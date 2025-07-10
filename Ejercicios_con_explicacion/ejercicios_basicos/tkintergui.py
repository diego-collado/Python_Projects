'''
Tkinter es la biblioteca para crear GUIs con Python. Características:
    · Totalmente FREE
    · Existen otras como PyGTK, PyQT5, Kivy, wxPython, PySimpleGUI,
    Libavg, PyForms, PySide2, Cera, PyGUI...
    · Viene instalado en las últimas versiones de Python
---------------------------------------
-- -- -- EXPLICACIÓN PRINCIPAL -- -- --
---------------------------------------

# Tkinter actúa como un framework (tiene lenguaje propio)

import tkinter as tk # se utiliza un alias para no tener que poner tkinter cada vez que utilicemos la biblioteca

# Diseño de ventana principal - Sencillito (de andar por casa)

ventana = tk.Tk() # con esta llamada a la clase, creamos un objeto de tipo TK
ventana.title("- - Mi superaplicación - -") # ponemos un título
ventana.geometry("300x200") # tamaño de la ventana
ventana.mainloop() # para que aparezca (se ejecute) la ventana

# Diseño de ventana principal - Para vosotr@s, que sois PROs
class Aplicacion:
    # Constructor
    def __init__(self):
        self.ventana1 = tk.Tk() # creamos el objeto TK
        self.ventana1.title("Hola mundo")
        self.ventana1.mainloop()

app = Aplicacion() # llamada a la clase
'''
# IMPORT ----------------------------------------------------------
import tkinter as tk

# CLASS -----------------------------------------------------------
class Aplicacion:
    # Constructor
    def __init__(self):
        # variables globales de la ventana
        self.valor = 1

        # construcción de la ventana ··········································
        self.ventana = tk.Tk()
        self.ventana.title("IncremenDecrementador")

        # Pido los datos (si es necesario) ····································
        self.pedir = tk.Label(self.ventana, text="Introduce número: ")
        self.pedir.grid(column=3, row=2)
        self.dato = tk.StringVar() # guardamos el dato como tal

        self.seleccion = tk.IntVar()
        self.seleccion.set(2)

        self.selec1 = tk.IntVar()
        self.selec2 = tk.IntVar()
        self.selec3 = tk.IntVar()
        self.selec4 = tk.IntVar()
        
        # casillas de selección - checkbox ···································
        self.check_lenguaje1 = tk.Checkbutton(self.ventana, text="Python", variable=self.selec1)
        self.check_lenguaje1.grid(column=5, row=0)
        self.check_lenguaje2 = tk.Checkbutton(self.ventana, text="C/C++", variable=self.selec2)
        self.check_lenguaje2.grid(column=5, row=1)
        self.check_lenguaje3 = tk.Checkbutton(self.ventana, text="Ruby on Rails", variable=self.selec3)
        self.check_lenguaje3.grid(column=5, row=2)
        self.check_lenguaje4 = tk.Checkbutton(self.ventana, text="R", variable=self.selec4)
        self.check_lenguaje4.grid(column=5, row=3)

        self.mostrar_seleccion2 = tk.Button(self.ventana, text="Verificar", command=self.verificar)
        self.mostrar_seleccion2.grid(column=5, row=4)

        self.etiqueta4 = tk.Label(self.ventana, text="Cantidad:  ")
        self.etiqueta4.grid(column=5, row=7)

        # botones tipo radio - radiobuttons ··································
        self.radio_varon = tk.Radiobutton(self.ventana, text="Hombre", variable=self.seleccion, value=1)
        self.radio_varon.grid(column=4, row=1)

        self.radio_hembra = tk.Radiobutton(self.ventana, text="Mujer", variable=self.seleccion, value=2)
        self.radio_hembra.grid(column=4, row=2)

        self.mostrar_seleccion = tk.Button(self.ventana, text="Mostrar selección", command=self.mostrarSeleccion)
        self.mostrar_seleccion.grid(column=4, row=3)


        # label - etiqueta ····················································
        self.etiqueta1 = tk.Label(self.ventana, text=self.valor) # creamos el objeto
        self.etiqueta1.grid(column=0, row=0) # colocamos la etiqueta en una rejilla
        self.etiqueta1.configure(foreground="red") # fondo del texto

        self.etiqueta2 = tk.Label(self.ventana, text="Resultado") # creamos el objeto
        self.etiqueta2.grid(column=3, row=0) # colocamos la etiqueta en una rejilla
        self.etiqueta2.configure(foreground="blue") # fondo del texto

        self.etiqueta3 = tk.Label(self.ventana, text="Selección") # creamos el objeto
        self.etiqueta3.grid(column=4, row=5) # colocamos la etiqueta en una rejilla
        self.etiqueta3.configure(foreground="black") # fondo del texto

        # entry - inputs  ······················································
        self.input1 = tk.Entry(self.ventana, width=20, textvariable=self.dato)
        # input que permite recoger el dato que se ha de ingresar
        self.input1.grid(column=3, row=3)

        # button - botón ·······················································
        self.boton_inc = tk.Button(self.ventana, text="Incrementar", command=self.incrementar)
        #self.nombreBotón = tk.Button(dónde, qué texto lleva, qué ejecuta)
        self.boton_inc.grid(column=0, row=1)

        self.boton_dec = tk.Button(self.ventana, text="Decrementar", command=self.decrementar)
        self.boton_dec.grid(column=0, row=2)

        self.resultado = tk.Button(self.ventana, text="Calcular cuadrado", command=self.calcularCuadrado)
        self.resultado.grid(column=3, row=4)

        # otras opciones
        #self.ventana.resizable(False,False)
        # evitamos que nos hagan reescalado de la ventana

        # Ejecución de la ventana
        self.ventana.mainloop()

        # Métodos
    def incrementar(self):
        self.valor = self.valor + 1
        self.etiqueta1.config(text=self.valor)
        # "mandamos" el valor a su sitio

    def decrementar(self):
        self.valor = self.valor - 1
        self.etiqueta1.config(text=self.valor)

    def calcularCuadrado(self):
        valor = int(self.dato.get()) # pedimos datos
        self.ventana.title(self.dato.get()) # aparece el número que introduzco en la barra de títulos
        cuadrado = valor * valor
        self.etiqueta2.configure(text=cuadrado)

    def mostrarSeleccion(self):
        if self.seleccion.get() == 1:
            self.etiqueta3.configure(text="Es un CHiCo")
        if self.seleccion.get() == 2:
            self.etiqueta3.configure(text="Es una CHiCa")
    
    def verificar(self):
        cant = 0
        if self.selec1.get() == 1:
            cant += 1
        if self.selec2.get() == 1:
            cant += 1
        if self.selec3.get() == 1:
            cant += 1
        if self.selec4.get() == 1:
            cant += 1
        
        self.etiqueta4.configure(text=f"Cantidad: {cant}")


# MAIN -------------------------------------------------------------
app = Aplicacion()