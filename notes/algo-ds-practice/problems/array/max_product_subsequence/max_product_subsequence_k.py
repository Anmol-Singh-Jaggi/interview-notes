"""
Given an integer array, find any k numbers whose product is maximum and output the maximum product.
The length of the given array will be >= k and all elements are in the range [-1000, 1000].

Example 1:
Input : A[] = {1, 2, 0, 3}, k = 2
Output : 6
Explanation : Subsequence containing elements {2, 3} gives maximum product : 2*3 = 6

Example 2:
Input : A[] = {1, 2, -1, -3, -6, 4}, k = 4
Output : 144
Explanation : Subsequence containing {2, -3, -6, 4} gives maximum product : 2*(-3)*(-6)*4 = 144

SOLUTION:

CASE I: If max element of A is 0 and k is odd
Here if we don’t include 0 in subsequence then product will be less than 0.
Since the product of an odd number of negative integers gives a negative integer, hence 0 must be included in the subsequence. Answer = 0.

CASE II: If max element of A is -ve and k is odd.
Here the product will be less than 0.
Since the product of an odd number of negative integers gives a negative integer, so to get the maximum product, we take the product of the smallest (absolute value wise) k elements.
Meaning we take the product of max1, max2 ... maxk
Answer = A[n-1] * A[n-2] * ….. * A[n-k]

CASE III: If max element of A is +ve and k is odd.
Here in a subsequence of k size if all elements are < 0 then product will be less than 0, since the product of an odd number of negative integers gives a negative integer.
Hence, at least one element must be a positive integer in the subsequence.
To get the max product, max +ve number should be present in the subsequence.
Now we need to add k-1 more elements to the subsequence.
Since k is odd, k-1 becomes even. So the problem boils down to case IV.
Answer = A[n-1] * Answer from CASE IV.

CASE IV: If k is even.
Since k is even, we always add a pair in subsequence.
So total pairs required to be added in subsequence is k/2.
Now since A is sorted, pair with the maximum product will always be either A[0]*A[1] OR A[n-1]*A[n-2].
Now, if `A[0]*A[1] > A[n-1]*A[n-2]`, second max product pair will be either A[2]*A[3] OR A[n-1]*[n-2].
Else, second max product pair will be either A[0]*A[1] OR A[n-3]*[n-4].
So the idea is to keep two pointers one on the rightmost part of the unused array and one on the leftmost part of the unused array.
Keep iterating till we get k/2 pairs!
Answer = product of k/2 pairs found.
"""
