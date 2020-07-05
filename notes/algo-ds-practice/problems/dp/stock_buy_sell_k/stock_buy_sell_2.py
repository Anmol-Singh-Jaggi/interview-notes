'''
Same as the stock-buy-sell problem for k, but with k=2.
'''

'''
We can of-course solve it using the same algorithm.
But this is a different more clever algorithm.


Max profit with at most two transactions =
       MAX {max profit with one transaction and subarray price[0..i] +
            max profit with one transaction and aubarray price[i+1..n-1]  }
i varies from 0 to n-1.

Maximum possible using one transaction can be calculated using following O(n) algorithm.
Maximum difference between two elements such that larger element appears after the smaller number.
Time complexity of above simple solution is O(n2).

We can do this O(n) using following efficient Solution.
The idea is to store maximum possible profit of every subarray and solve the problem in following two phases.

1) Create a table profit[0..n-1] and initialize all values in it 0.
2) Traverse price[] from right to left and update profit[i] such that profit[i] stores maximum profit achievable from one transaction in subarray price[i..n-1].
3) Traverse price[] from left to right and update profit[i] such that profit[i] stores maximum profit such that profit[i] contains maximum achievable profit from two transactions in subarray price[0..i].
4) Return profit[n-1].

To do step 1, we need to keep track of maximum price from right to left side and to do step 2, we need to keep track of minimum price from left to right.
Why we traverse in reverse directions?
The idea is to save space, in second step, we use same array for both purposes, maximum with 1 transaction and maximum with 2 transactions.
After an iteration i, the array profit[0..i] contains maximum profit with 2 transactions and profit[i+1..n-1] contains profit with two transactions.
'''
