# Floyd Warshall explanation

Lets say we are computing `dp[5][8]` when `k` = 2.<br>
`dp[5][8] = dp[5][2] + dp[2][8]`<br>
According to the algorithm spec, we have found the shortest distance from vertex 5 to 8 considering the intermediate vertices 1 and 2. You might be thinking that we missed some paths like `dp[5][1] + dp[1][2] + dp[2][8]` or `dp[5][2] + dp[2][1] + dp[1][8]`.<br>
But no; actually we have covered both of them. This is how:

We already checked the path `dp[5][1] + dp[1][2]` while computing `dp[5][2]` for k=1.<br>
We already checked the path `dp[5][2] + dp[2][1]` while computing `dp[5][1]` for k=2.

The wikipedia explanation is pretty good too.

# Caveats

- Works with negative edges.
- Works with negative cycles; Will detect cycle; `dp[x][x]` will be negative rather than 0\. So just check the diagonal matrix.
- Works for both directed and undirected.
- Unweighted graph does not make sense, but it will still work obviously.
