'''
Generador de contraseñas aleatorias
'''
# 1º método: el más simple
import random # genera valores aleatorios
import string # trabaja con las cadenas

password = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(25))
print(password)

# 2º método: rizando el rizo rizado
import random
import string

# string.ascii_letters --> letras minus/mayus ASCII
# string.digits --> dígitos ASCII
# string.punctuation) --> símbolos ASCII

todos = string.ascii_letters + string.digits + string.punctuation

print (''.join(random.choices(todos, k=25))) # k= longitud de la clave
