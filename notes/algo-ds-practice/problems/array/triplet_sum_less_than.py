'''
Given an array of distinct integers and a sum value.
Find count of triplets with sum smaller than given sum value.
Expected Time Complexity is O(n2).

Examples:

Input : arr[] = {-2, 0, 1, 3}
        sum = 2.
Output : 2
Explanation :  Below are triplets with sum less than 2
               (-2, 0, 1) and (-2, 0, 3)

Input : arr[] = {5, 1, 3, 4, 7}
        sum = 12.
Output : 4
Explanation :  Below are triplets with sum less than 12
               (1, 3, 4), (1, 3, 5), (1, 3, 7) and
               (1, 4, 5)
'''

'''
SOLUTION:

We have to find a,b,c such that a+b+c < sum and a<b<c.
First sort the array.
Then fix 'c' to arr[n-1].
Now search for a,b such that a+b < (sum - arr[n-1]) and a<b.
This can be done in O(n) using meet-in-the-middle 2-pointer algo.
We will do this by fixing c = arr[n-1], arr[n-2]... arr[2] one-by-one.
So total Complexity = O(n*n).
'''
