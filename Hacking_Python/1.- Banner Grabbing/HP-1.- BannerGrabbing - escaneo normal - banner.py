#IMPORTS
import socket
import threading
import time


def scan_port(port):
    try:
        host = "localhost"# Dirección ip que hay que escanear.
        host_ip = socket.gethostbyname(host)
        status = False

        # se crea una nueva instancia del socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # se conecta con la ip proporcionada y se testean los puertos
        s.connect((host_ip, port))
        try:
            banner = s.recv(1024).decode()
            print("El puerto {} está abierto. Tiene el banner: {}".format(port, banner))

        except:
            print("El puerto {} está abierto.".format(port))

    except:
        pass


start_time = time.time()

for i in range(0, 100000):
    thread = threading.Thread(target=scan_port, args=[i])
    thread.start()

end_time = time.time()
print("El escaneo de puertos (todos) ha tomado {} segundos".format(end_time - start_time))