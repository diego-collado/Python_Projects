'''
10.- Cargar una oración por teclado. Mostrar luego cuántos espacios en blanco se han
ingresado. Debemos tener en cuenta que un espacio en blanco se identifica como " ", y
las cadenas vacías como "".
'''
# DECLARACIÓN E INICIALIZACIÓN DE VARIABLES ----------

frase = input("Introduzca una frase completa: \n")
blancos = 0
espacios = 0

# MAIN -----------------------------------------------
#[m][i][ ][c][o][c][h][e][ ][e][s][ ][r][o][j][o]
for caracter in frase:
    if caracter == " ":
        blancos = blancos + 1
        # es lo mismo que lo anterior blancos += 1 

# Otra forma válida para hacerlo
espacios = frase.count(" ")


print(f"En la frase, hemos detectado {blancos} espacios.")
#Cuando ponemos f"..." en un print, podemos insertar cualquier variable
#en sitio que queramos, es decir, yo puedo poner blancos antes o después
# de cualquier otra palabra, variable... Sólo debo escribir { } para
# decir que ahí va a estar la variable periquito_colorao.

print("En la frase, hemos detectado",espacios,"espacios") 