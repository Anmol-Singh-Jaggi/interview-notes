'''
The cost of a stock on each day is given in an array. Find the max profit that you can make by buying and selling in those days, a maximum `k` times only. Only 1 stock can be held at a time.

For example:

**Input**:<br>
Price = [10, 22, 5, 75, 65, 80]<br>
K = 2

**Output**: 87<br>
Trader earns 87 as sum of 12 and 75 Buy at price 10, sell at 22, buy at 5 and sell at 80

**Input**:<br>
Price = [12, 14, 17, 10, 14, 13, 12, 15]<br>
K = 3

**Output**: 12<br>
Trader earns 12 as the sum of 5, 4 and 3 Buy at price 12, sell at 17, buy at 10 and sell at 14 and buy at 12 and sell at 15

**Input**:<br>
Price = [100, 30, 15, 10, 8, 25, 80]<br>
K = 3

**Output**: 72<br>
Only one transaction. Buy at price 8 and sell at 80.

**Input**:<br>
Price = [90, 80, 70, 60, 50]<br>
K = 1

**Output**: 0<br>
Not possible to earn.

# Solution

Let `profit[t][i]` represent maximum profit using at most `t` transactions up to day `i` (including day i).<br>
Then the relation is:

```
profit[t][i] = max(
        profit[t][i-1],
        max(price[i] – price[j] + profit[t-1][j]) for all j in range [0, i-1]
        )
```

`profit[t][i]` will be maximum of:

- `profit[t][i-1]` which represents not doing any transaction on the ith day.
- Maximum profit gained by selling on ith day.<br>
  In order to sell shares on ith day, we need to purchase it on any one of [0, i – 1] days.<br>
  If we buy shares on jth day and sell it on ith day, max profit will be price[i] – price[j] + profit[t-1][j] where j varies from 0 to i-1.<br>
  Here profit[t-1][j] is best we could have done with one less transaction till jth day.

The above time complexity is `O(k*n*n)`.

We can further reduce it by computing the second case in `O(1)`. The formula `price[i] – price[j] + profit[t-1][j]` can be rewritten as:

`price[i] + (profit[t-1][j] - price[j])`

which means the second case is:

`price[i] + max(profit[t-1][j] - price[j]) for all j in range [0, i-1]`

So we can keep a running maximum now.

Time and space complexity - `O(n*k)`.

'''
def stock_maximize_k(stocks, k):
    ans = [[0 for j in range(len(stocks))] for i in range(k + 1)]
    # CAREFUL: range has to start from 1 not 0!!
    # Python interprets -1 as len-1 rather than giving an exception!!!
    for t in range(1, k + 1):
        for i in range(1, len(stocks)):
            no_sell = ans[t][i - 1]
            yes_sell = 0
            for j in range(0, i):
                if stocks[i] > stocks[j]:
                    yes_sell = max(yes_sell, stocks[i] - stocks[j] + ans[t - 1][j])
            ans[t][i] = max(no_sell, yes_sell)
    return ans[k][len(stocks) - 1]


def stock_maximize_k_optimal(stocks, k):
    ans = [[0 for j in range(len(stocks))] for i in range(k + 1)]
    for t in range(1, k + 1):
        prev_max_diff = ans[t - 1][0] - stocks[0]
        for i in range(1, len(stocks)):
            no_sell = ans[t][i - 1]
            yes_sell = stocks[i] + prev_max_diff
            ans[t][i] = max(no_sell, yes_sell)
            prev_max_diff = max(prev_max_diff, ans[t - 1][i] - stocks[i])

    return ans[k][len(stocks) - 1]


def main():
    stocks = [10, 22, 5, 75, 65, 80]
    k = 2
    ans = stock_maximize_k_optimal(stocks, k)
    print(ans)


if __name__ == "__main__":
    main()
