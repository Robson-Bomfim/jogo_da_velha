import random


def display_board(board):
    print(' ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print('===============')
    print(' ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('===============')
    print(' ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])


def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player: Voce quer ser "O" ou "X"').upper()

    if marker == 'X':
        print('Você é o player 1 e está com o "X"')
        return ('X', 'O')
    else:
        print('Você é o player 2 e está com o "O"')
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # top horizontal
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # meio horizontal
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # baixo horizontal
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # primeira coluna vertical
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # segunda coluna vertical
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # terceira coluna vertical
            (board[9] == mark and board[5] == mark and board[1] == mark) or  # diagonal
            (board[7] == mark and board[5] == mark and board[3] == mark))  # diagonal


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = ' '

    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Player, escolha sua jogada de (1-9)!')

    return int(position)


def replay():
    return input('Quer jogar novamente? "Sim" ou "Nao" ').lower().startswith('s')


print('Bem vindo ao jogo da velha!')

while True:
    # Defina o jogo
    # pass

    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' Começa!')
    game_on = True

    while game_on:
        # Vez do jogador 1
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

        # checa vitoria
        if win_check(board, player1_marker):
            display_board(board)
            print('Parabéns! Você venceu! Player 1')
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print('Empate!')
                break
            else:
                turn = 'Player 2'

        # Vez do jogador 2
        if turn == 'Player 2':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

        # checa vitoria
        if win_check(board, player2_marker):
            display_board(board)
            print('Parabéns! Você venceu! Player 2')
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print('Empate!')
                break
            else:
                turn = 'Player 1'

    if not replay():
        break
