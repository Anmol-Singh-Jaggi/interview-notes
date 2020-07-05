'''
Given a graph and two vertices src and dest, count the total number of walks from src to dest where the length of the path is k (there should be exactly k edges between them).

Note that "walk" is different from "path"; walks can repeat edges and vertices.

SOLUTION 1:
Brute force:
Start from u, go to all adjacent vertices and recur for adjacent vertices with k as k-1, source as adjacent vertex and destination as v.

int countwalks(int graph[][V], int u, int v, int k)
{
   if (k == 0 && u == v)      return 1;
   if (k == 1 && graph[u][v]) return 1;
   if (k <= 0)                return 0;
   int count = 0;
   for (int i = 0; i < V; i++)
       if (graph[u][i] == 1)
           count += countwalks(graph, i, v, k-1);
   return count;
}


The worst case time complexity of the above function is O(V**k) where V is the number of vertices in the given graph.
We can simply analyze the time complexity by drawing recursion tree.
The worst occurs for a complete graph.
In worst case, every internal node of recursion tree would have exactly n children.


SOLUTION 2:
DP
We can optimize the above solution using Dynamic Programming.
The idea is to build a 3D table where first dimension is source,
second dimension is destination, third dimension is number of edges from source to destination,
and the value is count of walks.

Complexity -> O(V**3 * K)

int countwalks(int graph[][V], int u, int v, int k)
{
    int count[V][V][k+1];
    for (int e = 0; e <= k; e++) // for num edges
    {
        for (int i = 0; i < V; i++)  // for source
        {
            for (int j = 0; j < V; j++) // for destination
            {
                // initialize value
                count[i][j][e] = 0;

                // from base cases
                if (e == 0 && i == j)
                    count[i][j][e] = 1;
                if (e == 1 && graph[i][j])
                    count[i][j][e] = 1;

                // go to adjacent only when number of edges is more than 1
                if (e > 1)
                {
                    for (int a = 0; a < V; a++) // adjacent of source i
                        if (graph[i][a])
                            count[i][j][e] += count[a][j][e-1];
                }
           }
        }
    }
    return count[u][v][k];
}


SOLUTION 3:

There is cool trick to do this.
If G is the adjacency matrix, then the [u][v] cell in the matrix G^k will be our answer.
Complexity -> O(V^3 logk).
It takes V^3 to multiply a matrix of size V*V.
And we will multiply log(k) times.

Proof:
See https://cp-algorithms.com/graph/fixed_length_paths.html
'''
