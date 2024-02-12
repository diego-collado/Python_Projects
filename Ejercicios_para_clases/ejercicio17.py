'''
Almacenar los nombres de 5 productos y sus precios.
Utilizar una lista y cada elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
        1) Cargar por teclado.
        2) Listar los productos y precios.
        3) Imprimir los productos con precios comprendidos entre 10 y 15.
'''
#FUNCTIONS
def cargar_productos():
    productos = []

    for i in range(5):
        nombre = input("Introduce nombre del producto: ")
        precio = int(input("Introduce precio del producto: "))
        productos.append((nombre, precio))#añadimos a cada elemento de la lista una tupla nombre-precio
    return productos
def imprimir_productos(productos):
    print("LISTA DE PRODUCTOS MERCALLORONA")
    for nombre, precio in productos:
        #productos= [ (nombre, precio), (nombre, precio), (nombre, precio)...]
        print(f"Nombre:{nombre} - {precio}€")
def imprimir_entre10y15(productos):
    print("LISTA DE PRODUCTOS MERCALLORONA (>=10€ y <=15€)")
    for nombre, precio in productos:
        #productos= [ (nombre, precio), (nombre, precio), (nombre, precio)...]
        if (precio >= 10) and (precio <= 15):
            print(f"Nombre:{nombre} - {precio}€")
#MAIN
productos = cargar_productos()
imprimir_productos(productos)
imprimir_entre10y15(productos)