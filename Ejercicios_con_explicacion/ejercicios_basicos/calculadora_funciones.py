'''
Calculadora creada con funciones

NOTAS:
--------------------------------------------------------------------------
if __name__ == "__main__":
    main()

Esto significa que este archivo se ejecuta SIEMPRE Y CUANDO sea un archivo principal, 
es decir, que no lo hayamos importado desde fuera.

__name__ es una variable especial que indica el nombre del módulo (archivo) actual

'''

# FUNCTIONS -----------------
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1,num2):
    if (num2 == 0):
        return "Error: se ha divido entre 0, es inviable"
    return num1/num2

def mostrarMenu():
    print("CALCULADORA CASI CIENTÍFICA")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Salir")

def main():
    while True:
        # 1.- Mostramos el menú
        mostrarMenu()# llamada a la función que se encarga de imprimir el menú en pantalla
        
        #2.- Solicitamos que se elija una opción
        opcion = input("Elige tu opción (1-5):  ")

        if (opcion == '5'):
            print("...Saliendo de la calculadora...")
            break

        #3.- Introducir los números para poder realizar la operación
        try:
            num1 = float(input("Introduce el primer número:  "))
            num2 = float(input("Introduce el segundo número:  "))
        except ValueError: #ValueError es un error contemplado por Python
            print("Entrada inválida... Intentaló de nuevo...")
            continue # para salir de esta parte y continuar con el resto del programa
        
        #4.- Realizar la operación seleccionada
        if (opcion == '1'):
            resultado = sumar(num1,num2) #en resultado se guarda lo retornado de la función
        
        elif (opcion == '2'):
            resultado = restar(num1,num2) 

        elif (opcion == '3'):
            resultado = multiplicar(num1,num2)

        elif (opcion == '4'):
            resultado = dividir(num1,num2)
        
        else:
            print("Opción seleccionada no válida....")
            continue

        #5.- Imprimimos el resultado en pantalla
        print(f"Resultado = {resultado}\n")

# MAIN ----------------------
if __name__ == "__main__":
    main() # función con toda la lógica del programa