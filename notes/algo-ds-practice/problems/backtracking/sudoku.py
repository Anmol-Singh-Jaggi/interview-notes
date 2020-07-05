from math import sqrt


def get_empty_slots(matrix):
    empty_slots = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 0:
                empty_slots.append((i, j))
    return empty_slots


def change_value(matrix, cache, slot_pos, num):
    '''
    We'll need to update the caches while updating a matrix value.
    '''
    posx = slot_pos[0]
    posy = slot_pos[1]
    old_num = matrix[posx][posy]

    cache_row = cache['row'].get(posx, set())
    cache['row'][posx] = cache_row
    cache_row.discard(old_num)
    cache_row.add(num)

    cache_col = cache['col'].get(posy, set())
    cache['col'][posy] = cache_col
    cache_col.discard(old_num)
    cache_col.add(num)

    submatrix_index = get_submatrix_index(matrix, slot_pos)
    cache_submatrix = cache['submatrix'].get(submatrix_index, set())
    cache['submatrix'][submatrix_index] = cache_submatrix
    cache_submatrix.discard(old_num)
    cache_submatrix.add(num)

    matrix[posx][posy] = num


def is_valid(matrix, cache, slot_pos, num):
    cache_row = cache['row']
    if num in cache_row[slot_pos[0]]:
        return False
    cache_col = cache['col']
    if num in cache_col[slot_pos[1]]:
        return False
    cache_submatrix = cache['submatrix']
    if num in cache_submatrix[get_submatrix_index(matrix, slot_pos)]:
        return False
    return True


def get_submatrix_index(matrix, slot_pos):
    size = int(sqrt(len(matrix)))
    submatrix_pos = (slot_pos[0] // size, slot_pos[1] // size)
    return submatrix_pos[0] * size + submatrix_pos[1]


def dfs(matrix, cache, empty_slots, slot_pos, num_empty_slots):
    if num_empty_slots == 0:
        return True
    for num in range(1, 10):
        if is_valid(matrix, cache, empty_slots[slot_pos], num):
            change_value(matrix, cache, empty_slots[slot_pos], num)
            found_solution = dfs(matrix, cache, empty_slots, slot_pos + 1,
                                 num_empty_slots - 1)
            if found_solution:
                return True
            change_value(matrix, cache, empty_slots[slot_pos], 0)
    return False


def compute_cache(matrix, cache):
    # A cache of all the number currently in 'i'th row/column/submatrix.
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            change_value(matrix, cache, (i, j), matrix[i][j])


def solve_sudoku(matrix):
    cache_row_nums = dict()
    cache_col_nums = dict()
    cache_submatrix_nums = dict()
    cache = dict()
    cache['row'] = cache_row_nums
    cache['col'] = cache_col_nums
    cache['submatrix'] = cache_submatrix_nums
    compute_cache(matrix, cache)
    empty_slots = get_empty_slots(matrix)
    return dfs(matrix, cache, empty_slots, 0, len(empty_slots))


def print_answer(matrix):
    for i in range(0, len(matrix)):
        print(' '.join(map(str, matrix[i])))


def main():
    sudoku_linear = '3 0 6 5 0 8 4 0 0 5 2 0 0 0 0 0 0 0 0 8 7 0 0 0 0 3 1 0 0 3 0 1 0 0 8 0 9 0 0 8 6 3 0 0 5 0 5 0 0 9 0 6 0 0 1 3 0 0 0 0 2 5 0 0 0 0 0 0 0 0 7 4 0 0 5 2 0 6 3 0 0'
    sudoku_linear = [int(x) for x in sudoku_linear.split()]
    k = 0
    matrix = [[None for j in range(9)] for i in range(9)]
    for i in range(0, 9):
        for j in range(0, 9):
            matrix[i][j] = sudoku_linear[k]
            k += 1
    print(matrix)
    ans = solve_sudoku(matrix)
    print(ans)
    print_answer(matrix)


main()
