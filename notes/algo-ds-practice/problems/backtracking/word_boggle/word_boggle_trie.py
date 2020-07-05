from ds.trie.trie import Trie


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


def dfs(matrix, trie_root, current_pos, current_word, visited, solutions):
    current_word += matrix[current_pos[0]][current_pos[1]]
    if trie_root.is_end:
        solutions.add(current_word)
    visited.add(current_pos)
    neighbours = get_neighbours(matrix, current_pos)
    for neigh in neighbours:
        if neigh not in visited:
            neigh_char = matrix[neigh[0]][neigh[1]]
            if neigh_char not in trie_root.children:
                continue
            dfs(matrix, trie_root.get_child(neigh_char), neigh, current_word,
                visited, solutions)
    visited.remove(current_pos)


def get_all_words(matrix, trie_root):
    solutions = set()
    visited = set()
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] not in trie_root.children:
                continue
            current_word = ''
            current_pos = (i, j)
            dfs(matrix, trie_root.get_child(matrix[i][j]), current_pos,
                current_word, visited, solutions)
    return solutions


def main():
    trie = Trie()
    trie.insert('geeks')
    trie.insert('for')
    trie.insert('quiz')
    trie.insert('go')
    matrix = []
    matrix.append([x for x in 'g i z'.split()])
    matrix.append([x for x in 'u e k'.split()])
    matrix.append([x for x in 'q s e'.split()])
    solutions = get_all_words(matrix, trie.root)
    if not solutions:
        solutions = '-1'
    print(solutions)


main()
