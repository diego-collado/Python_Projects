'''
while True: ¿bonito o feo?

Mientras que sea verdadero... Siempre se cumplirá la condición.
Se ejecuta un llamado bucle infinito. Se utiliza en programación para:
    · espera de eventos: conexión a LAN, entrada usuario...
    · para servidores: siempre deben estar activos
    · lectura de datos continuada: sensores
    · programación interactiva: siempre hay listener activos
'''
contador = 1 # inicialización en el mismo momento de su creación

while True:
    entrada = input("Escribe 'salir' para terminar:    ")
    print(f"Te estoy contando: {contador}")
    contador += 1# contador = contador + 1, es decir, cuanta 1 cada vez
    if entrada == 'salir':
        break # aquí está el corte de trabajo real