import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def player_move(board):
    while True:
        try:
            move = int(input("Введи число від 1 до 9: ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Ця клітинка вже зайнята!")
        except (ValueError, IndexError):
            print("Некоректний ввід. Введи число від 1 до 9.")

def computer_move(board):
    row, col = random.choice(get_empty_cells(board))
    board[row][col] = "O"
    print(f"Комп'ютер вибрав клітинку {row * 3 + col + 1}")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Хрестики-нулики! Ти граєш за X, комп'ютер за O.")
    print_board(board)
    
    for turn in range(9):
        if turn % 2 == 0:
            player_move(board)
        else:
            computer_move(board)
        print_board(board)
        
        if check_winner(board, "X"):
            print("Ти виграв!")
            return
        elif check_winner(board, "O"):
            print("Комп'ютер виграв!")
            return
    
    print("Нічия!")

if __name__ == "__main__":
    main()
