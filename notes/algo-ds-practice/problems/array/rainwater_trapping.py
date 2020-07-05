'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Examples:

Input: arr[]   = {2, 0, 2}
Output: 2
Structure is like below
| |
|_|
We can trap 2 units of water in the middle gap.

Input: arr[]   = {3, 0, 0, 2, 0, 4}
Output: 10
Structure is like below
     |
|    |
|  | |
|__|_|
We can trap "3*2 units" of water between 3 an 2,
"1 unit" on top of bar 2 and "3 units" between 2
and 4.  See below diagram also.

Input: arr[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
       |
   |   || |
_|_||_||||||
Trap "1 unit" between first 1 and 2, "4 units" between
first 2 and 3 and "1 unit" between second last 1 and last 2.
'''


'''
Solution:

A Simple Solution is to traverse every array element and find the highest bars on left and right sides.
Take the smaller of two heights.
The difference between the smaller height and height of the current element is the amount of water that can be stored in this array element.
Time complexity of this solution is O(n2).

An Efficient Solution is to pre-compute highest bar on left and right of every bar in O(n) time.
Then use these pre-computed values to find the amount of water in every array element.
'''
