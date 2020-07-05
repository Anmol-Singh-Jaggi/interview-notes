'''
You are given an input integer 'numCities' and 'threshold'.
One city 'x' is connected to another city 'y' if gcd(x, y) >= 'threshold'.
Cities can range from 1 to numCities.

You will be given queries of the form 'u v', where u and v represent a city index.
You have to tell if u and v are connected.
Note that they need not be directly connected (transtive connections also valid).


SOLUTION:

We can first create the graph with the necessary edges, and then run union-find algo on the inputs 'u' and 'v'.
But how to create the graph??

We can have a nested loop from i = 1 to N and j = i+1 to N, and check if gcd(i, j) >= thresh.
If yes, then add them to the same disjoint set.

But this will be O(n*n*logn) algo.

We can instead do this:

Starting from t = threshold  --> numCities, we can connect the vertices:
(t, 2t)
(2t, 3t)
(3t, 4t)
...


For example, if threshold=5, then for t=5:
(5, 10)
(10, 15)
(15, 20)
....

And for t=6:
(6, 12)
(12, 18)
....

Till t=numCities

The number of edges formed this way will always be O(nlogn), where n = number of cities.

Proof:
n/5 + n/6 + n/7 + ... n/thresh =
n * (1/5 + 1/6 + 1/7 + ... 1/n) =
n * logn
'''
