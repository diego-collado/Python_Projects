'''
11.- HARDCORE: Tenemos que controlar que:
    - se introduzca una clave que no tenga ningún espacio en blanco
    - no contenga ninguna instrucción <script> o </script>
    - que esté entre 10 y 20 caracteres.
Implementar un código que repita la petición tantas veces como no se cumplan los aspectos que pedimos.
A utilizar, cualquier código, cualquier instrucción....
'''

def iniciar():
    clave = str(input("Introduzca una clave alfanumérica: "))
    comprobar(clave)

def comprobar(clave):
    for i in clave:
        print(clave)
        if i == " ":
            print("Lo sentimos, no se permiten espacios en las claves")
            iniciar()
        elif (i == "<") or (i == ">"):
            print("Lo sentimos, no se permite scripting")
            iniciar()
        elif (len(clave) < 10) or (len(clave) > 20):
            print("Lo sentimos, la longitud debe estar entre 10 y 20")
            iniciar()
        else:
            print("Clave introducida válida, saliendo de la BBDD")
            break


#MAIN
iniciar()
