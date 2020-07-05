"""
Find the largest perfect binary subtree that can be obtained by removing any number of nodes.
You need to return the number of nodes in the largest perfect subtree.
A perfect tree is a binary tree where every node has either 1 or 2 children.
And all the leaves are at the same level. (See wikipedia for more info)

SOLUTION:

Let our function take a node as an input and return the height of the largest perfect tree rooted at that node.
How to get that recursively?

ans(node) = min(ans(node.left), ans(node.right)) + 1

Why so? Because, lets say the right subtree has a perfect tree of height 3, and left has a perfect tree of height 2.
Now, at the root node, we can make a perfect tree of height 2 (min of left and right) + 1(self).
Take an example and draw it on paper to understand.
The final answer will be the max of any of the heights so formed on any node.
"""

global_ans = 0


def largest_perfect(root):
    if root is None:
        return 0
    left_ans = largest_perfect(root.l)
    right_ans = largest_perfect(root.r)
    ans = min(left_ans, right_ans) + 1
    global global_ans
    global_ans = max(ans, global_ans)
    return ans


def solution(root):
    largest_perfect(root)
    return (1 << global_ans) - 1

