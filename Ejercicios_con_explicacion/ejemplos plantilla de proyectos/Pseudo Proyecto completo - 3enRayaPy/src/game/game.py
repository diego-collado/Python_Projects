from .board import Board
from .player import Player
from .ai import AIPlayer

def start_game():
    print("Bienvenido a 3 en Raya")
    mode = input("¿Jugar contra la computadora? (s/n): ").strip().lower()
    board = Board()
    player1 = Player("Jugador 1", "X")
    if mode == 's':
        player2 = AIPlayer("O")
    else:
        player2 = Player("Jugador 2", "O")

    current_player = player1
    while True:
        board.display()
        current_player.make_move(board)
        winner = board.check_winner()
        if winner:
            board.display()
            print(f"¡{current_player.name} ({winner}) ha ganado!")
            break
        if board.is_full():
            board.display()
            print("¡Empate!")
            break
        current_player = player2 if current_player == player1 else player1
