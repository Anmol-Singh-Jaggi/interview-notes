"""
In Fractional Knapsack, we can break items for maximizing the total value of knapsack.
This problem in which we can break an item is also called the fractional knapsack problem.
In the unbounded variation, we can use one item as many items as we want.

Input: val[] = {14, 27, 44, 19}, wt[] = {6, 7, 9, 8}, W = 50
Output: 244.444

Input: val[] = {100, 60, 120}, wt[] = {20, 10, 30}, W = 50
Output: 300

SOLUTION:
Greedy approach:
Just keep selecting the item with the highest value/weight ratio as much as you can.
"""


def fractional_knapsack_unbounded(items, capacity):
    max_ratio_item = items[0]
    for item in items:
        if item[1] / item[0] > max_ratio_item[1] / max_ratio_item[0]:
            max_ratio_item = item
    print(max_ratio_item)
    return (capacity * max_ratio_item[1]) / max_ratio_item[0]


def main():
    weights = [10, 40, 20, 30]
    values = [60, 40, 100, 120]
    items = list(zip(weights, values))
    capacity = 50

    ans = fractional_knapsack_unbounded(items, capacity)
    print(ans)


main()
