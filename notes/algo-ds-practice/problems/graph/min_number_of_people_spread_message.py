'''
Considering that I'ld would like to spread a promotion message across all people in twitter. Assuming the ideal case, if a person tweets a message, then every follower will re-tweet the message.

You need to find the minimum number of people to reach out (for example, who doesn't follow anyone etc) so that your promotion message is spread out across entire network in twitter.

Also, we need to consider loops like, if A follows B, B follows C, C follows D, D follows A (A -> B -> C -> D -> A) then reaching only one of them is sufficient to spread your message.

Input: A 2x2 matrix like below. In this case, a follows b, b follows c, c follows a.

    a b c
a  1 1 0
b  0 1 1
c  1 0 1

Output: List of people to be reached to spread out message across everyone in the network.

SOLUTION:

1. Find Strongly Connected Components.
2. Make a condensation graph such that one node in the new graph represents one component.
3. The number of vertices with 0 in-degree in the condensation graph is our answer.

ALTERNATE:

1. Find a vertex whose out-degree is 0.
2. Then run a DFS from that and mark all vertices.
3. Keep doing this until there are no more vertices with 0 in-degree.
4. answer = Number of times dfs was run.
5. Now if there are any remaining vertices, it means that they must be in a cycle.
6. Find the number of cycles in the remaining vertices by running DFS's from any random node.
7. answer += the number of times DFS was run in the above step.
'''
