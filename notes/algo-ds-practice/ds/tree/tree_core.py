from functools import total_ordering


@total_ordering
class TreeNode:
    """
    General purpose multi-children Tree Node class.
    """

    def __init__(self, data):
        self.children = {}
        self.parent = None
        self.data = data

    def __repr__(self) -> str:
        parent = self.parent
        parent_data = None
        if parent:
            parent_data = parent.data
        return "TreeNode:\nData={}\nParent={}\nChildren={}\n-----".format(
            self.data, parent_data, len(self.children)
        )

    def __hash__(self):
        return super().__hash__()

    def _get_label(self):
        return self.data

    def set_child(self, key, node):
        """
        Does not make a copy of the input node!
        Modifies its 'parent' field.
        """
        self.children[key] = node
        if node:
            node.parent = self

    def get_child(self, key):
        """
        Returns None if the child does not exist!
        """
        return self.children.get(key, None)

    def remove_child(self, key):
        del self.children[key]

    def is_leaf(self):
        """
        Probably will need to override this for different contexts.
        """
        return not self.children

    def _get_size_of_tree_recursive(self):
        num_children = 0
        for child in self.children.values():
            if child is not None:
                num_children += child._get_size_of_tree_recursive()
        return num_children + 1

    def size(self):
        return self._get_size_of_tree_recursive()

    def display(self):
        indentation = 4
        return self._display("", True, True, indentation)

    def get_children_sorted(self):
        keys_sorted = sorted(self.children.keys())
        values = []
        for key in keys_sorted:
            values.append((key, self.children[key]))
        return values

    def _display(self, prefix, is_tail, even_child, indentation):
        """
        `is_tail` is required to prevent a `|` before the last child.
        `even_child` signifies that this child was a left child.
        This is only used in case of differentiating between left and
        right children during pretty printing binary trees.
        """
        symbol = "|" + "-" * (indentation - 1)
        spaces = " " * indentation
        filler = symbol.replace("-", " ")
        if even_child:
            symbol = "|" + "+" * (indentation - 1)
        output = prefix + symbol + str(self._get_label()) + "\n"
        child_prefix = prefix + (spaces if is_tail else filler)
        if is_tail and not self.children:
            output += prefix + "\n"
        children_sorted = self.get_children_sorted()
        for i in range(len(children_sorted) - 1):
            child_key, child = children_sorted[i]
            if child is not None:
                even_child = (
                    False if (isinstance(child_key, int) and (child_key & 1)) else True
                )
                output += child._display(child_prefix, False, even_child, indentation)
            else:
                output += child_prefix + symbol + "None\n"
        if self.children:
            child_key, last_child = children_sorted[-1]
            if last_child is not None:
                even_child = (
                    False if (isinstance(child_key, int) and (child_key & 1)) else True
                )
                output += last_child._display(
                    child_prefix, True, even_child, indentation
                )
            else:
                output += child_prefix + symbol + "None\n"
        return output

    def _is_valid_operand(self, other):
        return hasattr(other, "data")

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.data == other.data

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.data < other.data


class Tree:
    def __init__(self, root):
        self.root = root

    def __str__(self):
        if self.root is None:
            return "Root none!!"
        return self.root.display()

    def get_root(self):
        return self.root

    def size(self, verify=False):
        return self.root.size()


def main() -> None:
    root = TreeNode(1)

    root.set_child(0, TreeNode(2))
    root.set_child(1, TreeNode(3))
    root.set_child(2, TreeNode(100))

    root.get_child(0).set_child(0, TreeNode(4))
    root.get_child(0).set_child(1, TreeNode(5))
    root.get_child(1).set_child(0, TreeNode(6))
    root.get_child(1).set_child(1, TreeNode(7))
    root.get_child(2).set_child(0, TreeNode(7))
    root.get_child(1).get_child(0).set_child(1, TreeNode(100))
    root.get_child(1).get_child(1).set_child(0, TreeNode(100))

    tree1 = Tree(root)

    print(tree1)
    print(tree1.size())


if __name__ == "__main__":
    main()
