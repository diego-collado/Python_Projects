'''5.- Un posible candidato a un empleo realiza un test de capacitación, se obtuvo la siguiente información:
    - cantidad total de preguntas que se le realizaron
    - cantidad de preguntas que contestó correctamente

Se pide confeccionar un programa que:
    - ingrese los dos datos por teclado
    - informe el nivel del porcentaje de respuestas correctas que ha obtenido:
        · Nivel máximo: Porcentaje>=90%
        · Nivel medio: Porcentaje>=75% y <90%
        · Nivel regular: Porcentaje>=50% y <75%
        · Fuera de nivel: Porcentaje<50%.
'''

preguntas = int(input("Introduce el número de preguntas: "))
correctas = int(input("Introduce el número de preguntas correctas: "))

porcentaje = (preguntas / correctas) * 100

if (porcentaje >= 90):
    print("Nivel máximo alcanzado")
elif (porcentaje >= 75) and (porcentaje < 90):
    print("Nivel medio alcanzado")
elif (porcentaje >= 50) and (porcentaje < 75):
    print("Nivel regulero alcanzado")
elif (porcentaje < 50) or (porcentaje > preguntas):
    print("Fuera de nivel de corrección, eRRoR")