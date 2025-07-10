'''
Con tres listas de palabras (sujetos, verbos, objetos), genera frases
aleatorias, siempre combinando elementos de cada lista.
'''
# IMPORTS ------------------------------------------
import random

# Listas de palabras
sujetos = ["Mi gato","El coche", "Perico", "Ruperta","Mendrugo"]
verbos = ["madruga","enseña","rompe","conduce","juego al badminton"]
objetos = ["con una pera","con una pelota","un camión", "un ratón"]

# El máximo de frase que se van a generar de forma aleatoria
num_frases = 5

print("Estas son las frases inventadas por la IA:\n\n")

for i in range(num_frases):
# cada uno de los elementos de cada una de las listas
    sujeto = random.choice(sujetos)
    verbo = random.choice(verbos)
    objeto = random.choice(objetos)
    
    #frase = random.choice(sujetos, verbos, objetos) no se puede utilizar

    '''
    Con random.shuffle(sujetos) no va bien.
    random.shuffle(verbos)
    random.shuffle(objetos)
    sujeto = random.choice(sujetos)
    verbo = random.choice(verbos)
    objeto = random.choice(objetos)'''

    print(f"{sujeto} {verbo} {objeto}\n\n")
    #print(frase)
    