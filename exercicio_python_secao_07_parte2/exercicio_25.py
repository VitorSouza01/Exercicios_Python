"""
25. Faça um programa para determinar a próxima jogada em um Jogo da Velha. Assumir que o tabuleiro é representado por
uma matriz de 3 x 3, onde cada posição representa uma das casas do tabuleiro. A matriz pode conter os seguintes
valores -1, 0, 1 representando respectivamente uma casa contendo uma peça minha (-1), uma casa vazia do tabuleiro(0),
e uma casa contendo uma peça do meu oponente (1).

Exemplo:

[-1,  1, 1]
[-1, -1, 0]
[ 0,  1, 0]
"""
import copy

# Função para imprimir o tabuleiro


def print_board(board):
    for row in board:
        print(row)

# Função para verificar se alguém venceu o jogo


def check_winner(board):
    # Verificar linhas
    for row in board:

        if row.count(row[0]) == len(row) and row[0] != 0:
            return row[0]

    # Verificar colunas
    for col in range(len(board[0])):

        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            return board[0][col]

    # Verificar diagonais
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]

    # Nenhum vencedor
    return 0

# Função para determinar a pontuação de uma jogada


def evaluate(board):
    winner = check_winner(board)

    if winner == -1:
        return 1  # Se eu vencer

    elif winner == 1:
        return -1  # Se meu oponente vencer

    else:
        return 0  # Empate

# Função para determinar a melhor jogada usando o algoritmo Minimax


def minimax(board, depth, maximizing_player):

    if depth == 0 or check_winner(board) != 0:
        return evaluate(board)

    if maximizing_player:
        max_eval = float('-inf')

        for i in range(len(board)):

            for j in range(len(board[0])):

                if board[i][j] == 0:
                    board_copy = copy.deepcopy(board)
                    board_copy[i][j] = -1
                    eval = minimax(board_copy, depth - 1, False)
                    max_eval = max(max_eval, eval)
        return max_eval

    else:
        min_eval = float('inf')

        for i in range(len(board)):

            for j in range(len(board[0])):

                if board[i][j] == 0:
                    board_copy = copy.deepcopy(board)
                    board_copy[i][j] = 1
                    eval = minimax(board_copy, depth - 1, True)
                    min_eval = min(min_eval, eval)
        return min_eval

# Função para determinar a próxima jogada


def get_next_move(board):
    best_score = float('-inf')
    best_move = None

    for i in range(len(board)):

        for j in range(len(board[0])):

            if board[i][j] == 0:
                board_copy = copy.deepcopy(board)
                board_copy[i][j] = -1
                score = minimax(board_copy, 5, False)  # Profundidade do minimax = 5

                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Exemplo de uso


board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

print("Tabuleiro inicial:")
print_board(board)

while check_winner(board) == 0:
    row = int(input("Digite o número da linha (0-2): "))
    col = int(input("Digite o número da coluna (0-2): "))
    board[row][col] = 1  # Atualizar a jogada do oponente
    print("Tabuleiro após a jogada do oponente:")
    print_board(board)

    if check_winner(board) != 0:
        break

    next_move = get_next_move(board)
    board[next_move[0]][next_move[1]] = -1  # Minha jogada
    print("Tabuleiro após minha jogada:")
    print_board(board)

winner = check_winner(board)
if winner == -1:
    print("Eu venci!")

elif winner == 1:
    print("O oponente venceu!")

else:
    print("Empate!")
