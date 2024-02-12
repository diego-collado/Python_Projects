'''
8.-Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo.
Ordenar alfabéticamente e imprimir los resultados.
Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente.
'''

paises = []
habitantes = []

#Bloque de petición de datos
for i in range(5):
    nombre_pais = str(input("Introduce el nombre del país: "))
    habitantes_pais = int(input("Introduce el número de habitantes (M): "))

#Se añade cada petición a su correspondiente array (lista)
    paises.append(nombre_pais)
    habitantes.append(habitantes_pais)

#Bloque ordenación (método de la burbuja sin auxiliar, forma dinámica)
'''
array --> [posición 0][posición 1][posición 2][posición 3]
variable --> [auxiliar]
'''
# ordenamiento alfabético
#paises.sort()
for i in range(4):#bucle paises
    for j in range(4-i):#bucle habitantes
        if (paises[j] > paises[j + 1]):
            paises[j], paises[j + 1] = paises[j + 1], paises[j]
            habitantes[j], habitantes[j + 1] = habitantes[j + 1], habitantes[j]
#print(paises)
for i in range(5):
    print("País: {} - Nº habitantes: {}".format(paises[i],habitantes[i]))

print("###################################################################################")
# ordenamiento numérico
for i in range(4):#bucle paises
    for j in range(4-i):#bucle habitantes
        if (habitantes[j] < habitantes[j + 1]):
            paises[j], paises[j + 1] = paises[j + 1], paises[j]
            habitantes[j], habitantes[j + 1] = habitantes[j + 1], habitantes[j]

for i in range(5):
    print("País: {} - Nº habitantes: {}".format(paises[i],habitantes[i]))