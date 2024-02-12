'''
Se deberá utilizar una lista de subredes
'''

import datetime
import ipaddress
from ping3 import ping
import concurrent.futures
import threading

subnets = ['192.168.102.0/29', '192.168.107.0/29', '192.168.108.0/29']  # añadir las subnets
output_file = 'resultados_ping.txt'
output_lock = threading.Lock()

def ping_sweep(subnet):
    network = ipaddress.ip_network(subnet, strict=False)
    results = []

    for ip in network.hosts():
        ip_str = str(ip)
        # se construye cadena con una marca de tiempo
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # se intenta hacer ping a la IP actual y se construye string con los resultados
        try:
            response_time = ping(ip_str, timeout=1)
            if response_time is not None:
                message = f"{timestamp} - {ip_str} es accesible"
            else:
                message = f"{timestamp} - {ip_str} no es accesible (inalcanzable)"
        except Exception:
            message = f"{timestamp} - Error en el ping {ip_str}"

        results.append(message)

    with output_lock:
        print(f"Resultados del ping para la sudred: {subnet}:")
        with open(output_file, 'a') as f:
            f.write(f"Resultados del ping para la sudred: {subnet}:\n")
            for msg in results:
                print(msg)
                f.write(msg + '\n')
            f.write('\n')
        print()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(ping_sweep, subnets)