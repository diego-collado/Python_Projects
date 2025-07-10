'''
Cosas que podemos hacer con los diccionarios: métodos BUILT-IN (Precocinados de Python)
'''

di1 = {'a':1, 'b':2}
di1.clear()# borra todo el contenido del diccionario

di2 = {'a':1, 'b':2}
print(di2.get('a')) # obtenemos el valor de una clave
print(di2.get('a','Error, no encontrado')) # obtenemos el valor de una clave, pero no existe, provoca error

print(di2.values()) # muestra los valores que tenga el diccionario, no las claves
print(di2.keys()) # muestra las claves, no los valores

di2.pop('a') # borra el elemento con clave a

#nombreDiccionario =  {clave:valor, clave:valor}
diccionario1 = {'a':10, 'b': 20}
diccionario2 = {'a':1, 'd': 210}
print(diccionario1)

diccionario1.update(diccionario2) # actualizamos el diccionario1 con el contenido diccionario2
print(diccionario1)

monedas = {} #inicialización y puesta a 0
monedas["Bitcoin"] = 65000 #en el diccionario monedas, introduce Bitcoin como clave y 65000 como valor
monedas["Litecoin"] = 650
print(monedas)