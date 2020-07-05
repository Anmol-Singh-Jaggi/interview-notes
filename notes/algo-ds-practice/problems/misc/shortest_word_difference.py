'''
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.
Your method will be called repeatedly many times with different parameters.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3

Input: word1 = "makes", word2 = "coding"
Output: 1

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

SOLUTION:

Basically for every word in the dictionary, keep a list of sorted indices.
Following that, the problem is reduced to just finding a pair of numbers of 2 lists such that their absolute difference is minimum, which can be done in O(n).

For example,
indices of word1:
0, 3, 7
indices of word2:
2, 5
Keep a pointer i=0 for list1 and j=0 for list2.
Compare the 2 numbers and update the global minima.
Then increment the lower of the 2 values.
'''
