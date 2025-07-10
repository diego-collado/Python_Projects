'''
ESTRUCTURAS DE CONTROL DEL FLUJO DEL PROGRAMA
'''
'''
# CONDICIONALES # ---------------------------------------------
a = 48

# Condicional simple
if a > 5:
    print("A tiene dentro: ",a)

# Condicional un poco "menos" simple
if a > 5 and 47 <a: # X condición y Y condición se deben cumplir
    # a > 5 or 47 < a nos permite ejecurar sólo una de las 2
    print("A tiene dentro: ",a)

# Condicionales programados de otras maneras diferentes
# Con una instrucción 
if a > 5 and 47 <a: print("A tiene dentro: ",a)
# Con más de una instrucción
if a > 5 and 47 <a: print("A tiene dentro: ",a); print("Chauuuu")

# Usamos la versión del "y si no..."
# si ..., sino si... hasta que tienes la opción y si no, pues nada.

algo = 'a'

if algo == 'a':
    print("La X es un 5")
elif algo == 'b':
    print("La X es un 6")
elif algo == 'c':
    print("La X es un 7")
else:
    print("Error técnico...")

# Operador ternario: 
# [código si se cumple] if [condición] else [si no se cumple]

if algo == 'a':
    print("La X es un 5")
else:
    print("Error técnico...")

# modo operador ternario
print ("Es 5" if algo == 5 else "No es 5")

a = 10
b = 5
c = a/b if b != 0 else -1
print(c)

# BUCLES FOR # ---------------------------------------------
# for no tiene condiciones como while... Es un bucle más efectivo

for i in range(0,5):# for un_contador desde 0 hasta 5...
    print(i)

for i in "Python":
    print(i)

# Ejemplito de bucle anidado
for i in range(0,10):
    print(i)
    for j in "Python":
        print(j)

# for itera "al derecho"... Veamos "al revés"
texto = "Python"
for i in texto[::-1]:
    print(i)

# Iteramos de modo que vaya elemento sí - elemento no
texto = "Python"

for i in texto[::2]:
    print(i)

# RANGE # ---------------------------------------------
# range(inicio, fin, salto)
for i in range(5, 20, 2):#empieza en 5, hasta 20, contando de 2 en 2
    print(i)

for j in range(20, 0, -1):
    print(j)

# WHILE # ---------------------------------------------
print("Bucle superchulo...")
contador = 10

while contador > 0:
    print(contador)
    contador -= 1 # contador = contador -1

# SWITCH (Python >= 3.10) # ---------------------------------------------
opcion = input("Elige fruta: (1) Fresa - (2) Melón - (3) Plátano: \n")

match opcion:
    case "1": 
        print ("\n\nElegiste Fresa")
    case "2": 
        print ("\n\nElegiste Melón without jamón")
    case "3": 
        print ("\n\nElegiste Plátano")
    case _: # Y si no, todo lo que sea diferente a  lo anterior...
        #_ es el valor no capturado... es un comodín
        # default: print(...)
        print ("\n\nUpss... Esta fruta no es de por aquí...")
'''
mes = int(input("Introduce el número del mes del año: "))
match mes:
    case 12 | 1 | 2: print("Invierno")
    case 3 | 4 | 5: print("Primavera")
    case 6 | 7 | 8: print("Verano")
    case 9 | 10 | 11: print("Otoño")
    case _: print("Error... Hemos dicho 12 meses...")