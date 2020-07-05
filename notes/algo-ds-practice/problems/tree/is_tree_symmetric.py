"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3



But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

"""
from collections import deque


def is_mirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    ans3 = root1.val == root2.val
    ans1 = is_mirror(root1.left, root2.right)
    ans2 = is_mirror(root1.right, root2.left)
    return ans1 and ans2 and ans3


def isSymmetric(root):
    if root is None:
        return True
    return is_mirror(root.left, root.right)


def is_symmetric_iterative(root):
    dq = deque()
    dq.append(root)
    dq.append(root)
    while dq:
        t1 = dq.pop()
        t2 = dq.pop()
        if t1 is None and t2 is None:
            continue
        if t1 is None or t2 is None:
            return False
        if t1.val != t2.val:
            return False
        dq.append(t1.left)
        dq.append(t2.right)
        dq.append(t1.right)
        dq.append(t2.left)
    return True
