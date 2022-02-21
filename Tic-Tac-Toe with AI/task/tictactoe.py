def print_cells(cells):
    split_cells = list(cells)
    for j in range(len(split_cells)):
        if split_cells[j] == '_':
            split_cells[j] = ' '
    board = _create_board(split_cells)
    s = '---------\n'
    for row in board:
        s += '| '
        for place in row:
            s += place + ' '
        s += '|'
        s += "\n"
    s += '---------'
    return s


def _create_board(cells):
    rows = []
    x = 0
    for i in range(3):
        row = []
        for j in range(3):
            row.append(cells[x])
            x += 1
        rows.append(row)
    return rows


print(print_cells('_XXOO_OX_'))
