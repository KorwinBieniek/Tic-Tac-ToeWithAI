class AlreadyTakenSpotError(Exception):
    """Raised when one of the indexes is already taken"""
    pass


def return_cells(board):
    s = '---------\n'
    for row in board:
        s += '| '
        for place in row:
            s += f'{place} '
        s += '|'
        s += "\n"
    s += '---------'
    return s


def _create_board(cells):
    rows = []
    x = 0
    for i in range(3):
        row = []
        for _ in range(3):
            row.append(cells[x])
            x += 1
        rows.append(row)
    return rows


def fix_spot(board, player, row_index, col_index):
    if board[row_index][col_index] != ' ':
        raise AlreadyTakenSpotError()
    else:
        board[row_index][col_index] = player


def _verify_coordinates(board, player):
    while True:
        try:
            row, col = list(
                map(int, input('Enter the coordinates: ').split()))
            print()
            fix_spot(board, player, row_index=row - 1, col_index=col - 1)
            break
        except AlreadyTakenSpotError:
            print('This cell is occupied! Choose another one!')
            continue
        except IndexError:
            print('Coordinates should be from 1 to 3!')
            continue
        except ValueError:
            print('You should enter numbers!')
            continue


def is_win(board, player):
    return bool(_check_rows(board, player, len(board)) \
                or _check_columns(board, player, len(board)) \
                or _check_diagonals(board, player, len(board)))


def is_draw(board):
    for row in board:
        for place in row:
            if place == ' ':
                return False
    return True


def _check_rows(board, player, board_length):
    for i in range(board_length):
        if win := all(board[i][j] == player for j in range(board_length)):
            return win


def _check_columns(board, player, board_length):
    for i in range(board_length):
        if win := all(board[j][i] == player for j in range(board_length)):
            return win


def _check_diagonals(board, player, board_length):
    win = True
    for i in range(board_length):
        win = True
        if board[i][i] != player:
            win = False
            break
    if win:
        return win

    for i in range(board_length):
        win = True
        if board[i][board_length - 1 - i] != player:
            win = False
            break
    if win:
        return win
    return False


if __name__ == '__main__':
    cells = list(input('Enter the cells: '))
    for i, _ in enumerate(cells):
        if cells[i] == '_':
            cells[i] = ' '
    from collections import Counter

    counter = Counter(cells)
    player = 'X'
    if counter['X'] <= counter['O']:
        player = 'X'
    else:
        player = 'O'
    # print(player)
    board = _create_board(cells)
    print(return_cells(board))
    _verify_coordinates(board, player)
    print(return_cells(board))
    if is_draw(board):
        print('Draw')
    elif is_win(board, player):
        print(f'{player} wins')
    else:
        print('Game not finished')
