'''
A 2d grid map of m rows and n columns is initially filled with water.
We may perform an `addLand` operation which turns the water at position (row, col) into a land.
Given a list of positions to operate, count the number of islands after each addLand operation.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example:
Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0

Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0

Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0

Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0

Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0

We return the result as an array: [1, 1, 2, 3]

SOLUTION:

Case 1:
The new found land has no neighbouring land vertices at all.
In this case, num_islands++ since this is a new island of its own.

Case 2:
The new land has just 1 neighbouring land vertex.
That means it will be merged into that island.
Meaning no change in num_islands.

Case 2:
2 or more neighbouring lands.
In this case, it might happen that those 2 vertices are connected using some other path.
Or it can happen that they are not connected.
If they are connected already, then it means no change in num_islands.
However, if they were not connected, then num_islands--.

So, for this problem, we'll need to know whether any 2 land vertices are connected already or not.
Which means we can use union-find.

For every new-land, just union all the neighbouring land vertices together with this new land vertex.
At the end, just return the number of disjoint sets.
'''
