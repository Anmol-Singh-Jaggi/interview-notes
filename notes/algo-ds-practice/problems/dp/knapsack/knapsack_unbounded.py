from functools import lru_cache

items = []


@lru_cache(maxsize=None)
def knapsack_unbounded(capacity):
    ans = 0
    for item in items:
        if item[0] <= capacity:
            ans = max(ans, item[1] + knapsack_unbounded(capacity - item[0]))
    return ans


def main():
    capacity = 8
    weights = [1, 3, 4, 5]
    values = [10, 40, 50, 70]
    global items
    items = list(zip(weights, values))
    ans = knapsack_unbounded(capacity)
    print(ans)


if __name__ == "__main__":
    main()
