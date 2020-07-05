'''
Given a string with repeated characters, the task is to rearrange characters in a string so that no two adjacent characters are same.

Examples:

Input: aaabc
Output: abaca

Input: aaabb
Output: ababa

Input: aa
Output: Not Possible

Input: aaaabc
Output: Not Possible

SOLUTION:

The idea is to put the highest frequency character first (a greedy approach).
We use a priority queue (Or Binary Max Heap) and put all characters and ordered by their frequencies (highest frequency character at root).
We one by one take the highest frequency character from the heap and add it to result.

1. Pop from heap twice to get the 2 most frequently occurring characters.
2. Print the 2 characters to the result.
3. Add them both back with after decrementing their frequencies by 1.
4. Repeat the above process until there is only one element in the heap.
5. If at the end, the frequency of that element is > 1, then not possible.
'''
