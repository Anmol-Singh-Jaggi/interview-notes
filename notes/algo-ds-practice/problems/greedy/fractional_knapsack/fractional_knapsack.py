"""
In Fractional Knapsack, we can break items for maximizing the total value of knapsack.
This problem in which we can break an item is also called the fractional knapsack problem.

Input:
  Items as (value, weight) pairs
  arr[] = {{60, 10}, {100, 20}, {120, 30}}
  Knapsack Capacity, W = 50;
Output :
   Maximum possible value = 240
   By taking full items of 10 kg, 20 kg and
   2/3rd of last item of 30 kg

SOLUTION:
Greedy approach:
Sort the items on the basis of value/weight ratio.
Then starting from the highest ratio, keep adding full items.
At the end, we might end up with remaining capacity < weight of item.
In that case, we'll just add as much of the item as we can.
That means we will add 'k' full items. (k+1)th item might be partial.
"""


def fractional_knapsack(items, capacity):
    items.sort(reverse=True, key=lambda item: item[1] / item[0])
    ans = 0
    for item in items:
        wt = item[0]
        val = item[1]
        if capacity >= wt:
            capacity -= wt
            ans += val
        else:
            fraction = capacity / wt
            ans += val * fraction
            break
    return ans


def main():
    weights = [10, 40, 20, 30]
    values = [60, 40, 100, 120]
    items = list(zip(weights, values))
    capacity = 50

    ans = fractional_knapsack(items, capacity)
    print(ans)


main()
