# Caveats:

- A graph without any edges is always bipartite.
- A tree is always bipartite.
- Cycle graphs with an even number of vertices are bipartite.
- We can also use DFS to check instead of BFS.
# TODO: Implement using DFS

# Applications:

## Assignment Problem

- There are a number of agents and a number of tasks.
- Any agent can be assigned to perform any task, incurring some cost that may vary depending on the agent-task assignment.
- It is required to perform all tasks by assigning exactly one agent to each task and exactly one task to each agent in such a way that the total cost of the assignment is minimized.

## Hall's Marriage Theorem

- Imagine two groups; one of n men, and one of n women.
- For each woman, there is a subset of the men, any one of which she would happily marry; and any man would be happy to marry a woman who wants to marry him.
- Consider whether it is possible to pair up (in marriage) the men and women so that every person is happy.

## The Mutilated Chessboard Problem

- Suppose a standard 8x8 chessboard has two diagonally opposite corners removed, leaving 62 squares.
- Is it possible to place 31 dominoes of size 2x1 so as to cover all of these squares?
- It can be solved using Hall's Theorem.

# TODO
https://www.geeksforgeeks.org/graph-coloring-applications/
https://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/
https://www.geeksforgeeks.org/coloring-a-cycle-graph/
https://www.geeksforgeeks.org/mathematics-planar-graphs-graph-coloring/
https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/

General graph coloring checking algorithm is HARD. ;)
