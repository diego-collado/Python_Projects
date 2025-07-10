class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.grid:
            print('|'.join(row))
            print('-' * 5)

    def update(self, row, col, symbol):
        if self.grid[row][col] == ' ':
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self):
        lines = self.grid + [list(x) for x in zip(*self.grid)]  # rows and cols
        diagonals = [[self.grid[i][i] for i in range(3)],
                     [self.grid[i][2 - i] for i in range(3)]]
        for line in lines + diagonals:
            if line[0] != ' ' and all(cell == line[0] for cell in line):
                return line[0]
        return None

    def is_full(self):
        return all(cell != ' ' for row in self.grid for cell in row)
