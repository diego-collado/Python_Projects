'''
La pareja del año: TRY-EXCEPT

Si se maltraduce, es un intenta el código siempre y cuando no haya X 
condiciones, es decir, a excepción de X casos.
Excepción puede ser:
    · error         · evento X           · interrupción del sistema
    · división 0    · algo inexistente   · manejo de archivos no existentes
    · tipo dato incorrecto o mal formado · índices fuera de rango
'''
try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")

except ZeroDivisionError: # división entre 0, inviable
    print("Error, no podemos dividir entre 0")

except ValueError: # error en el valor que hemos introducido
    print("Error, no podemos trabajar con este valor introducido")