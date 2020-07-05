'''
Given an array of words, find all shortest unique prefixes to represent each word in the given array.
Assume that no word is prefix of another.

Examples:

Input: arr[] = {"zebra", "dog", "duck", "dove"}
Output: dog, dov, du, z
Explanation: dog => dog
             dove = dov
             duck = du
             z   => zebra

Input: arr[] =  {"geeksgeeks", "geeksquiz", "geeksforgeeks"};
Output: geeksf, geeksg, geeksq}

SOLUTION:

Use a trie.
Insert all the words in a trie.
While inserting words, keep a count of how many times a trie node has been visited.
Keep incrementing the node's frequency on very visit.

Then for every word, traverse the trie; as soon as we find the first node with freq=1, then stop;
we've found the prefix for this word.
'''
