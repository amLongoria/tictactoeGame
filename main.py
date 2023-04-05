import random
import time

def print_board(grid: list[list]) -> str:
    """
    :param grid:
        current grid
    :return:
        printable grid
    """

    string = ''

    for row in range(3):
        string += '{0} | {1} | {2}\n'.format(str(grid[row][0]), str(grid[row][1]), str(grid[row][2]))
        if row < 2:
            string += '---------\n'
    return string


def player_select() -> str:
    """

    :return:
        True if X
        False if O
    """

    while True:
        player = input('Play as X or O?\n')
        if player.lower() == 'x':
            return player.upper()
        elif player.lower() == 'o':
            return player.upper()


def check_winner(grid: list[list]) -> str:

    diagonal = []

    for row in grid:
        if len(set(row)) == 1:
            return row[0]

    for col in range(3):
        column = [column[col] for column in grid]
        if len(set(column)) == 1:
            return column[0]

        diagonal.append(grid[col][col])
    if len(set(diagonal)) == 1:
        return diagonal[0]

    diagonal = []
    diagonal.append(grid[0][2])
    diagonal.append(grid[1][1])
    diagonal.append(grid[2][0])
    if len(set(diagonal)) == 1:
        return diagonal[0]



def tictactoe() -> str:
    """
    :return:
        final resulting board
    """

    turns = 0
    playing = True
    index = ['a','b','c']
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    ex_grid = [['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3']]

    player = player_select()
    print('Here is the board and its indices')
    print('A1 | B1 | C1\n-----------\nA2 | B2 | C2\n-----------\nA3 | B3 | C3\n')

    while playing:
        if player == 'X':
            move = input('Where would you like to go?')
        else:

            while True:
                your_turn = True

                print('the bot\'s turn...\n')
                bot_move = random.randint(0, 8)
                if not grid[bot_move // 3][bot_move % 3]:
                    grid[bot_move // 3][bot_move % 3] = 'X'
                    print(print_board(grid))
                    turns += 1
                    break

            status = check_winner(grid)
            if isinstance(status, str):
                print('X wins!')
                return print_board(grid)
            elif turns == 9:
                if not isinstance(status, str):
                    print('tie!')
                    return print_board(grid)

            while your_turn:
                move = input('Your turn! Where would you like to go?\n')
                for row in ex_grid:
                    if move.upper() in row:
                        if not grid[int(move[1])-1][index.index(move[0])]:
                            grid[int(move[1])-1][index.index(move[0])] = 'O'
                            print(print_board(grid))
                            your_turn = False
                            turns += 1

            status = check_winner(grid)
            if isinstance(status, str):
                print('O wins!')
                return print_board(grid)


print(tictactoe())