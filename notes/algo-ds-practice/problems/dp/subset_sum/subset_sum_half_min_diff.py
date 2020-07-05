'''
Given an array, the task is to divide it into two sets S1 and S2 such that
the absolute difference between their sums is minimum.

SOLUTION:

Just apply subset sum.
Answer is min(abs(dp[len-1][sum] - arr_sum)) for all dp[][] == True and sum = 0 to arr_sum/2.
'''
