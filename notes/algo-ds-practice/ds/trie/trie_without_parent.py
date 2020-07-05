from ds.trie.trie import Trie, TrieNode, test1, test2


# remove() does not use 'parent' field in this implementation.
# Only change in `remove()` method.
class TrieWithoutParent(Trie):
    def _remove(self, word, curr_node: TrieNode, word_idx):
        if word_idx == len(word):
            if not curr_node.is_end:
                # word not found!
                return curr_node
            curr_node.is_end = False
            if curr_node.is_leaf():
                # We can delete this node.
                return None
            return curr_node
        curr_char = word[word_idx]
        if curr_char not in curr_node.children:
            return curr_node
        old_child_node = curr_node.get_child(curr_char)
        new_child_node = self._remove(word, old_child_node, word_idx + 1)
        if new_child_node is None:
            # The child node was removed.
            curr_node.remove_child(curr_char)
        else:
            curr_node.set_child(curr_char, new_child_node)
        if curr_node.is_leaf() and not curr_node.is_end:
            # The current node can be deleted too!
            return None
        return curr_node

    def remove(self, word):
        self._remove(word, self.root, 0)


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
