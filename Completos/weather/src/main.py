# Archivo main.py

# IMPORTS ------------------------------------------------------
import argparse
from weather import get_weather

# FUNCTIONS ----------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Consulta el clima de una ciudad.")
    parser.add_argument("--city", required=True, help="Nombre de la ciudad")
    args = parser.parse_args()

    resultado = get_weather(args.city)

    if "error" in resultado:
        print(f"❌ Error: {resultado['error']}")
    else:
        print(f"🌤 Clima en {resultado['ciudad']}:")
        print(f"  Temperatura: {resultado['temperatura']}°C")
        print(f"  Sensación térmica: {resultado['sensacion']}°C")
        print(f"  Estado: {resultado['clima'].capitalize()}")
        print(f"  Humedad: {resultado['humedad']}%")
        print(f"  Viento: {resultado['viento']} m/s")

# MAIN -------------------------------------------------------
if __name__ == "__main__":
    main()