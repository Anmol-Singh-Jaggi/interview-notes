'''
Given a sorted array of integers with size n, find if there exists a number that is repeated at least n/4 times.

Solution:

This can be done in O(4*log(n)).

One by one go to indices i/4, 2*i/4 ... and do a lower bound for this element.
Let this index be `lb`. Now check if index `lb + n/4` is also having this element.
If yes, then this is it.


**Example:**

Lets say n = 40.

The groups are:
- 1 - 10
- 11 - 20
- 21 - 30
- 31 - 40

We'll search at the indices 10, 20, 30, 40.
'''
