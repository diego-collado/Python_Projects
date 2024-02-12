'''
Detector de proximidad de BlueTooth

BlueTooth: tecnología inalámbrica estándar para el intercambio de datos a corta distancia entre dispositivos fijos
y móviles, creando redes de área personal (PANs). Utiliza radio UHF en la banda ISM de 2.4GHz, pudiendo conectar
múltiples dispositivos al mismo tiempo, superando problemas de sincronización.

Al activar el BT, el dispositivo arranca el modo "descubrimiento", momento en el que emite y recibe información:
    - Dirección MAC: Un identificador único para el dispositivo
    - Nombre del dispositivo: Un nombre legible por humanos asignado al dispositivo
    - RSSI (Indicador de Fuerza de Señal Recibida): Una medida de la potencia de la señal recibida, que se puede
    utilizar para estimar la distancia
    - Servicios disponibles: Conjuntos de funcionalidades que el dispositivo ofrece
    - Características de los servicios: Detalles específicos sobre los servicios (capacidad de leer o escribir datos)

RSSI (Received Signal Strength Indicator): Indicador de fuerza de la señal recibida, no calidad de señal.
Valores: sobre una escala de 0 a -80 RSSI:
    - 0: señal ideal, difícil de lograr en la práctica - solo en condiciones ideales (laboratorios)
    - -40 a -60: señal idónea con tasas de transferencia estables
    - -60: enlace bueno, donde ajustando la transmisión, se podría lograr una conexión estable al 80%
    - -70: enlace medio-bajo, con una señal medianamente buena aunque se pueden sufrir problemas con lluvia y viento
    - -80: es la señal mínima aceptable para establecer la conexión, ya que pueden ocurrir caídas que se traducen
    en corte de comunicación (pérdida de llamada, pérdida de datos), mensajes sms corruptos (ilegibles), etc

Equivalencias en dBm (unidad de medida de relación de potencia expresada en decibelios relativa a un milivatio), es decir,
nivel de cobertura en función de dBm en aire recibido:
    - Menos de -76 dBm (números más cercanos a 0) = Excelente
    - Entre -89 y -77 = Muy buena
    - Entre -97 y -90 = Buena/Media
    - Entre -103 y -98 = Baja cobertura
    - Entre -112 y -104 = Muy baja cobertura (problemas para establecer llamadas)
    - Entre -113 y -132 dBm = Muy poca cobertura (problemas para establecer llamadas y rendimiento muy bajo)
    - A partir de -135 = Sin cobertura

CÁLCULO DE DISTANCIAS
    distancia = 10 ^ ((RSSI_REF - RSSI) / (10 * n))
    distancia = 10 ^ ((RSSI_REF - RSSI) / (10 * PATH_LOSS_EXPONENT)) --> en este caso

RSSI_REF es el RSSI medido a un metro de distancia
PATH_LOSS_EXPONENT es el exponente de pérdida de trayectoria, que depende del entorno

    - distancia: estimación de la distancia entre dispositivo y receptor
    - RSSI_REF: es el RSSI medido a un metro de distancia del transmisor
    - RSSI: medición actual del RSSI
    - n: exponente de pérdida de trayectoria (2 en espacios abiertos)


Más info de imports:
    - https://docs.python.org/es/3/library/asyncio.html
    - https://bleak.readthedocs.io/en/latest/


'''

# IMPORTS
import asyncio
from bleak import discover
import tkinter as tk
from math import pi, cos, sin
import random

# Calibración de valores medidos según el entorno
RSSI_REF = -60 # -60 dBm (el RSSI a un metro)
PATH_LOSS_EXPONENT = 2

# FUNCTIONS

# 1.- búsqueda de dispositivos BlueTooth -----------------------------------
async def buscar_dispositivos_bluetooth():
    dispositivos = await discover() # activación del modo descubrimiento
    return [(dispositivo.address, dispositivo.name or "Desconocido", dispositivo.rssi) for dispositivo in dispositivos]

# 2.- Cálculo de distancias (RSSI) -----------------------------------------
def calcular_distancia(rssi):
    ratio_db = RSSI_REF - rssi #
    ratio_linear = 10 ** (ratio_db / (10 * PATH_LOSS_EXPONENT))
    return ratio_linear

# 3.- Parte visual: representación de datos --------------------------------
def generar_color_unico():
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"
    # {random.randint(0, 255):02x} --> genera un color aleatorio (256 valores posibles) en hexadecimal

def actualizar_interfaz(canvas, lista, dispositivos, x_centro, y_centro, escala):
    # borrado/limpieza de zona Canvas y Tkinter
    canvas.delete("all")
    lista.delete(0, tk.END)

    # posicionándonos... pero nosotros como emisores/receptores
    canvas.create_oval(x_centro - 5, y_centro - 5, x_centro + 5, y_centro + 5, fill="red")
    canvas.create_text(x_centro, y_centro - 10, text="Tú", fill="red")

    # array de dispositivos
    for dispositivo in dispositivos:
        direccion, nombre, rssi = dispositivo
        distancia = calcular_distancia(rssi)
        color = generar_color_unico()

        # posicionamiento y "pintado" de los dispositivos ajenos a nosotros
        angle = random.uniform(0, 2 * pi)
        x_pos = x_centro + distancia * escala * cos(angle)
        y_pos = y_centro + distancia * escala * sin(angle)

        canvas.create_line(x_centro, y_centro, x_pos, y_pos, fill=color) # creación de la línea como tal
        canvas.create_oval(x_pos - 3, y_pos - 3, x_pos + 3, y_pos + 3, outline=color, fill=color)

        # adquiriendo información
        info = f"{nombre}: {distancia:.2f}m (RSSI {rssi} dBm)"
        lista.insert(tk.END, info)

        canvas.create_text(x_pos, y_pos, text=f"{nombre} ({distancia:.2f} m)", fill=color, anchor="center")

# 4.- Actualizar búsqueda de dispositivos-----------------------------------
async def actualizar_async(canvas, lista, x_centro, y_centro, escala):
    dispositivos = await buscar_dispositivos_bluetooth()
    actualizar_interfaz(canvas, lista, dispositivos, x_centro, y_centro, escala)
def on_actualizar_click(canvas, lista, x_centro, y_centro, escala):
    asyncio.run(actualizar_async(canvas, lista, x_centro, y_centro, escala))

# 5.- Manejo de la visual --------------------------------------------------
def zoom_in(canvas, x_centro, y_centro, escala):
    escala_nueva = escala * 1.2
    canvas.scale("all", x_centro, y_centro, 1.2, 1.2)
    return escala_nueva

def zoom_out(canvas, x_centro, y_centro, escala):
    escala_nueva = escala / 1.2
    canvas.scale("all", x_centro, y_centro, 0.8, 0.8)
    return escala_nueva

# 6.- Creando "entorno" -----------------------------------------------------

def main():
    # creación y posicionamiento de ventana
    ventana = tk.Tk()
    ventana.title("Detector BlueTooth - CyberSentinel -")
    ventana.geometry("600x400")

    # creación de frame
    frame = tk.Frame(ventana)
    frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # creación de Canvas
    canvas = tk.Canvas(frame, width=800, height=600)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # creación de lista (listBox)
    lista = tk.Listbox(frame)
    lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


    x_centro, y_centro = 400, 300
    escala = 2

    # creación y colocación de botones
    boton_escanear = tk.Button(ventana, text="Escanear dispositivos",
                               command=lambda: on_actualizar_click(canvas, lista, x_centro, y_centro, escala))
    boton_escanear.pack(side=tk.BOTTOM)

    boton_zoom_in = tk.Button(ventana, text="+", command=lambda: zoom_in(canvas, x_centro, y_centro, escala))
    boton_zoom_in.pack(side=tk.BOTTOM)

    boton_zoom_out = tk.Button(ventana, text="-", command=lambda: zoom_out(canvas, x_centro, y_centro, escala))
    boton_zoom_out.pack(side=tk.BOTTOM)

    ventana.mainloop()

# MAIN
if __name__ == "__main__":
    main()
