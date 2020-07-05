'''
Given a sorted dictionary of an alien language having N words,
the task is to return the order of characters in the language.
Note: Many orders may be possible for a particular test case, thus you may return any valid order.

Examples:

Input:  Dictionary = { "baa", "abcd", "abca", "cab", "cad" }
Output: b, d, a, c
Note that words are sorted and in the given language "baa" comes before "abcd",
therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Input: Dictionary = { "caa", "aaa", "aab"
Output: c, a, b
'''

from ds.graph.graph_core import GraphCore
from problems.graph.standard.topo_sort.topo_sort import topo_sort


def compare_words(word1, word2, graph: GraphCore):
    idx1 = 0
    idx2 = 0
    while idx1 < len(word1) and idx2 < len(word2):
        char1 = word1[idx1]
        char2 = word2[idx2]
        if char1 == char2:
            idx1 += 1
            idx2 += 1
            continue
        graph.add_edge(char1, char2)
        break


def get_char_order(words):
    graph = GraphCore(False)
    for i in range(len(words) - 1):
        compare_words(words[i], words[i + 1], graph)
    print(graph)
    return topo_sort(graph)
