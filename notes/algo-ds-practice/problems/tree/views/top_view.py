from ds.tree.binary_tree import BinaryTreeNode as Node
from collections import deque


def get_top_view(root: Node):
    '''
    Very similar to vertical order.
    We just need the first element of every vertical line.
    '''
    top_view = []
    if root is None:
        return []
    xpos = 0
    xpos_nodes_map = {}
    dq = deque()
    dq.append((root, xpos))
    while dq:
        node, xpos = dq.popleft()
        if xpos not in xpos_nodes_map:
            xpos_nodes_map[xpos] = node
        if node.left is not None:
            dq.append((node.left, xpos - 1))
        if node.right is not None:
            dq.append((node.right, xpos + 1))
    keys = sorted(xpos_nodes_map.keys())
    for key in keys:
        top_view.append(xpos_nodes_map[key].data)
    return top_view


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    xpos_nodes_map = {}
    top_view = get_top_view(root)
    print(top_view)


main()
