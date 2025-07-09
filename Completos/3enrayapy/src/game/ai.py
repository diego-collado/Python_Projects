import random

class AIPlayer:
    def __init__(self, symbol):
        self.name = "Computadora"
        self.symbol = symbol

    def make_move(self, board):
        print("Turno de la computadora:")
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if board.update(row, col, self.symbol):
                break
