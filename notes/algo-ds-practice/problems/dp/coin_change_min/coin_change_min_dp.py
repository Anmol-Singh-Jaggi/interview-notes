import math


def get_min_coins(denominations, amount):
    dp = [math.inf for amt in range(amount + 1)]
    dict_dp = [{} for amt in range(amount + 1)]
    dp[0] = 0

    for amt in range(1, amount + 1):
        for i in range(0, len(denominations)):
            denom = denominations[i]
            remaining_amt = amt - denom
            if remaining_amt >= 0:
                sub_ans = dp[remaining_amt]
                if sub_ans != math.inf:
                    sub_ans += 1
                    if sub_ans < dp[amt]:
                        dp[amt] = sub_ans
                        dict_dp[amt] = dict(dict_dp[remaining_amt])
                        dict_dp[amt][denom] = dict_dp[amt].get(denom, 0) + 1

    return dict_dp[amount]


def main():
    amount = 43
    denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
    ans = get_min_coins(denominations, amount)
    print(ans)


main()
