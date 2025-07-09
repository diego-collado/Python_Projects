class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        while True:
            try:
                row = int(input(f"{self.name} ({self.symbol}), fila (0-2): "))
                col = int(input(f"{self.name} ({self.symbol}), columna (0-2): "))
                if board.update(row, col, self.symbol):
                    break
                else:
                    print("Casilla ocupada, intenta otra.")
            except ValueError:
                print("Entrada inválida, usa números entre 0 y 2.")
