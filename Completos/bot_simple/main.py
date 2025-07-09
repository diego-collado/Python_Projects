# Archivo main.py

# IMPORTS --------------------------------------------------------
from ia.engine import SimpleBot

# FUNCTIONS ------------------------------------------------------
def main():
    bot = SimpleBot()
    print("¡Hola! Soy SimpleBot. Escribe 'salir' para terminar.")

    while True:
        user_input = input("Tú: ").strip().lower()
        if user_input == "salir":
            print("SimpleBot: ¡Hasta luego!")
            break
        respuesta = bot.responder(user_input)
        print(f"SimpleBot: {respuesta}")
# MAIN -----------------------------------------------------------
if __name__ == "__main__":
    main()