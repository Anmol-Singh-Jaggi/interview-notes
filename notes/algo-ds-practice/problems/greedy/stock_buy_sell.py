'''
The cost of a stock on each day is given in an array.
Find the max profit that you can make by buying and selling in those days.
Only 1 stock can be held at a time.

For example:
Array = {100, 180, 260, 310, 40, 535, 695}
The maximum profit can earned by buying on day 0, selling on day 3.
Again buy on day 4 and sell on day 6.
If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.
'''


'''
If we are allowed to buy and sell only once, then we can use following algorithm. Maximum difference between two elements. Here we are allowed to buy and sell multiple times.
Following is algorithm for this problem.
    1. Find the local minima and store it as starting index. If not exists, return.
    2. Find the local maxima. and store it as ending index. If we reach the end, set the end as ending index.
    3. Update the solution (Increment count of buy sell pairs)
    4. Repeat the above steps if end is not reached.

Alternate solution:
class Solution {
    public int maxProfit(int[] prices) {
        int maxprofit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1])
                maxprofit += prices[i] - prices[i - 1];
        }
        return maxprofit;
    }
}
Explanation - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/
'''
