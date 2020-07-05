'''
Given an array of n elements, where each element is at most k away from its target position, sort it.
For example, let us consider k is 2,
an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

SOLUTION 1:
We can use insertion sort.
For every element at index i:
Move elements of A[0..i-1], that are greater than arr[i], to one position ahead of their current position.
This loop will run at most k times.

Total complexity -> O(nk)

SOLUTION 2:
Create a min-heap of size k+1 with first k+1 elements.
One by one remove min element from heap, put it in result array,
and add a new element to heap from remaining elements.
CAREFUL: Notice the k+1 !!
Complexity -> O(nlogk)
'''
