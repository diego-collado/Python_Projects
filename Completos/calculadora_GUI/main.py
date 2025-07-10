# Archivo main.py

# IMPORTS --------------------------------------------------------
from tkinter import Tk
from gui.calculator_gui import Pycalc

# MAIN -----------------------------------------------------------
if __name__ == "__main__":
    app = Tk()
    app.title("AdictoCalculator")
    app.resizable(False, False)
    app.config(cursor="pencil")
    calculator = Pycalc(app)
    calculator.grid()
    app.mainloop()
