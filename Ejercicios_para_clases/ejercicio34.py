'''
Crear 2 objetos de la clase Button con las etiquetas: "chico" y "chica"
Al presionarse el botón, mostrar en la barra de títulos de la ventana la etiqueta del botón presionado
'''

import tkinter as tk

class Aplicacion:

    #creación e inicialización de ventana/etiqueta/botones
    def __init__(self):
        #Ventana principal (la hemos llamado Ventana1)
        self.ventana1 = tk.Tk()#llamada para creación de ventana
        self.ventana1.title("Cambiando títulos")#título de la ventana

        #Button (botón) que hemos llamada boton1 y boton2
        self.boton1 = tk.Button(self.ventana1, text="Chico", command=self.chico)
        #nombre_boton = tk.claseBotón(dónde_lo_muestro, text="que texto pongo en el botón", command=lo_que_ejecuto)
        self.boton1.grid(column=0, row=1)

        self.boton2 = tk.Button(self.ventana1, text="Chica", command=self.chica)
        self.boton2.grid(column=0, row=2)

        #lanzamiento de ventana al sistema o monitor
        self.ventana1.mainloop()

    def chico(self):
        self.ventana1.title('Chico')

    def chica(self):
        self.ventana1.title('Chica')

#MAIN
aplicacionchunga = Aplicacion()