"""
Given an array of integers where each element represents the max number of steps that
can be made forward from that element.
The task is to find the minimum number of jumps to reach the end of the array (starting from the first element).
If an element is 0, then cannot move through that element.

Example:
Input:
2
11
1 3 5 8 9 2 6 7 6 8 9
6
1 4 3 2 6 7
Output:
3
2

Explanation:
Testcase 1: First jump from 1st element, and we jump to 2nd element with value 3.
Now, from here we jump to 5h element with value 9. and from here we will jump to last.
"""
