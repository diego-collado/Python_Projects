'''
Función LAMBDA: son funciones anónimas, es decir, un tipo de función de Python que TIPICAMENTE se definen
en una única línea, cuyo código es muy corto.
Sintaxis: lambda argumentos: expresion

    def suma(a, b):
        return a + b
- - - - - - - - - - - - - -
    lambda a, b: a + b
'''

suma = lambda a, b : a + b
print((lambda a, b : a + b)(8, 8))

def miFuncion(lambda_func):
    return lambda_func(2, 4)

print(miFuncion(lambda a, b : a + b)) # lambda como entrada a función común
print(miFuncion(lambda a, b, c = 3 : a + b + c)(1 , 2)) # lambda con parámetros por defecto
print(miFuncion(lambda a, b, c : a + b + c)(a = 1, b = 4, c = 6)) # lambda con argumentos nombrados

x = lambda a, b : (b, a)
print(x(3, 9))# devolvería más de un valor