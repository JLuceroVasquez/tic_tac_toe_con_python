"""Proyecto Final - Fundamentos de Python 1 (PE1): Tic-Tac-Toe.

La maquina juega con 'X' (primer movimiento siempre en el centro) y el
usuario con 'O'. La maquina elige sus cuadros de forma aleatoria.
"""
from random import randrange


def display_board(board):
    # La funcion acepta un parametro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def enter_move(board):
    # La funcion acepta el estado actual del tablero y pregunta al usuario acerca de
    # su movimiento, verifica la entrada y actualiza el tablero acorde a la decision.
    ok = False  # suposicion falsa - la necesitamos para entrar al bucle
    while not ok:
        move = input("Ingresa tu movimiento: ")
        ok = len(move) == 1 and move >= '1' and move <= '9'  # es valido lo ingresado?
        if not ok:
            print("Movimiento erroneo, ingresalo nuevamente")  # no lo es, ingresalo otra vez
            continue
        move = int(move) - 1  # numero de celda de 0 a 8
        row = move // 3  # fila de la celda
        col = move % 3  # columna de la celda
        sign = board[row][col]  # verificamos el cuadro elegido
        ok = sign not in ['O', 'X']
        if not ok:  # esta ocupado - movimiento invalido
            print("Cuadro ocupado, ingresa otro")
            continue
    board[row][col] = 'O'  # establecemos '0' en el cuadro


def make_list_of_free_fields(board):
    # La funcion examina el tablero y construye una lista de todos los cuadros vacios.
    # La lista esta compuesta por tuplas, cada tupla es un par de numeros de fila y columna.
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free.append((row, col))
    return free


def victory_for(board, sgn):
    # La funcion analiza el estado del tablero para verificar si
    # el jugador que utiliza 'O's o 'X's ha ganado el juego.
    if sgn == "X":  # estamos buscando X?
        who = 'me'  # si, es la maquina
    elif sgn == "O":  # ... o tal vez O?
        who = 'you'  # si, es el usuario
    else:
        who = None  # no deberiamos caer aqui!
    cross1 = cross2 = True  # para las diagonales
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:  # revisa fila rc
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:  # revisa columna rc
            return who
        if board[rc][rc] != sgn:  # revisa la 1ra diagonal
            cross1 = False
        if board[2 - rc][rc] != sgn:  # revisa la 2da diagonal
            cross2 = False
    if cross1 or cross2:
        return who
    return None


def draw_move(board):
    # La funcion dibuja el movimiento de la maquina y actualiza el tablero.
    free = make_list_of_free_fields(board)
    cnt = len(free)
    if cnt > 0:
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'


def main():
    board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]  # tablero inicial
    board[1][1] = 'X'  # el primer movimiento de la maquina: el centro
    free = make_list_of_free_fields(board)
    human_turn = True  # cual turno es?
    while len(free):
        display_board(board)
        if human_turn:
            enter_move(board)
            victor = victory_for(board, 'O')
        else:
            draw_move(board)
            victor = victory_for(board, 'X')
        if victor is not None:
            break
        human_turn = not human_turn
        free = make_list_of_free_fields(board)

    display_board(board)
    if victor == 'you':
        print("¡Has Ganado!")
    elif victor == 'me':
        print("¡La maquina ha ganado!")
    else:
        print("¡Empate!")


if __name__ == "__main__":
    main()
