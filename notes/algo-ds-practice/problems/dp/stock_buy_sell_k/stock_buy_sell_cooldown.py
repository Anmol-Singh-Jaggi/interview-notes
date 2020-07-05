'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

SOLUTION:

Basically, maintain the local minima and the corresponding local maxima.
Let i be the index of a local minima, and j be the index of the local maxima, such that j > i.

Then ans[j] = max(prices[j] - prices[i] + ans[i-2], prices[j] - prices[i+1] + ans[i-1])

Basically, we can either choose price[i] itself, or we can choose price[i+1].
'''
