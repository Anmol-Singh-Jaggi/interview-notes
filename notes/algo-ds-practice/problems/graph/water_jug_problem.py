'''
You are given a m litre jug and a n litre jug.
Both the jugs are initially empty.
The jugs don’t have markings to allow measuring smaller quantities.
You have to use the jugs to measure d litres of water where d is less than n.
(X, Y) corresponds to a state where X refers to amount of water in Jug1 and Y refers to amount of water in Jug2.
Determine the path from initial state (xi, yi) to final state (xf, yf), where (xi, yi) is (0, 0) which indicates both Jugs are initially empty and (xf, yf) indicates a state which could be (0, d) or (d, 0).

The operations you can perform are:

   - Empty a Jug, (X, Y)->(0, Y) Empty Jug 1
   - Fill a Jug, (0, 0)->(X, 0) Fill Jug 1
   - Pour water from one jug to the other until one of the jugs is either empty or full, (X, Y) -> (X-d, Y+d)


Example:
Input : 4 3 2
Output : {(0, 0), (0, 3), (4, 0), (4, 3),
          (3, 0), (1, 3), (3, 3), (4, 2),
          (0, 2)}

SOLUTION 1(BFS):

Basically we are given an initial state (0,0).
And we have to reach the final state (?, d) or (d, ?).
So basically use BFS.

SOLUTION 2 (DP):
At any point, there can be a total of six possibilities:

Empty the first jug completely
Empty the second jug completely
Fill the first jug
Fill the second jug
Fill the water from the second jug into the first jug until the first jug is full or the second jug has no water left
Fill the water from the first jug into the second jug until the second jug is full or the first jug has no water left.

return
(waterJugSolver(0, amt2) or
waterJugSolver(amt1, 0) or
waterJugSolver(jug1, amt2) or
waterJugSolver(amt1, jug2) or
waterJugSolver(amt1 + min(amt2, (jug1-amt1)),
amt2 - min(amt2, (jug1-amt1))) or
waterJugSolver(amt1 - min(amt1, (jug2-amt2)),
amt2 + min(amt1, (jug2-amt2))))

'''
