def snake_ladder_bfs(shortcuts):
    """
    Assuming the snake and ladder board is of size 30.
    Create a graph such that every number 'num' has an outward edge
    going to num+1, num+2, ... num+6.
    Also, if there is a shortcut from 2 to 20, then rather than 1->2,
    have an edge from 1->20 directly.
    Then apply BFS from 1 to 30.
    """
    pass


def main():
    shortcuts = {}
    shortcuts[12] = 18
    shortcuts[3] = 19
    print(snake_ladder_bfs(shortcuts))


main()
