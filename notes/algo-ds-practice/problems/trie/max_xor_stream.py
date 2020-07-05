'''
You are given a number of queries Q and each query will be of the following types:

Query 1 : add(x) This means add x into your data structure.
Query 2 : maxXOR(y) This means print the maximum possible XOR of y with all the elements already stored in the data structure.
1 <= x, y <= 10^9
1 <= 10^5 <= Q
The data structure begins with only a 0 in it.

Example:

Input: (1 10), (1 13), (2 10), (1 9), (1 5), (2 6)
Output: 7 15

Add 10 and 13 to stream.
Find maximum XOR with 10, which is 7
Insert 9 and 5
Find maximum XOR with 6 which is 15.

SOLUTION:
Lets say all number are represented using 32 bits.
Then when we are to add a number, then add its binary representation in the trie.
When we want to find maxXor of a number x, then start traversing through the trie trying our best to
visit the bit which is the opposite of the bit of 'x'.
For example if 'x' is 1010.
Then in the trie, we'll try to visit in the order '0101' so that the final xor becomes '1111'.
If at a step opposite bit is not available, then we'll have to obviously visit through the same bit.
'''
