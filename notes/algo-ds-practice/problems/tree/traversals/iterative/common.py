from ds.tree.binary_tree import BinaryTreeNode as Node
from collections import deque


def inorder_iterative(root: Node):
    '''
    Maintain a stack where one entry is <node, count>.
    count is the number of times this node has been seen throughout the loop.
    '''
    stack = deque()
    stack.append([root, 0])
    traversal = []
    while stack:
        top_node, top_count = stack[-1]
        if top_node is None:
            stack.pop()
            continue
        stack[-1][1] += 1
        if top_count == 0:
            # Seeing it for the first time.
            stack.append([top_node.left, 0])
        elif top_count == 1:
            # Seeing it for the second time.
            traversal.append(top_node)
            stack.pop()
            stack.append([top_node.right, 0])
    return traversal


def preorder_iterative(root: Node):
    '''
    Almost same as inorder_iterative.
    '''
    stack = deque()
    stack.append([root, 0])
    traversal = []
    while stack:
        top_node, top_count = stack[-1]
        if top_node is None:
            stack.pop()
            continue
        stack[-1][1] += 1
        if top_count == 0:
            # Seeing it for the first time.
            traversal.append(top_node)
            stack.append([top_node.left, 0])
        elif top_count == 1:
            # Seeing it for the second time.
            stack.pop()
            stack.append([top_node.right, 0])
    return traversal


def postorder_iterative(root: Node):
    '''
    Almost same as inorder_iterative.
    '''
    stack = deque()
    stack.append([root, 0])
    traversal = []
    while stack:
        top_node, top_count = stack[-1]
        if top_node is None:
            stack.pop()
            continue
        stack[-1][1] += 1
        if top_count == 0:
            # Seeing it for the first time.
            stack.append([top_node.left, 0])
        elif top_count == 1:
            # Seeing it for the second time.
            stack.append([top_node.right, 0])
        else:
            traversal.append(top_node)
            stack.pop()
    return traversal


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)
    order = inorder_iterative(root)
    print(order)
    order = preorder_iterative(root)
    print(order)
    order = postorder_iterative(root)
    print(order)


main()
