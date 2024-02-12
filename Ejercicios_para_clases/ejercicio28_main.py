'''
Definir una clase Cliente que almacene un código de cliente y un nombre.
En la clase Cliente definir una variable de clase de tipo lista que almacene todos los clientes que
tienen suspendidas sus cuentas corrientes.
Imprimir por pantalla todos los datos de clientes y el estado que se encuentra su cuenta corriente.
'''
#CLASS
class Cliente:
    suspendidos = []

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def imprimir(self):
        print(f"Código cliente: {self.codigo} - Nombre: {self.nombre}")
        self.suspensos()

    def suspensos(self):
        if (self.codigo in Cliente.suspendidos):
            print(f"El cliente {self.nombre}, con código {self.codigo}, está suspendido.")
        else:
            print(f"El cliente {self.nombre}, con código {self.codigo}, está activo.")
    def suspender(self):
        Cliente.suspendidos.append(self.codigo)
#MAIN
cliente1 = Cliente(1, "Diego")
cliente2 = Cliente(2, "Marta")
cliente3 = Cliente(3, "Adrián")
cliente4 = Cliente(4, "Izan")

cliente1.suspender()
cliente2.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(Cliente.suspendidos)