import math
from functools import lru_cache

denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]


@lru_cache(maxsize=None)
def get_min_coins(amount):
    if amount == 0:
        return 0, {}
    ans = math.inf
    answer_mapping = {}
    for i in range(len(denominations)):
        denom = denominations[i]
        if amount >= denom:
            sub_ans, sub_ans_mapping = get_min_coins(amount - denom)
            if sub_ans == math.inf:
                continue
            sub_ans += 1
            if sub_ans < ans:
                ans = sub_ans
                answer_mapping = dict(sub_ans_mapping)
                answer_mapping[denom] = answer_mapping.get(denom, 0) + 1
    return ans, answer_mapping


def main():
    amount = 43
    ans = get_min_coins(amount)
    print(ans)


main()
