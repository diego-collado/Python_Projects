'''
10.- Cargar una oración por teclado.
Mostrar luego cuantos espacios en blanco se ingresaron. Tener en cuenta que un espacio en blanco es igual a
" ", en cambio una cadena vacía es ""
'''
espacios = 0

frase = str(input("Introduce una frase: "))
for i in frase:
    if i == " ":#cuando el caracter en el que estoy sea un espacio, entro en el condicional
        espacios += 1
print(espacios)