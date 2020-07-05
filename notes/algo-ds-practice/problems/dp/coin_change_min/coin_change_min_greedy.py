"""
Note that this algo is wrong!!
See this https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/

amount = 11
denominations = [1, 5, 6, 9]
Greedy answer = {9: 1, 1:2}
Actual answer = {5:1, 6:1}
"""


def get_min_coins(denominations, amount):
    answer = {}
    for i in range(len(denominations) - 1, -1, -1):
        denom = denominations[i]
        num_notes = amount // denom
        if num_notes:
            answer[denom] = num_notes
            amount -= denom * num_notes
    return answer


def main():
    amount = 43
    denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
    amount = 11
    denominations = [1, 5, 6, 9]
    ans = get_min_coins(denominations, amount)
    print(ans)


main()
