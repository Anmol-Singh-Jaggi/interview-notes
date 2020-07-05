# Caveats

- Does not work with negative edges.
- Can we fix it by adding a constant value to all the edges so that no edge is negative?? **NO**: 

  > Adding a weight to every edge adds more weight to long paths than short paths. (Long in the sense of having many edges.) For example, suppose the lowest-cost edge has weight -2 and there are two paths from a to b: a single edge of weight 3 and a path with two edges, each of weight 1\. The two-edge path has the lowest weight. However, if you add 2 to every edge, the one-edge path has weight 5 but the three-edge path now has weight 6, so you get the wrong answer.

- Works for both directed and undirected.
- Unweighted graph does not make sense, but it will still work obviously.
- It is actually a greedy algo, not DP!!
