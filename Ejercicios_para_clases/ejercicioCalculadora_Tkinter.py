'''
Crear una calculadora con las siguientes operaciones:
    - suma
    - resta
    - multiplicación
    - división
El resultado se deberá mostrar en un Label1

DECLARACIÓN DE VARIABLES EN TKINTER ---------------------------------------------------------
Las variables de control, se declaran de la siguiente forma:
    - enteros: IntVar()
    - flotantes: DoubleVar()
    - cadenas: StringVar()
    - booleanos: BooleanVar()

Inicialización de variables:

    blog = StringVar(value="Lo que se nos ocurra en este momento")

Métodos que podemos utilizar para este tipo de variables--------------------------------------
    · MÉTODO SET --> asignamos un valor a la variable de control, es decir, se utiliza para modificar
    el valor o estado de nuestros widgets.

    EJEMPLOS PRÁCTICOS:
        nombre = StringVar()
            --> Ahora, introducimos el valor --> nombre.set("El texto que quiera")
                                             --> blog = tk.Entry(ventana, textvariable=nombre, width=25)

        id_articulo = IntVar()
            --> Ahora, introducimos el valor --> id_articulo.set(1)
                                             --> articulo = tk.Label(Ventana, textvariable=id_articulo)

    · MÉTODO GET --> obtenemos el valor que tenga una variable en un momento dado de la vida de la aplicación.
    Se utiliza normalmente a la hora de leer el valor del control.

    EJEMPLOS PRÁCTICOS:
        print("Blog:", nombre.get())
        print("ID. Artículo:", id_articulo.get())

------------------------------------------------------------------------------------------------
1º.- SE PINTAN LOS INPUT, ES DECIR, LAS CAJAS QUE RECOGEN LOS DATOS
2º.- A CADA INPUT, LE CORRESPONDE UN LABEL, QUE NO ES MÁS QUE UNA ETIQUETA CON TÍTULO
3º.- SE CREAN LOS BOTONES, ASIGNANDO UN MÉTODO A CADA BOTÓN DE CLASE BUTTON (+, -, *, /...)
4º.- SE CREAN LOS MÉTODOS QUE NOS AYUDARÁN A MANEJAR LA CALCULADORA.
    DENTRO DE LOS MÉTODOS, TENEMOS QUE HACER UN GETTER, ES DECIR, RECOGER EL VALOR QUE SE INTRODUJO EN LOS INPUTS
5º.- SE PINTA EL RESULTADO EN LA PANTALLA

'''
#IMPORTS
import tkinter as tk

#CLASS
class Calculadora:
    def __init__(self):
        # Ventana principal (Padre)---------------------------------------------------------------
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora Científica Básica")

        # Primer valor----------------------------------------------------------------------------
        # Pintando en el monitor (etiqueta antes del input) - - - - - - - -
        self.label1 = tk.Label(self.ventana, text="Introduce primer valor: ")
        self.label1.grid(column=0, row=0)
        # Recogiendo el dato de un input - - - - - - - -
        self.dato1 = tk.IntVar()  # recoger datos que se introducen por teclado
        self.entrada1 = tk.Entry(self.ventana, width=10, textvariable=self.dato1)
        # Pintando en el monitor (input) - - - - - - - - - - - - - - - - - -
        self.entrada1.grid(column=2, row=0)

        # Segundo valor
        self.label2 = tk.Label(self.ventana, text="Introduce segundo valor: ")
        self.label2.grid(column=0, row=3)
        self.dato2 = tk.IntVar()  # recoger datos que se introducen por teclado
        self.entrada2 = tk.Entry(self.ventana, width=10, textvariable=self.dato2)
        self.entrada2.grid(column=2, row=3)

        # Resultado
        self.label3 = tk.Label(self.ventana, text="Resultado")
        self.label3.grid(column=0, row=8)


        # Creación de botones para las operaciones
        self.boton_sumar = tk.Button(self.ventana, text="+", command=self.suma)
        self.boton_sumar.grid(column=0, row=4)
        self.boton_restar = tk.Button(self.ventana, text="-", command=self.resta)
        self.boton_restar.grid(column=1, row=4)
        self.boton_multiplicar = tk.Button(self.ventana, text="x", command=self.multiplicacion)
        self.boton_multiplicar.grid(column=2, row=4)
        self.boton_dividir = tk.Button(self.ventana, text="/", command=self.division)
        self.boton_dividir.grid(column=3, row=4)


        self.ventana.mainloop()

    def suma(self):
        valor = self.dato1.get() + self.dato2.get()
        self.label3.configure(text=valor)

    def resta(self):
        valor = self.dato1.get() - self.dato2.get()
        self.label3.configure(text=valor)

    def multiplicacion(self):
        valor = self.dato1.get() * self.dato2.get()
        self.label3.configure(text=valor)

    def division(self):
        valor = self.dato1.get() / self.dato2.get()
        self.label3.configure(text=valor)

#MAIN
calculadora = Calculadora()