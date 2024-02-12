'''
Comprobación si hemos introducido o no un email por teclado


mail = str(input("Introduce el email: "))
if ("@" not in mail):
    print("Deja de hacer el tonto e inserta un email!!")
else:
    print("Genial, es un email!!")'''

mail = str(input("Introduce el email: "))
if "@" in mail:#in, nos da TRUE si está contenido, FALSE si no lo está
    print("OK")
else:
    print("Error")
'''
Se utiliza principalmente para strings o saber si se contienen elementos en un array

IN --> QUE ESTÁ PRESENTE ---> IF --> SE CUMPLE CONDICIÓN
NOT IN --> QUE NO ESTÁ PRESENTE --> ELSE --> NO SE CUMPLE CONDICIÓN
'''