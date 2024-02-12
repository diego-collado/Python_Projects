'''
EXPLICACIÓN TKINTER: paquete que se dedica a las GUI (Graphic User Interface) en Python.
Está integrado en Python.
'''

'''#Hola mundo, versión fácil
import tkinter as tk

ventana1 = tk.Tk()#llamada a clase Tk (por lo tanto, toda el paquete está en POO)
ventana1.title("¡¡Hola mundo mundial!!")#creación de un título de ventana

ventana1.mainloop()#loquesea.mainloop() se utilizar para llamar a la ventana desde mi monitor

#Hola mundo, versión App con clases y orientada a objetos
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Hola, olita, olaza!!")
        self.ventana1.mainloop()

app = Aplicacion()'''

'''#Ventana con BUTTON y LABEL
import tkinter as tk

class Aplicacion:

    #creación e inicialización de ventana/etiqueta/botones
    def __init__(self):
        #Ventana principal (la hemos llamado Ventana1)
        self.valor = 1
        self.ventana1 = tk.Tk()#llamada para creación de ventana
        self.ventana1.title("Controles de BUTTON y LABEL")#título de la ventana

        #Label (etiqueta o texto) que hemos llamado Label1
        self.label1=tk.Label(self.ventana1, text=self.valor)#creación de objeto que variará su valor
        self.label1.grid(column=0, row=0)#como tenemos muchas formas de pintar en el monitor, utilizamos un grid (rejilla)
        self.label1.configure(foreground="red")#cambiamos el color de fondo de ese valor, es decir, el color de la fuente que nos muestra el valor

        #Button (botón) que hemos llamada boton1 y boton2
        self.boton1 = tk.Button(self.ventana1, text="Incrementar valor ++", command=self.incrementar)
        #nombre_boton = tk.claseBotón(dónde_lo_muestro, text="que texto pongo en el botón", command=lo_que_ejecuto)
        self.boton1.grid(column=0, row=1)

        self.boton2 = tk.Button(self.ventana1, text="Decrementar valor --", command=self.decrementar)
        self.boton2.grid(column=0, row=2)

        #lanzamiento de ventana al sistema o monitor
        self.ventana1.mainloop()

    def incrementar(self):
        self.valor = self.valor + 1
        self.label1.config(text=self.valor)

    def decrementar(self):
        self.valor = self.valor - 1
        self.label1.config(text=self.valor)

#MAIN
aplicacionchunga = Aplicacion()'''

'''#Creando ventanas padre e hijas
import tkinter as tk

ventana = tk.Tk()
ventana.title("Ventana Padre")

ventanaHija = tk.Toplevel(ventana)
ventanaHija.title("Ventana Hija")

etiqueta = tk.Label(ventanaHija, text="Ejemplo de transient")
etiqueta2 = tk.Label(ventanaHija, text="Ejemplo de transient 2")
etiqueta.pack()#mostrar etiqueta. Se puede utilizar pady para márgenes, igual que en HTML/CSS
etiqueta2.pack()

etiqueta.grid(row=1, column=0)
etiqueta2.grid(row=4, column=0

#Posicionando las ventanas
ventana.geometry("400x400+100+100")
ventanaHija.geometry("200x200+150+150")


ventanaHija.transient(ventana)
ventana.mainloop()'''

'''
CheckButton: botón con 2 estados, conocido por el público como cuadro de selección--------------------------


import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        # Construcción de CheckButtons ------------------------------------------------------------------
        # toma de valores
        self.select1 = tk.IntVar()
        self.select2 = tk.IntVar()
        self.select3 = tk.IntVar()
        self.select4 = tk.IntVar()

        # construyendo los checkbutton en la pantalla
        self.checkbutt1 = tk.Checkbutton(self.ventana, text="Python", variable=self.select1)
        self.checkbutt2 = tk.Checkbutton(self.ventana, text="HTML + CSS", variable=self.select2)
        self.checkbutt3 = tk.Checkbutton(self.ventana, text="JS", variable=self.select3)
        self.checkbutt4 = tk.Checkbutton(self.ventana, text="PHP", variable=self.select4)

        # pintando el checkbutton real en la pantalla
        self.checkbutt1.grid(column=0, row=0)
        self.checkbutt2.grid(column=0, row=1)
        self.checkbutt3.grid(column=0, row=2)
        self.checkbutt4.grid(column=0, row=3)

        # Construcción de CheckButtons para verificación ------------------------------------------------
        self.botonVerificar = tk.Button(self.ventana, text="Verificar", command=self.verificar)
        self.botonVerificar.grid(column=0, row=5)

        # Contrucción de etiqueta -----------------------------------------------------------------------
        self.etiqueta = tk.Label(self.ventana, text="Cantidad")
        self.etiqueta.grid(column=0, row=6)


        self.ventana.mainloop()

    def verificar(self):
        cantidad = 0

        if (self.select1.get() == 1):
            cantidad += 1
        if (self.select2.get() == 1):
            cantidad += 1
        if (self.select3.get() == 1):
            cantidad += 1
        if (self.select4.get() == 1):
            cantidad += 1

        self.etiqueta.configure(text="Cantidad: " + str(cantidad))

#MAIN
app1 = Aplicacion()'''

'''
ListBox: lista de items
'''

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        # Construcción de ListBox -----------------------------------------------------------
        '''self.lista = tk.Listbox(self.ventana) # lista para 1 única selección'''
        self.lista = tk.Listbox(self.ventana, selectmode=tk.MULTIPLE) # lista con múltiples selecciones
        self.lista.grid(column=0, row=0)

        # Construcción del scroll vertical
        self.scroll_lista = tk.Scrollbar(self.ventana, orient=tk.VERTICAL)# es scroll en Y, vertical
        self.scroll_lista.configure(command=self.lista.yview) # vista en vertical
        self.scroll_lista.grid(column=1, row=0, sticky='NS')# desde Norte hasta Sur (orientación vertical)

        self.lista.insert(0, "BMW")
        self.lista.insert(1, "Mercedes")
        self.lista.insert(2, "Lexus")
        self.lista.insert(3, "Volkswagen")
        self.lista.insert(4, "Mitsubishi")
        self.lista.insert(5, "Abarth")
        self.lista.insert(6, "Alfa Romeo")
        self.lista.insert(7, "Ferrari")
        self.lista.insert(8, "Lamborghini")
        self.lista.insert(9, "Pagani")
        self.lista.insert(10, "McLaren")
        self.lista.insert(10, "Rolls Royce")
        self.lista.insert(10, "Lamborghini")



        # Contrucción de botón Recuperar ---------------------------------------------------
        self.boton = tk.Button(self.ventana, text="Recuperar", command=self.recuperar)
        self.boton.grid(column=0, row=1)

        self.etiqueta = tk.Label(self.ventana, text="Seleccionado: ")
        self.etiqueta.grid(column=0, row=2)

        self.ventana.mainloop()

    # método para el botón recuperar -----------------------------------------------------
    '''def recuperar(self): # recuperación de 1 único valor - - - - - - 
        # comprobamos que la lista ha sido pulsada y que está un valor seleccionado
        # esta lo logramos sabiendo que la longitud es >0
        if (len(self.lista.curselection()) != 0):
            self.etiqueta.configure(text=self.lista.get(self.lista.curselection()[0]))
            # retorna una tupla con las posiciones seleccionadas en la lista desplegable
            # al ser una lista, solo se permite un única selección, la posición [0]
    '''
    def recuperar(self):# recuperación de múltiples valores - - - - - - -
        if(len(self.lista.curselection()) != 0):
            selecciones = ''

            for posicion in self.lista.curselection():
                selecciones += self.lista.get(posicion) + "\n"
            self.etiqueta.configure(text=selecciones)

#MAIN
app1 = Aplicacion()