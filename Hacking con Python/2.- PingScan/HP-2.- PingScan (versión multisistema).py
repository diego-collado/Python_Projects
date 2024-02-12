import os

red = input("Introduzca red (ejemplo --> 192.168.1): ")
if red == "":
    red = "192.168.1"
rangoInicial = int(input("Introduzca rango inicial (ejemplo --> 1): "))
rangoFinal = int(input("Introduzca rango final (ejemplo --> 250): "))

# Obtenemos el sistema operativo, nt = windows, posix = Linux
so = os.name

if rangoInicial > rangoFinal:
    print("Debe indicar un rango inicial inferior al rango final")
else:
    listaIP = []  # Lista de IP que responden al ping
    for i in range(rangoInicial, rangoFinal, 1):  # Recorremos el rango de IP indicado
        ipEquipo = red + "." + str(i)
        print("Haciendo ping a IP " + ipEquipo, end=" ")
        if (so == "nt"):
            rep = os.system("ping -n 1 " + ipEquipo + " > 1")
        else:
            rep = os.system("ping -c 1 " + ipEquipo + " > 1")
        if rep == 0:
            listaIP.append(ipEquipo)
            print("[OK]")
        else:
            print("[No responde]")

    print("\n Las IP que han respondido al ping: " + str(len(listaIP)))
    for i in range(len(listaIP)):
        print(listaIP[i])