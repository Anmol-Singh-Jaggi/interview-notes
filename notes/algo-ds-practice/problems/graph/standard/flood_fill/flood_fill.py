def get_neighbours(matrix, pos, color):
    x, y = pos
    neighbours = [(x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y)]
    neighbours = [
        neigh for neigh in neighbours if is_pos_valid(matrix, neigh, color)
    ]
    return neighbours


def is_pos_valid(matrix, pos, color):
    rows, cols = (len(matrix), len(matrix[0]))
    x, y = pos
    return x >= 0 and x < rows and y >= 0 and y < cols and matrix[x][y] == color


def dfs(matrix, pos, color, old_color):
    matrix[pos[0]][pos[1]] = color
    neighbours = get_neighbours(matrix, pos, old_color)
    for neigh in neighbours:
        dfs(matrix, neigh, color, old_color)


def flood_fill(matrix, pos, color):
    old_color = matrix[pos[0]][pos[1]]
    dfs(matrix, pos, color, old_color)


def main():
    matrix_dims = (3, 4)
    matrix_linear = [int(x) for x in '0 1 1 0 1 1 1 1 0 1 2 3'.split()]
    k = 0
    matrix = [[None for j in range(matrix_dims[1])]
              for i in range(matrix_dims[0])]
    for i in range(matrix_dims[0]):
        for j in range(matrix_dims[1]):
            matrix[i][j] = matrix_linear[k]
            k += 1
    flood_fill(matrix, (0, 1), 5)
    k = 0
    for i in range(matrix_dims[0]):
        for j in range(matrix_dims[1]):
            matrix_linear[k] = matrix[i][j]
            k += 1
    print(' '.join(map(str, matrix_linear)))


main()
