'''
Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.

Example:

    Input: arr[] = {3, 1, 4, 6, 5}
    Output: True
    There is a Pythagorean triplet (3, 4, 5).

    Input: arr[] = {10, 4, 6, 12, 5}
    Output: False
    There is no Pythagorean triplet.

SOLUTIONS:

SOLUTION 1:
Brute force = O(n^3)

SOLUTION 2:
We can solve this in O(n2) time by sorting the array first.
1) Do square of every element in input array. This step takes O(n) time.
2) Sort the squared array in increasing order. This step takes O(nLogn) time.
3) To find a triplet (a, b, c) such that a2 = b2 + c2, do following.
 - Fix ‘a’ as last element of sorted array.
 - Now search for pair (b, c) in subarray between first element and ‘a’.
   A pair (b, c) with given sum can be found in O(n) time using meet-in-middle algorithm.
 - If no pair found for current ‘a’, then move ‘a’ one position back and repeat step 3.2.

Meet-in-middle algorithm is an algorithm to check if there exists a pair in a sorted array which sums up to a target value.
Basically, keep pointer 1 at index 0 and pointer 2 at index n-1. Then at each step, reduce the window size by 1, depending upon whether the current pair sum is larger or smaller than the target.

SOLUTION 3:
We can use hashing.
Just square all the numbers and put it in hash table.
Now select all pairs a and b and check if a+b exists in the hash table or not.
Complexity -> O(n*n)
'''
