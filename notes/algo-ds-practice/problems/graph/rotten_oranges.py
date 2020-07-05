"""
Given a matrix of dimension r*c where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

So, we have to determine what is the minimum time required to rot all oranges.
A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time.
If it is impossible to rot every orange then simply return -1.
"""
from collections import deque


def get_all_rotten(matrix):
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                res.append((i, j))
    return res


def get_fresh_orange_neighbours(matrix, pos):
    x, y = pos
    neighbours = [(x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y)]
    neighbours = [neigh for neigh in neighbours if is_pos_valid(matrix, neigh)]
    return neighbours


def is_pos_valid(matrix, pos):
    rows, cols = len(matrix), len(matrix[0])
    x, y = pos
    return x >= 0 and x < rows and y >= 0 and y < cols and matrix[x][y] == 1


def is_any_fresh_orange_present(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                return True
    return False


def min_time_rotten(matrix):
    rottens = get_all_rotten(matrix)
    current_time = 0
    queue = deque(rottens)
    sentinel = (-1, -1)
    queue.append(sentinel)
    # Like a 'Level-Order BFS'
    while queue:
        top = queue.popleft()
        if top == sentinel:
            if not queue:
                break
            current_time += 1
            queue.append(sentinel)

        fresh_oranges = get_fresh_orange_neighbours(matrix, top)
        for pos in fresh_oranges:
            matrix[pos[0]][pos[1]] = 2
            queue.append(pos)
    if is_any_fresh_orange_present(matrix):
        return -1
    return current_time


def main():
    tc = int(input())
    while tc:
        tc -= 1
        rows, cols = [int(x) for x in input().split()]
        matrix_linear = [int(x) for x in input().split()]
        k = 0
        matrix = [[None for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = matrix_linear[k]
                k += 1
        ans = min_time_rotten(matrix)
        print(ans)


main()
