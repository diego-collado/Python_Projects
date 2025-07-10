'''
Son casi iguales a las listas, pero de tipo INMUTABLE, es decir, no pueden ser modificadas 
una vez se declaren, pero se declaran más o menos igual que las listas.
'''

tupla = (1,2,3)
print(tupla)
print(type(tupla))
print(tupla[0])

#semana = ("lunes","martes","miércoles", "jueves", "viernes",(1,2,3))
#tupla[2]  = "Volvo"
#tupla.append ("Volvo")

#for dia in semana:
    #print(dia)

#### MÉTODOS PARA PODER UTILIZAR LAS TUPLAS CORRECTAMENTE ####
semana = ("lunes","martes","miércoles", "jueves", "lunes")
print("Cuantos:", semana.count("lunes")) # cuenta los elementos que tenemos con el mismo contenido
print("Dónde:", semana.index("lunes")) # busca el contenido y devuelve la posición donde la encontró
#Si no lo encuentra, devuelve ValueError

print("Dónde:", semana.index("lunes",2)) # revisa a ver si está el texto a partir de la posición que quieras