# Telephonic

## Problem 1:
- Given a string of the form `b*a*c*`, like `bbbbaaaaaccc`, find the count of a.
- Used binary search.

## Problem 2:
- Given a modified binary tree such that one node has 2 parents, find such a node.
- https://leetcode.com/problems/redundant-connection/
- Used DFS and hashmap. 

# Round 1

## Problem 1:
- Given a directed graph with n vertices and m edges, find if you can reach (n-1,n-1) from (0,0).
  But there is a twist; apart from the m edges given in the input, every vertex also has a mapping (x, y) signifying that there is now a new edge x-y.
  For example, if n=5 and the input edges are 0->1 and 1->3, and vertex 2 contains the mapping 1->4, then the answer is NO.
  This is because we will never be able to reach vertex 2 from 0 and unlock the new edge.
- Solved using DFS + Disjoint-set (although now I think Disjoint set is not required).
- We can simply use DFS:
  - Lets say we detect a new edge `[x, y]`. Now there can be following possibilities:
   - x and y are both visited => Ignore.
   - x is visited but y partially visited (being visited right now) => Ignore.
   - x and y are both partially visited => Ignore.
   - x is visited and y is unvisited => Add y to x's neighbour list and add x back to to-be-explored list.
   - x is visiting and y is unvisited => Add y to x's neighbour list; it will be visited later automatically.
   - x and y are both unvisited => Add y to x's neighbour list.
- Using disjoint-set can however result in a slight optimization; consider that we have edges 1<->2<->3<->4, where all these vertices are in the unvisited set.
- Now if we notice that 1 and 4 are connected later on, we can simply ignore that rather than adding a new edge between them. And we will need disjoint set to detect this.
- Another case where this optimization can happen is this: Imagine vertices 1, 2, 3 are visited.
- Now we notice that 2 and 4 are connected; we add a new edge.
- Later we notice that 3 and 4 are connected; we can detect that adding a new edge would be redundant now.
- Note that all these optimizations will not result in the reduction of algorithmic complexity compared to plain DFS.

# Round 2

## Problem 1:
- Given an array of integers, find if there is a subsequence whose (sum modulo n) = 0, where n is the size of the array.
- Solved using DP O(N*N).
- We will create a boolean dp array of size n.
- Lets say we are at index i. In such a case`dp[j]` signifies whether there exists a subsequence from index 0 to i-1, whose sum modulo n is j.
- Now, for the index i, we'll just repopulate dp by marking `(arr[i] + dp[j]) % n` index of dp to be true.
- But the interviewer wanted a better solution.
- He later asked me to find a subarray whose sum modulo n is 0. I did it with simple O(N) hashing.
- He then concluded that for any array, the answer is always going to be true.
- That is, in any array, there always exists a subsequence whose sum modulo n is 0.
- So this was a trick question kind of.

## Problem 2:
- Given a complete binary tree (just like a heap), insert a new node into while maintaing the complete binary tree invariant.
- Solved it in O(n) first, where n is the size of the tree. Dont remember exactly how I solved it.
- Then solved it using O(logn).
- At every node, first compute the depth of the leftmost node and the rightmost node rooted from the left and right child.
- So we'll have four numbers - ll, lr, rl, rr.
- If ll == lr, that means left child is completely balanced, now recurse for right.
- There is one edge case; what if all levels are filled; now we need to add a new level; this can be easily covered in O(logn) also.

# Round 3

## Problem 1
- There is a tournament happening.
- We are given data like `1->2`, `4->5` etc..
- This means that person 1 defeated 2 and 4 defeated 5.
- Given such data, tell the global relationship between every one.
- Note that the global relationship is valid only if there is no ambiguity.
- For example, in the above example, there is ambiguity between 1 and 4.
- So the answer in above case is None.
- But for example, `1->2` and `2->3`; in this case the final answer is `1->2->3`.
- Solved it using topological sort (Kahns algo).
- The ambiguity case can be easily detected by checking the size of the 0-indegree queue; if the size is > 1 at any point of time, then there is an ambiguity.

## Problem 2
- Given an array of numbers and another number M, find maximum X such that `foo(X)` <= M.
- `foo(X) = sum of min(arr[i], X) for all i`.
- Solved it by binary searching for the answer.
- Let the current candidate for X be x.
- Then how to find out foo(x)??
- Just sort the input array, and compute the cumulative sum in the beginning itself.
- Then do an upper bound for X on the input array `arr`.
- Then `foo(x) = cumsum[ub-1] + x*(size-i)`, where `cumsum` is the cumulative sum array, `ub` is the upper bound of `x` on `arr`, and size is the number of elements.
- Final complexity = O(nlogn) + O(logM * logN).
- Interviewer was expecting something better though.

# Round 4

# Problem 1
- Given a matrix of positive integers and -1's, where -1 signify a bloackage, find the max sum path from anywhere to anywhere.
- Basically we'll divide the matrix into multiple connected components, where each of those components is actually a tree rather than graph.
- Then we can find the max sum path in the trees separately and return the max of them.
- Now how to find the max sum path in an n-ary tree??
- Just like in binary tree, use DP.
- Select any random node as the root, and get the answers for all the children.
- Now, the children will return 2 things:
  - Max sum path from root to any leaf = ans1
  - Max sum path from anywhere to anywhere in that subtree = ans2
- We can combine ans1 and ans2 to compute answer for the root node recursively by choosing max(top 2 ans1's + root.val, ans2).
- Complexity -> O(MN).
- https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/434281/Java-or-DFS-or-O(m*n)-Time-and-Space
- https://leetcode.com/problems/path-with-maximum-gold/discuss/?currentPage=1&orderBy=most_votes&page=2&query=

```
/*
ans(node) = Max path from 1 leaf to another in this subtree
dp1(node) = Max path from 1 leaf to another leaf in this subtree excluding this node
dp2(node) = Max path from 1 leaf to another leaf in this subtree including this node
dp3(node) = Max path from this node to any of its leaves
*/

/*
dp2A = largest dp2 of all the children
dp2B = second largest ...
*/


dp1(node) = Max(ans(c1), ans(c2) ....)
dp2(node) = value(node) + dp3A + dp3B
ans = max(dp1, dp2)
dp3 = max(dp3 of all children) + value(node)
return ans, dp3
```