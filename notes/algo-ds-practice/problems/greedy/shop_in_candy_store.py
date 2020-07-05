"""
Shop in Candy Store:

In a candy store there are N different types of candies available  and the prices of all the N different types of candies are provided to you.
You are now provided with an attractive offer.
You can buy a single candy from the store and get atmost K other candies ( all are different types ) for free.
Now you have to answer two questions.
Firstly, you have to tell what is the minimum amount of money you have to spend to buy all the N different candies.
Secondly, you have to tell what is the maximum amount of money you have to spend to buy all the N different candies.
In both the cases you must utilize the offer i.e. you buy one candy and get K other candies for free.

Example:
Input
 1
 4  2
 3 2 1 4
Output
 3 7

Explanation
As according to the offer if you but one candy you can take atmost two more for free.
So in the first case you buy the candy which costs 1 and take candies worth 3 and 4 for free, also you buy candy worth 2 as well.
So min cost = 1+2 =3.
In the second case I buy the candy which costs 4 and take candies worth 1 and 2 for free, also I  buy candy worth 3 as well.
So max cost = 3+4 =7.
"""


def min_max_candy(prices, k):
    idx1 = 0
    idx2 = len(prices) - 1
    ans = 0
    free = 0
    while idx1 <= idx2:
        ans += prices[idx1]
        for i in range(k):
            if idx2 <= idx1:
                break
            free += prices[idx2]
            idx2 -= 1
        idx1 += 1
    assert free + ans == sum(prices)
    return ans


def main():
    prices = [1, 2, 3, 4]
    k = 0
    prices.sort()
    ans = min_max_candy(prices, k)
    print(ans)
    prices.reverse()
    ans = min_max_candy(prices, k)
    print(ans)


main()
