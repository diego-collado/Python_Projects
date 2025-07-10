'''
Hay veces que es complicado crear una función y llamarla... Para esos momentos, creamos las
conocidas como FUNCIONES ANÓNIMAS, cuyo código es muy corto.

Sintaxis:
    función "normal":
        def sumar(a,b):
            return a + b
    función lambda:
        lambda a,b:a+b


'''
def sumar(a,b):
    return a + b

print(sumar(4,8))

print((lambda a,b:a+b)(5,5))