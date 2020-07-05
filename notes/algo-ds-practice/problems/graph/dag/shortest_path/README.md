We can compute the shortest paths for a DAG with the exact same algorithms that we used for computing the longest path.
That is:
1. Using topo sort.
2. DP.
3. Negation.

We just need to replace `max()` with `min()` and `-inf` with `inf` everywhere.
