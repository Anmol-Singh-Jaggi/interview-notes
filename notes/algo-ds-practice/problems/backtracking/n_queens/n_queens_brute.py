def generate_all_permutations_iterator(lst, start, end):
    if start >= end:
        yield list(lst)
        return
    for i in range(start, end):
        lst[start], lst[i] = lst[i], lst[start]
        yield from generate_all_permutations_iterator(lst, start + 1, end)
        lst[start], lst[i] = lst[i], lst[start]


def is_on_same_diagonal(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) == abs(y1 - y2)


def is_valid_order(order):
    positions = [(order[i], i) for i in range(len(order))]
    x_positions = [pos[0] for pos in positions]
    if len(set(x_positions)) != len(positions):
        return False
    y_positions = [pos[1] for pos in positions]
    if len(set(y_positions)) != len(positions):
        return False
    for i in range(0, len(positions)):
        for j in range(i + 1, len(positions)):
            if is_on_same_diagonal(positions[i], positions[j]):
                return False
    return True


def n_queens(size):
    solutions = []
    lst = [i for i in range(1, size + 1)]
    for order in generate_all_permutations_iterator(lst, 0, len(lst)):
        if is_valid_order(order):
            solutions.append(order)
    return solutions


def main():
    size = 1
    ans = n_queens(size)
    print(ans)


main()
