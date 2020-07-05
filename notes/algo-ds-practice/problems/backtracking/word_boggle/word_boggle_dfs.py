'''
Possible optimizations:

1. Pass maxLen of word in the dictionary. Terminate DFS when it tries to grow word beyond this limit.
2. Upon matching a word first time, delete all of its occurrences from the dictionary,
so that subsequent matches required are lesser in number.
'''


def get_neighbours(matrix, pos):
    '''
    Returns the valid neighbours only.
    '''
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
    return x >= 0 and x < rows and y >= 0 and y < cols


def dfs(matrix, dictionary, current_pos, current_word, visited, solutions):
    current_word += matrix[current_pos[0]][current_pos[1]]
    if current_word in dictionary:
        solutions.add(current_word)
    visited.add(current_pos)
    neighbours = get_neighbours(matrix, current_pos)
    for neigh in neighbours:
        if neigh not in visited:
            dfs(matrix, dictionary, neigh, current_word, visited, solutions)
    visited.remove(current_pos)


def get_all_words(matrix, dictionary):
    solutions = set()
    visited = set()
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            current_word = ''
            current_pos = (i, j)
            dfs(matrix, dictionary, current_pos, current_word, visited,
                solutions)
    return solutions


def main():
    dictionary = set()
    dictionary.add('geeks')
    dictionary.add('for')
    dictionary.add('quiz')
    dictionary.add('go')
    matrix = []
    matrix.append([x for x in 'g i z'.split()])
    matrix.append([x for x in 'u e k'.split()])
    matrix.append([x for x in 'q s e'.split()])
    solutions = get_all_words(matrix, dictionary)
    print(solutions)


main()
