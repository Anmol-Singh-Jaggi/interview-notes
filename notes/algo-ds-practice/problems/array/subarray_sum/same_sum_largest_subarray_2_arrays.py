'''
Given two binary arrays arr1[] and arr2[] of same size n.
Find length of the longest common span (i, j) where j >= i such that
arr1[i] + arr1[i+1] + …. + arr1[j]
=
arr2[i] + arr2[i+1] + …. + arr2[j].


Examples :

Input: arr1[] = {0, 1, 0, 0, 0, 0};
       arr2[] = {1, 0, 1, 0, 0, 1};
Output: 4
The longest span with same sum is from index 1 to 4.

Input: arr1[] = {0, 1, 0, 1, 1, 1, 1};
       arr2[] = {1, 1, 1, 1, 1, 0, 1};
Output: 6
The longest span with same sum is from index 1 to 6.

Input: arr1[] = {0, 0, 0};
       arr2[] = {1, 1, 1};
Output: 0

Input: arr1[] = {0, 0, 1, 0};
       arr2[] = {1, 1, 1, 1};
Output: 1

SOLUTION:

Lets say we compute cumulativeSum1 and cumulativeSum2 for the 2 arrays.
Now, we want 2 indices i and j ( j >= i) such that:
cumSum1[j] - cumSum1[i] = cumSum2[j] - cumSum2[i]
This can be rewritten as:
cumSum2[i] - cumSum1[i] = cumSum2[j] - cumSum1[j]

That is we make a new array such that newArr[i] = arr1[i] - arr2[i].
Now in this array, we need to just find the largest subarray with zero sum.
Which can be done through hashing in O(n).

'''
