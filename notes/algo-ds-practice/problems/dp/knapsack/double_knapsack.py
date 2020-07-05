'''
We have n items each with value and weight of its own.
We have 2 knapsacks of capacities cap1 and cap2.
Fill the knapsacks such that the total value is maximized.

SOLUTION:

for i = 1 to n do
  for w1 = maxW1 down to a[i].weight do
    for w2 = maxW2 down to a[i].weight do
      dp[w1, w2] = max
                   {
                       dp[w1, w2], <- we already have the best choice for this pair
                       dp[w1 - a[i].weight, w2] + a[i].gain <- put in knapsack 1
                       dp[w1, w2 - a[i].weight] + a[i].gain <- put in knapsack 2
                   }
'''
