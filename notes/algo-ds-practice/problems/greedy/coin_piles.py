"""
There are N piles of coins each containing  A[i] coins.
Now, you have to adjust the number of coins in each pile such that for any two pile,
if 'a' be the number of coins in first pile and 'b' is the number of coins in second pile, then |a-b|<=K.
In order to do that you can remove coins from different piles to decrease the number of coins in those
piles but you cannot increase the number of coins in a pile by adding more coins.
Now, given a value of N and K, along with the sizes of the N different piles you have to
tell the minimum number of coins to be removed in order to satisfy the given condition.

Note: You can also remove a pile by removing all the coins of that pile.

Example
Input
3
4 0
2 2 2 2
6 3
1 2 5 1 1 1
6 3
1 5 1 2 5 1

Output
0
1
2

Explanation
1. In the first test case, for any two piles the difference in the number of coins is <=0. So no need to remove any coins.
2. In the second test case if we remove one coin from pile containing 5 coins then for any
two piles the absolute difference in the number of coins is <=3.
3. In the third test case if we remove one coin each from both the piles containing 5 coins,
then for any two piles the absolute difference in the number of coins is <=3.

SOLUTION:
1. Sort the entire array.
2. Let start = 0. max capacity of any pile, therefore = arr[start] + k.
3. Starting from the end of the array in reverse, if arr[i] > max_cap, remove arr[i] - max_cap coins from pile i.
4. Since we also have the option of removing an entire pile, we can do so one-by-one from starting.
5. Repeat 2-3 with start=[0, len-1]

Note that no point in removing entire piles from the end; since its better to remove just as many coins as needed.
Imagine a case like this - [1, 2, 50, 51, 52, 53]
In this, its better to simply remove the entire first 2 piles.
"""


def min_coin_remove(piles, start, k):
    ans = 0
    max_limit = piles[start] + k
    for i in range(len(piles) - 1, start - 1, -1):
        if piles[i] > max_limit:
            diff = piles[i] - max_limit
            ans += diff
    return ans


def min_coin_remove_all(piles, k):
    if len(piles) == 1:
        return 0
    ans = 100000000
    piles.sort()
    cum_sum = []
    sum = 0
    for i in range(0, len(piles)):
        sum += piles[i]
        cum_sum.append(sum)
    for start in range(0, len(piles) - 1):
        ans2 = min_coin_remove(piles, start, k)
        if start >= 1:
            ans2 += cum_sum[start - 1]
        ans = min(ans, ans2)
    return ans


def main():
    piles = [1]
    k = 3
    ans = min_coin_remove_all(piles, k)
    print(ans)


main()
