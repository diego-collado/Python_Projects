'''
Formularios CRUD:
    - lógica de presentación de datos
    - hace uso de otro archivo para la gestión de accesos a la BBDD
'''
#IMPORTS ------------------------------------------------------------------------------
import tkinter as tk

# importación de submódulos para gestión de ventanas, scroll y otros parámetros
from tkinter import ttk
from tkinter import messagebox as mb # más info: https://docs.python.org/es/3.9/library/tkinter.messagebox.html
from tkinter import scrolledtext as st

# importación de articulos.py (módulo externo)
import articulos

#CLASS ------------------------------------------------------------------------------
class FormularioArticulos:
    # método de inicialización de ventanas y otros parámetros (artículos)
    def __init__(self):
        # adquiriendo artículos
        self.articulo1 = articulos.Articulos()

        # parametrización de ventana & pestañas
        self.ventana1 = tk.Tk()
        self.ventana1.title("- . - Mantenimiento de artículos - . -")

        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)

        # llamadas a métodos
        self.carga_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrado()
        self.modificar()

        # "arranque" de la ventana
        self.ventana1.mainloop()

    # método de carga de artículos (alta de nuevos artículos)
    def carga_articulos(self):
        # parametrización de frames
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de artículos")

        self.labelFrame1 = ttk.LabelFrame(self.pagina1, text="Artículo")
        self.labelFrame1.grid(column=0, row=0, padx=5, pady=10)

        # labels
        self.label1 = ttk.Label(self.labelFrame1, text="Descripción")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.label2 = ttk.Label(self.labelFrame1, text="Precio")
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        # cargas
        self.descripcioncarga = tk.StringVar()
        self.preciocarga = tk.StringVar()

        # entrys
        self.entrydescripcion = ttk.Entry(self.labelFrame1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        self.entryprecio = ttk.Entry(self.labelFrame1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)

        # botón de confirmación para agregar el artículo
        self.boton1 = ttk.Button(self.labelFrame1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def agregar(self):
        datos = (self.descripcioncarga.get(), self.preciocarga.get())
        self.articulo1.alta(datos)

        # messagebox
        mb.showinfo("Información", "Los datos fueron cargados con éxito...")

        # datos
        self.descripcioncarga.set("")
        self.preciocarga.set("")

    # método de consulta de artículos por código
    def consulta_por_codigo(self):
        # parametrización de frames
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")

        self.labelFrame2 = ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelFrame2.grid(column=0, row=0, padx=5, pady=10)

        # label
        self.label1 = ttk.Label(self.labelFrame2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.label2 = ttk.Label(self.labelFrame2, text="Descripción:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.label3 = ttk.Label(self.labelFrame2, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)


        # cargas
        self.codigo = tk.StringVar()
        self.descripcion = tk.StringVar()
        self.precio = tk.StringVar()

        # entry
        self.entrycodigo = ttk.Entry(self.labelFrame2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.entrydescripcion = ttk.Entry(self.labelFrame2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.entryprecio = ttk.Entry(self.labelFrame2, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)

        # botón de confirmación para carga de consulta
        self.boton1 = ttk.Button(self.labelFrame2, text="Confirmar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos = (self.codigo.get(), )

        respuesta = self.articulo1.consulta(datos)# query a la BBDD

        # comprobación si tenemos respuesta o no, es decir, si se encuentra el artículo en la BBDD
        if (len(respuesta) > 0):
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set('')
            self.precio.set('')

            # messagebox
            mb.showerror("Información","No existe el artículo solicitado con el código introducido...")

    # método de listado completo de artículos (BBDD completa en principio)
    def listado_completo(self):
        # parametrización de frames
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado de artículos")

        self.labelFrame3 = ttk.LabelFrame(self.pagina3, text="Artículo")
        self.labelFrame3.grid(column=0, row=0, padx=5, pady=10)

        # botón de confirmación para carga de consulta completa
        self.boton1 = ttk.Button(self.labelFrame3, text="Listar completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)

        # scroll para el texto a listar
        self.scrolledtext1 = st.ScrolledText(self.labelFrame3, width=30, height=10)
        self.scrolledtext1.grid(column=0, row=1, padx=10, pady=10)

    def listar(self):
        respuesta = self.articulo1.recuperar_todos()

        self.scrolledtext1.delete("1.0", tk.END)
        # cada salto, se comienza en el punto en el que se quedó el puntero de lectura (tk.END)
        # el espacio por salto es de 1 unidad
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "código: " + str(fila[0]) +
                                      "\ndescripción: " + str(fila[1]) +
                                      "\nprecio: " + str(fila[2]) + "\n\n")

    # método de borrado de artículo
    def borrado(self):
        # parametrización de frames
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de artículos")

        self.labelFrame4 = ttk.LabelFrame(self.pagina4, text="Artículo")
        self.labelFrame4.grid(column=0, row=0, padx=5, pady=10)

        # label
        self.label1 = ttk.Label(self.labelFrame4, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        # cargas
        self.codigoborra = tk.StringVar()

        # entry
        self.entryborra = ttk.Entry(self.labelFrame4, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)

        # botón de confirmación para borrado del artículo
        self.boton1 = ttk.Button(self.labelFrame4, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos = (self.codigoborra.get(), )
        cantidad = self.articulo1.baja(datos)

        # messagebox
        if (cantidad == 1):
            mb.showinfo("Información", "Se borró el artículo con éxito...")
        else:
            mb.showerror("Información","No existe el artículo solicitado con el código introducido...")

    # método de modificación de artículos
    def modificar(self):
        # parametrización de frames
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar artículo")
        self.labelframe5 = ttk.LabelFrame(self.pagina5, text="Artículo")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)

        # label
        self.label1 = ttk.Label(self.labelframe5, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.label2 = ttk.Label(self.labelframe5, text="Descripción:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.label3 = ttk.Label(self.labelframe5, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)


        # cargas
        self.codigomod = tk.StringVar()
        self.descripcionmod = tk.StringVar()
        self.preciomod = tk.StringVar()

        # entry
        self.entrycodigo = ttk.Entry(self.labelframe5, textvariable=self.codigomod)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.entrydescripcion = ttk.Entry(self.labelframe5, textvariable=self.descripcionmod)
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.entryprecio = ttk.Entry(self.labelframe5, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)

        # botón de consulta y modificación
        self.boton1 = ttk.Button(self.labelframe5, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
        self.boton1 = ttk.Button(self.labelframe5, text="Modificar", command=self.modifica)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)

    def modifica(self):
        datos = (self.descripcionmod.get(), self.preciomod.get(), self.codigomod.get())
        cantidad = self.articulo1.modificacion(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Se modificó el artículo")
        else:
            mb.showerror("Información", "No existe un artículo con dicho código")

    def consultar_mod(self):
        datos = (self.codigomod.get(),)
        respuesta = self.articulo1.consulta(datos)
        if len(respuesta) > 0:
            self.descripcionmod.set(respuesta[0][0])
            self.preciomod.set(respuesta[0][1])
        else:
            self.descripcionmod.set('')
            self.preciomod.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")


# ARRANQUE APP ------------------------------------------------------------------------------
aplicacion1 = FormularioArticulos()