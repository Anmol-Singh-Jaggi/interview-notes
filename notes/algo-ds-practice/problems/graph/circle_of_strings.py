"""
Given an array of strings A[], determine if the strings can be chained together to form a circle.
A string X can be chained together with another string Y if the last character of X is same as first character of Y.
If every string of the array can be chained, it will form a circle.

For eg
for the array arr[] = {"for", "geek", "rig", "kaf"}
the answer will be Yes as the given strings can be chained as "for", "rig", "geek" and "kaf".

SOLUTION 1:
Brute force (Backtracking)

SOLUTION 2:
Create a directed graph such that for every word `abc`, there is an edge from vertex 'a' -> 'c'.
Now just check if this graph has an eulerian circuit or not.
To do this, just check that for every vertex in-degree == out-degree.
Also, start dfs from any vertex (with non zero in and out degrees) and do a DFS.
If DFS covers all nodes, means its connected, meaning it is an eulerian graph.

SOLUTION 3:
Create a directed graph between words (word is a node).
Now check if there is a hamiltonian circuit.
But checking if a graph is hamiltonian is NP complete. So no point!
"""


def is_circle_possible(strs):
    words_mapping = {}
    for str in strs:
        words = words_mapping.get(str[0], [])
        words_mapping[str[0]] = words
        words.append(str)
    circle = []
    for word in strs:
        ret = dfs(word, words_mapping, len(strs), circle)
        if ret:
            return circle
    return None


def dfs(word, mapping, num_words_total, circle):
    # CAREFUL: We cannot use a visited set() as there can be duplicate
    # words in the input array.
    # Example - ['aa', 'aa']
    mapping[word[0]].remove(word)
    circle.append(word)
    if len(circle) == num_words_total and word[-1] == circle[0][0]:
        return True
    last_char = word[-1]
    for neigh in mapping.get(last_char, []):
        ret = dfs(neigh, mapping, num_words_total, circle)
        if ret:
            return True
    circle.pop()
    mapping[word[0]].append(word)
    return False


def main():
    words = ["for", "geek", "rig", "kaf"]
    words = ["ceee", "eeece", "ddbc"]
    # words = ['ab', 'bc', 'cd', 'da']
    # words = ['abc', 'bcd', 'cdf']
    words = ["dedce", "cdcae", "debdc", "d", "abde"]
    words = ["e", "e"]
    ans = is_circle_possible(words)
    print(ans)


main()
