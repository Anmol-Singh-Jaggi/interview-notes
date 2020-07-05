"""
You are given an array A of size N.
The array contains integers and is of even length.
The elements of the array represent N coin of values V1, V2, ....Vn.
You play against an opponent in an alternating way.
In each turn, a player selects either the first or last coin from the row,
removes it from the row permanently, and receives the value of the coin.
You need to determine the maximum possible amount of money you can win if you go first.

Examples:
Input:
2
4
5 3 7 10
4
8 15 3 7
Output:
15
22

Explanation:
Testcase1: The user collects maximum value as 15(10 + 5)
Testcase2: The user collects maximum value as 22(7 + 15)
"""


def game(arr, cache, start, end):
    if end in cache[start]:
        return cache[start][end]
    if start == end - 1:
        bigger = start
        smaller = end
        if arr[start] < arr[end]:
            bigger, smaller = smaller, bigger
        cache[start][end] = (arr[bigger], arr[smaller], [bigger], [smaller])
        return cache[start][end]
    ans1 = game(arr, cache, start + 1, end)
    ans2 = game(arr, cache, start, end - 1)
    # ans[0] = Value of coins with other player.
    # ans[1] = Value of coins with this player.
    # ans[2] = Indices of coins with other player.
    # ans[3] = Indices of coins with this player.
    # ans[2] and ans[3] are just for printing!
    # CAREFUL: Note the `+ arr[start]` and `+ arr[end]`
    if ans1[1] + arr[start] > ans2[1] + arr[end]:
        cache[start][end] = (ans1[1] + arr[start], ans1[0], ans1[3] + [start], ans1[2])
    else:
        cache[start][end] = (ans2[1] + arr[end], ans2[0], ans2[3] + [end], ans2[2])
    return cache[start][end]


def main():
    arr = [8, 15, 3, 7]
    cache = {}
    for i in range(len(arr)):
        cache[i] = {}
    ans = game(arr, cache, 0, len(arr) - 1)
    print(ans)


main()

