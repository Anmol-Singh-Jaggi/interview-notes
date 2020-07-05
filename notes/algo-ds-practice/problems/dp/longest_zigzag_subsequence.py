'''
The longest Zig-Zag subsequence problem is to find length of the longest subsequence of given sequence such that all elements of this are alternating.
If a sequence {x1, x2, .. xn} is alternating sequence then its element satisfy one of the following relation :

  x1 < x2 > x3 < x4 > x5 < …. xn or
  x1 > x2 < x3 > x4 < x5 > …. xn

Examples :

Input: arr[] = {1, 5, 4}
Output: 3
The whole arrays is of the form  x1 < x2 > x3

Input: arr[] = {1, 4, 5}
Output: 2
All subsequences of length 2 are either of the form
x1 < x2; or x1 > x2

Input: arr[] = {10, 22, 9, 33, 49, 50, 31, 60}
Output: 6
The subsequences {10, 22, 9, 33, 31, 60} or
{10, 22, 9, 49, 31, 60} or {10, 22, 9, 50, 31, 60}
are longest Zig-Zag of length 6.


SOLUTION 1:
Similar to how we solvest Longest Increasing Subsequence.
But in this case, we will maintain 2 arrays dp1[] and dp2[].
For every i, dp1[i] will tell the answer ending at i such that the previous element included was smaller than n[i].
For every i, dp2[i] will tell the answer ending at i such that the previous element included was greater than n[i].
How to calculate these 2:
for(j = 0; j < i; j++){
    if n[j] < n[i]{
        dp1[i] = max(dp1[i], dp2[j] + 1)
    }
    else{
        dp2[i] = max(dp2[i], dp1[j] + 1)
    }
}

Pretty dope huh!
Complexity -> O(n*n).

SOLUTION 2:
If you think about it, we dont even need DP here.
Lets say the first element chosen is n[0].
Now, we iterate from i = 1 until n[i] > n[0].
We then include this highest element in our subsequence after n[0].
Then we iterate forward and find the lowest.
Basically, find the local maxima and minima alternatingly.

We will also need to do this once more by starting with minima and then maxima.
Complexity -> O(n)

One simple way to implement this as follows:

Initialize integer lastSign to 0.
FOR i in range 1 to N - 1
    integer sign = signum(seq[i] - seq[i-1])
    IF sign != lastSign AND IF sign != 0
        increment length by 1. lastSign = sign.
    END IF
END FOR
return length.

Where signum(sign) =
{
    1 if sign > 0
    0 if sign == 0
    -1 if sign < 0
}

Another way to implement is to precompute the next greater index and the next smaller index for every index i using stacks.
'''
