def get_num_islands(matrix):
    num_islands = 0
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                dfs(matrix, (i, j))
                num_islands += 1
    return num_islands


def get_neighbours(matrix, pos):
    x, y = pos
    # U, UR, R, RD, D, DL, L, LU
    neighbours = []
    neighbours.append((x - 1, y))
    neighbours.append((x - 1, y + 1))
    neighbours.append((x, y + 1))
    neighbours.append((x + 1, y + 1))
    neighbours.append((x + 1, y))
    neighbours.append((x + 1, y - 1))
    neighbours.append((x, y - 1))
    neighbours.append((x - 1, y - 1))
    neighbours = [neigh for neigh in neighbours if is_pos_valid(matrix, neigh)]
    return neighbours


def is_pos_valid(matrix, pos):
    rows, cols = len(matrix), len(matrix[0])
    x, y = pos
    return x >= 0 and x < rows and y >= 0 and y < cols and matrix[x][y] == 1


def dfs(matrix, pos):
    matrix[pos[0]][pos[1]] = 0
    neighbours = get_neighbours(matrix, pos)
    for neigh in neighbours:
        if matrix[neigh[0]][neigh[1]] == 1:
            dfs(matrix, neigh)


def main():
    matrix = []
    matrix.append([1, 1, 0, 0])
    matrix.append([0, 0, 1, 0])
    matrix.append([0, 0, 0, 1])
    matrix.append([0, 1, 0, 0])
    ans = get_num_islands(matrix)
    print(ans)


main()
