def coin_change(denominations, target_value):
    dp_array = [[0] * len(denominations) for row in range(target_value + 1)]
    dp_array[0] = [1] * len(denominations)
    for val in range(1, target_value + 1):
        for denom_it in range(0, len(denominations)):
            part1 = 0
            part2 = 0
            # Include this denominations at least 1 time
            if val >= denominations[denom_it]:
                part1 = dp_array[val - denominations[denom_it]][denom_it]
            # Exclude this denomination
            if denom_it >= 1:
                part2 = dp_array[val][denom_it - 1]
            dp_array[val][denom_it] = part1 + part2
    return dp_array[target_value][len(denominations) - 1]


def coin_change2(denominations, target_value):
    # CAREFUL: Fantastic insight!!
    dp_array = [0] * (target_value+1)
    dp_array[0] = 1
    for den in denominations:
        for i in range(den, len(dp_array)):
            dp_array[i] += dp_array[i - den]
    return dp_array[target_value]


def main():
    dens = [2, 3, 5, 6]
    target_value = 100
    ans = coin_change2(dens, target_value)
    print(ans)


if __name__ == "__main__":
    main()
