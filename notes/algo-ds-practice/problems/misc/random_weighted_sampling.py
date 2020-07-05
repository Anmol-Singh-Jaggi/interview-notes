'''
Write a function that returns values randomly, according to their weight.
Suppose we have 3 elements with their weights: A (1), B (1) and C (2).
The function should return A with probability 25%, B with 25% and C with 50% based on the weights.

SOLUTION 1:
We could create a list of numbers according to their weights and then do normal sampling.
For example, [A, B, C, C] and we can just choose a rand number in this.
Space complexity -> O(n*w)
Time complexity -> O(n)

SOLUTION 2:
We can create a list of cumulative weights, and do a linear search in that.
Or even better binary search.
For example:
[1, 2, 4]
If input is 3, then the next bigger element is 4, meaning answer is C.
'''
