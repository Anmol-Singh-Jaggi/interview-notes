def get_neighbours(maze, pos):
    '''
    Returns the valid neighbours only.
    '''
    x, y = pos
    # Print in sorted order - D L R U.
    neighbours = [(x + 1, y, 'D'), (x, y - 1, 'L'), (x, y + 1, 'R'),
                  (x - 1, y, 'U')]
    neighbours = [neigh for neigh in neighbours if is_pos_valid(maze, neigh)]
    return neighbours


def is_pos_valid(maze, pos):
    maze_dim = len(maze)
    x, y, _ = pos
    return x >= 0 and x < maze_dim and y >= 0 and y < maze_dim and maze[x][
        y] == 1


def find_paths(maze, current_pos, current_path, visited, solutions):
    maze_dim = len(maze)
    if current_pos == (maze_dim - 1, maze_dim - 1):
        solutions.append(current_path)
        return
    visited.add(current_pos)
    neighbours = get_neighbours(maze, current_pos)
    for neigh in neighbours:
        neigh_pos = (neigh[0], neigh[1])
        if neigh_pos not in visited:
            find_paths(maze, neigh_pos, current_path + neigh[2], visited,
                       solutions)
    visited.remove(current_pos)


def main():
    maze = []
    maze.append([int(x) for x in '1 0 0 0'.split()])
    maze.append([int(x) for x in '1 1 0 1'.split()])
    maze.append([int(x) for x in '1 1 0 0'.split()])
    maze.append([int(x) for x in '0 1 1 1'.split()])
    solutions = []
    current_path = ''
    current_pos = (0, 0)
    visited = set()
    find_paths(maze, current_pos, current_path, visited, solutions)
    print(solutions)


main()
