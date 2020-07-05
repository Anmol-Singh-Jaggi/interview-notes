def knapsack(knapsack_weight, weights, values):
    num_items = len(values)
    dp_array = [[0] * (knapsack_weight + 1) for row in range(num_items)]
    for item_num in range(0, num_items):
        for weight in range(1, knapsack_weight + 1):
            if item_num >= 1:
                # Exclude this element
                dp_array[item_num][weight] = max(
                    dp_array[item_num][weight], dp_array[item_num - 1][weight])
                # Include this element
                item_weight = weights[item_num]
                item_value = values[item_num]
                if weight - item_weight >= 0:
                    dp_array[item_num][weight] = max(
                        dp_array[item_num][weight],
                        dp_array[item_num - 1][weight - item_weight] +
                        item_value)
    return dp_array[num_items - 1][knapsack_weight]


def main():
    knapsack_weight = 10
    weights = [0, 5, 4, 6, 3]
    values = [0, 10, 40, 30, 50]
    ans = knapsack(knapsack_weight, weights, values)
    print(ans)


if __name__ == "__main__":
    main()