'''
Given a string of length n of lowercase alphabet characters, we need to count total number of distinct substrings of this string.
Examples:

Input  : str = “ababa”
Output : 10
Total number of distinct substring are 10, which are,
"", "a", "b", "ab", "ba", "aba", "bab", "abab", "baba"
and "ababa".

SOLUTION 1:

Generate all the substrings, and use hash map.
Complexity -> O(n*n)

SOLUTION 2:
Insert all the suffixes of the word into a trie.
The total number of nodes in the trie would be our answer.
Complexity -> O(n*n)
But the space Complexity would be lower on average than hashmap.
Also, no scope of collisions so time Complexity would also be practically faster.
'''
