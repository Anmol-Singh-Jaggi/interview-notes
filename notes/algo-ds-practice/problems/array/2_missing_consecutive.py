'''
Given an array of size n-2 consisting of consecutive integers from 1 to n, find the 2 missing elements.
Example:

n = 5
arr = [1,3,5]
Missing = [2, 4]

SOLUTION:


SOLUTION 1:

Hash map / Boolean array.

SOLUTION 2:
We know sum of first n natural numbers = n*(n+1)/2
Also, sum of squares of first n natural numbers = n*(n+1)*(2n+1)/6
But the sum of the given array will be less than the actual value.

A + B = Sum(N) - sum(arr)
A^2 + B^2 = Sum2(N) - sum2(arr)

Now we have 2 equations in 2 variables.

For the second equation, we can do one more thing:

Find the average of the missing numbers = (Sum(N) - Sum(arr)) // 2
Sum up all the numbers in the array which are <= avg.
Smaller number, a = SUM(N, <=avg) - SUM(arr, <=avg)
Larger number, b = (A + B) - A

For example if arr = [1, 3, 5] and missing = [2, 4]
Sum of missing = 6
Avg = 3
sum of array numbers <= 3 => 1 + 3 = 4
Sum of first natural numbers till avg = 1 + 2 + 3 = 6
Therefore, smaller number = 6 - 4 = 2

SOLUTION 3:
Solution 2 is fine but it can lead to overflows.

We can XOR all the elements to get (A XOR B).
Meaning `arr[0] xor arr[1] xor .. arr[n] xor 1 xor 2 xor 3 .. xor n` = a xor b
where a and b are the missing numbers.
Now observe that in this xor, if a bit is set, that means that the bits of a and b differ at that position.
Lets say the rightmost set bit in a xor b is at position i
First we take the xor of all numbers in the array whose bit is set at i.
Then xor that with all the numbers from 1 to n whose bit is set at i.
We will get one missing number.

We can do similar approach with the numbers whose bit is not set at position i to get the second missing number.
'''
