'''
Crear y cargar una lista con 5 enteros por teclado.
Implementar un algoritmo que identifique el menor valor de la lista y la posición donde se encuentra.
'''

numeros = []
for i in range(5):
    valor = int(input("Introduce valor: "))
    numeros.append(valor)

print("Número más grande: ",max(numeros))
print("Número más pequeño: ",min(numeros))
#Yo paso un objeto números, el cual contiene muchos elementos... Tú te encargas de decirm el más grande o pequeño