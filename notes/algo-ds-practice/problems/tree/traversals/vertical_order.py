from ds.tree.binary_tree import BinaryTreeNode as Node
from collections import deque


def get_vertical_order(root: Node):
    vertical_order = []
    if root is None:
        return []
    xpos = 0
    xpos_nodes_map = {}
    dq = deque()
    dq.append((root, xpos))
    # Doing level-order traversal basically.
    while dq:
        node, xpos = dq.popleft()
        nodes = xpos_nodes_map.get(xpos, [])
        xpos_nodes_map[xpos] = nodes
        nodes.append(node)
        if node.left is not None:
            dq.append((node.left, xpos - 1))
        if node.right is not None:
            dq.append((node.right, xpos + 1))
    keys = sorted(xpos_nodes_map.keys())
    for key in keys:
        vertical_order.extend(xpos_nodes_map[key])
    return vertical_order


def get_vertical_order_wrong(root: Node, xpos, xpos_nodes_map):
    '''
    This will give wrong answer!!
    Sample:
            1
          2   3
        5   4
          6
            7
              8
                9
                  10
    It will print 7 before 4 !!
    '''
    if root is None:
        return
    nodes = xpos_nodes_map.get(xpos, [])
    xpos_nodes_map[xpos] = nodes
    nodes.append(root)
    get_vertical_order_wrong(root.left, xpos - 1, xpos_nodes_map)
    get_vertical_order_wrong(root.right, xpos + 1, xpos_nodes_map)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    vertical_order = get_vertical_order(root)
    vertical_order = [node.data for node in vertical_order]
    print(vertical_order)


main()
