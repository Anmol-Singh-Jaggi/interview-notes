from ds.tree.binary_tree import BinaryTreeNode
from ds.tree.tree_core import Tree


class BSTNode(BinaryTreeNode):
    def insert(self, data):
        '''
        Duplicates not allowed.
        '''
        if self.data == data:
            return self
        if data < self.data:
            if self.get_left_child() is None:
                left_child_node = BSTNode(data)
                self.set_left_child(left_child_node)
            return self.get_left_child().insert(data)
        if data > self.data:
            if self.get_right_child() is None:
                right_child_node = BSTNode(data)
                self.set_right_child(right_child_node)
            return self.get_right_child().insert(data)
        # Shouldn't reach here at all
        raise RuntimeError("Unknown error during insert!")

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data and self.get_left_child():
            return self.get_left_child().search(data)
        if data > self.data and self.get_right_child():
            return self.get_right_child().search(data)
        return None

    def _find_smallest(self):
        '''
        Return the smallest node by value in the tree rooted by `self`.
        '''
        left_child = self.get_left_child()
        if not left_child:
            return self
        return left_child._find_smallest()

    def remove(self, data):
        if data < self.data:
            left_child = self.get_left_child()
            if left_child:
                left_child = left_child.remove(data)
                if left_child:
                    self.set_left_child(left_child)
            return self
        if data > self.data:
            right_child = self.get_right_child()
            if right_child:
                right_child = right_child.remove(data)
                self.set_right_child(right_child)
            return self
        if data == self.data:
            # If either of the children are missing, then its simple.
            left_child = self.get_left_child()
            right_child = self.get_right_child()
            if left_child is None:
                return right_child
            if right_child is None:
                return left_child
            # This node is having both the children.
            # Find smallest node in the right subtree and replace
            # the current node with it.
            # We could have also chosen the max element in left subtree.
            smallest_right_subtree = self.get_right_child()._find_smallest()
            # Call a remove() on the right subtree so that the smallest
            # node's parent will not point to it anymore.
            # It will rather point to smallest node's right subtree.
            right_child = right_child.remove(smallest_right_subtree.data)
            self.set_right_child(right_child)
            self.data = smallest_right_subtree.data
            return self
        raise RuntimeError("Unknown error during remove!")


class BinarySearchTree(Tree):
    # CAREFUL: Its best to implement the methods on the
    # node class rather than the tree class.
    def insert(self, data):
        '''
        Insert a new node with this data.
        Does not overwrite if it exists already.
        Returns the node inserted/present.
        '''
        if self.root:
            return self.root.insert(data)
        else:
            self.root = BSTNode(data)
            return self.root

    def search(self, data):
        '''
        Returns the node having this data, else None
        '''
        if self.root is None:
            return None
        else:
            return self.root.search(data)

    def remove(self, data):
        '''
        Removes the node having this data.
        '''
        if self.root:
            self.root = self.root.remove(data)


def main():
    bst = BinarySearchTree(None)
    bst.insert(50)
    bst.insert(40)
    bst.insert(100)
    bst.insert(150)
    print(bst)
    bst.remove(50)
    print(bst)


if __name__ == "__main__":
    main()
