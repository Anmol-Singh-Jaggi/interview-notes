from ds.tree.tree_core import TreeNode, Tree


class TrieNode(TreeNode):
    def __init__(self, data=None):
        self.children = {}
        self.parent = None
        # End-of-word
        self.is_end = False
        self.data = data

    def __str__(self):
        return super().__str__().replace('TreeNode', 'TrieNode', 1)

    def _get_label(self):
        if self.is_end:
            return self.data + ';'
        else:
            return self.data

    def _get_all_words(self, prefix):
        result_set = []
        if self.is_end:
            result_set.append(prefix)
        for child_char, child_node in self.get_children_sorted():
            if child_node:
                result_set.extend(
                    child_node._get_all_words(prefix + child_char))
        return result_set


class Trie(Tree):
    def __init__(self):
        self.root = TrieNode('/')
        self.num_words = 0

    def get_num_words(self):
        return self.num_words

    def search(self, word):
        current_node = self.root
        char_idx = 0
        while True:
            if char_idx == len(word):
                if current_node.is_end:
                    return True
                return False
            char = word[char_idx]
            child_node = current_node.get_child(char)
            if child_node is None:
                return False
            char_idx += 1
            current_node = child_node

    def insert(self, word):
        current_node = self.root
        char_idx = 0
        while True:
            if char_idx == len(word):
                if not current_node.is_end:
                    current_node.is_end = True
                    self.num_words += 1
                return
            char = word[char_idx]
            child_node = current_node.get_child(char)
            if child_node is None:
                # Insert a new node and continue the loop
                child_node = TrieNode(char)
                current_node.set_child(char, child_node)
            char_idx += 1
            current_node = child_node

    def _remove_leaf(self, leaf_node):
        '''
        Remove the necessary ancestor nodes of a leaf
        while deleting a word.
        '''
        if leaf_node is None:
            return
        current_node = leaf_node
        current_node.is_end = False
        while True:
            if current_node.is_end or (not current_node.is_leaf()):
                # Dont delete this node if it is the end of some other word
                # or it still has some other children left
                break
            parent_node = current_node.parent
            if parent_node is None:
                break
            parent_node.remove_child(current_node.data)
            current_node = parent_node

    def remove(self, word):
        current_node = self.root
        char_idx = 0
        while True:
            if char_idx == len(word):
                if current_node.is_end and current_node.is_leaf():
                    self._remove_leaf(current_node)
                    self.num_words -= 1
                return
            char = word[char_idx]
            child_node = current_node.get_child(char)
            char_idx += 1
            if child_node is None:
                continue
            current_node = child_node

    def _search_prefix(self, word):
        '''
        Search for the word in the trie.
        If not found, search until the longest
        prefix found and return that.
        '''
        current_node = self.root
        char_idx = 0
        prefix = ''
        while True:
            if char_idx == len(word):
                break
            char = word[char_idx]
            child_node = current_node.get_child(char)
            if child_node is None:
                break
            char_idx += 1
            prefix += char
            current_node = child_node
        return (current_node, prefix)

    def get_auto_complete(self, word, strict=True):
        '''
        Find all the words having `word` as the prefix.
        `strict=False` => The prefix will keep getting more
        unrestrictive(shorter) until it is found that there are
        some words containing that prefix.
        'abcd' -> 'abc' -> 'ab' > 'a' > ''
        It might result in getting all the words being returned
        (when the prefix finally gets shortened to '')
        '''
        prefix_nearest_node, prefix = self._search_prefix(word)
        if strict and prefix is not word:
            return []
        return prefix_nearest_node._get_all_words(prefix)

    def get_all_words(self):
        return self.get_auto_complete('')


def test1():
    trie1 = Trie()
    trie1.insert('abcdef')
    trie1.insert('abcgef')
    trie1.insert('abcdefgh')
    trie1.insert('angoh')
    trie1.insert('ang')
    print(trie1)
    print(trie1.get_num_words())
    print(trie1.search('abcdef'))
    print(trie1.search('abcdefg'))
    print(trie1.search('abcdefgh'))
    trie1.remove('abcdef')
    trie1.remove('abcdefgh')
    trie1.remove('angoh')
    print(trie1.search('angoh'))
    print(trie1.search(''))
    trie1.insert('')
    print(trie1.search(''))
    print(trie1.search('ang'))
    print(trie1)
    print(trie1.get_num_words())


def test2():
    trie1 = Trie()
    trie1.insert('abcdef')
    trie1.insert('abcgef')
    trie1.insert('abcdefgh')
    trie1.insert('angoh')
    trie1.insert('ang')
    trie1.insert('bcd')
    trie1.insert('bxy')
    results = trie1.get_auto_complete('am', False)
    print(results)
    print(trie1.get_all_words())


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
