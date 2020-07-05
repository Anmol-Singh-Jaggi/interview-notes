'''
Find the longest even-length substring such that sum of first and second half is same.
Examples :

Input: str = "123123"
Output: 6
The complete string is of even length and sum of first and second
half digits is same

Input: str = "1538023"
Output: 4
The longest substring with same first and second half sum is "5380"

SOLUTION:

Just consider every index as the middle and expand outwards to check.
Complexity -> O(N*N)

ALTERNATE:

DP formula:

Let us say we have the sum of every substring sum(i,j). It can precomputed in O(n).

Now, ans(i, j) =
max(ans(i+1, j), ans(i, j+1)), if arr(i, j) is odd-length
max(ans(i+2, j), ans(i, j+2)), if arr(i, j) is even-length and sum of left half of array != right half
j-i if arr(i,j) is even length and sum of left half = sum of right half.

Complexity -> O(n*n)


'''
