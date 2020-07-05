"""
There are given n ropes of different lengths, we need to connect these ropes into one rope.
The cost to connect two ropes is equal to sum of their lengths.
We need to connect the ropes with minimum cost.

For example if we are given 4 ropes of lengths 4, 3, 2 and 6.
We can connect the ropes in following ways.
1) First connect ropes of lengths 2 and 3. Now we have three ropes of lengths 4, 6 and 5.
2) Now connect ropes of lengths 4 and 5. Now we have two ropes of lengths 6 and 9.
3) Finally connect the two ropes and all ropes have connected.
Total cost for connecting all ropes is 5 + 9 + 15 = 29.
This is the optimized cost for connecting ropes.

Other ways of connecting ropes would always have same or more cost.
For example, if we connect 4 and 6 first (we get three strings of 3, 2 and 10),
then connect 10 and 3 (we get two strings of 13 and 2).
Finally we connect 13 and 2.
Total cost in this way is 10 + 13 + 15 = 38.

SOLUTION:

Either we can do DP of complexity O(n*n) similar to matrix-chaining.

Or in this case even greedy would work:

We can notice that the lengths of the ropes which are picked first are included more than once in total cost.
Therefore, the idea is to connect smallest two ropes first and recur for remaining ropes.
We can do it easily through heap.
Complexity -> O(nlogn)
"""
import heapq


def min_rope_join_cost(ropes):
    pq = []
    for rope in ropes:
        heapq.heappush(pq, rope)
    cost = 0
    while pq:
        first = heapq.heappop(pq)
        if not pq:
            break
        second = heapq.heappop(pq)
        cost += first + second
        heapq.heappush(pq, first + second)
    return cost


def main():
    ropes = [6, 2, 3, 4]
    ans = min_rope_join_cost(ropes)
    print(ans)


main()
