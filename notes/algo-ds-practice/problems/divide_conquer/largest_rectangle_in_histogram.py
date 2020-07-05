'''
Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars.
For simplicity, assume that all bars have same width and the width is 1 unit.

For example, consider the following histogram with 7 bars of heights {6, 2, 5, 4, 5, 2, 6}.
The largest possible rectangle possible is 12.

SOLUTION 1:
A simple solution is to one by one consider all bars as starting points and calculate area of all rectangles starting with every bar.
Finally return maximum of all possible areas.
Time complexity of this solution would be O(n^2).

SOLUTION 2:
We can use Divide and Conquer to solve this in O(nLogn) time.
The idea is to find the minimum value in the given array.
Once we have index of the minimum value, the max area is maximum of following three values.
a) Maximum area in left side of minimum value (Not including the min value)
b) Maximum area in right side of minimum value (Not including the min value)
c) Number of bars multiplied by minimum value.
The areas in left and right of minimum value bar can be calculated recursively.
If we use linear search to find the minimum value, then the worst case time complexity of this algorithm becomes O(n^2).
In worst case, we always have (n-1) elements in one side and 0 elements in other side and if the finding minimum takes O(n) time, we get the recurrence similar to worst case of Quick Sort.

How to find the minimum efficiently?
Range Minimum Query using Segment Tree can be used for this.

Complexity -> O(nlogn)
'''
