'''
Given an array of integers (both odd and even), sort them in such a way that the first part of the array contains odd numbers sorted in descending order, rest portion contains even numbers sorted in ascending order.

Examples:

Input  : arr[] = {1, 2, 3, 5, 4, 7, 10}
Output : arr[] = {7, 5, 3, 1, 2, 4, 10}

Input  : arr[] = {0, 4, 5, 3, 7, 2, 1}
Output : arr[] = {7, 5, 3, 1, 0, 2, 4}


SOLUTION 1 (Using Partition):
Partition the input array such that all odd elements are moved to left and all even elements on right.
This step takes O(n).
Once the array is partitioned, sort left and right parts individually.
This step takes O(n Log n).

SOLUTION 2:
Make all odd numbers negative.
Sort all numbers.
Revert the changes made in step 1 to get original elements back.

SOLUTION 3:
This problem can be easily solved by using the inbuilt sort function with a custom compare method.
On comparing any two elements there will be three cases:
When both the elements are even: In this case, the smaller element must appear in the left of the larger element in the sorted array.
When both the elements are odd: The larger element must appear on left of the smaller element.
One is odd and the other is even: The element which is odd must appear on the left of the even element.
'''
