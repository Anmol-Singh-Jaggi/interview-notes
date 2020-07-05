def is_on_same_diagonal(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) == abs(y1 - y2)


def is_valid_order(pos_last, positions):
    if len(positions) == 0:
        return True
    for i in range(0, len(positions)):
        if pos_last[0] == positions[i][0]:
            return False
        if is_on_same_diagonal(positions[i], pos_last):
            return False
    return True


def n_queens(size, col_idx, current_order, solutions):
    if col_idx == size + 1:
        solutions.append([elem[0] for elem in current_order])
        return
    for row_idx in range(1, size+1):
        next_pos = (row_idx, col_idx)
        if is_valid_order(next_pos, current_order):
            n_queens(size, col_idx + 1, current_order + [next_pos], solutions)


def main():
    size = 4
    solutions = []
    n_queens(size, 1, [], solutions)
    print(solutions)


main()
