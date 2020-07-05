'''
Given a list of denominations of coins and a target value, find the number of ways to make that value using the coins, where a single denomination can be used infinite times possibly.

Eg.

denominations = {2,3,5,6}
target = 10

Answer = 5:

2x2 + 6x1
5x2
2x1 + 3x1 + 5x1
2x2 + 3x2
2x5
'''

def coin_change(denominations, target_value):
    if target_value < 0 or not denominations:
        return 0
    if target_value == 0:
        return 1
    ans = 0
    # Include the last denominations at least 1 time
    ans += coin_change(denominations, target_value - denominations[-1])
    # Exclude the last denomination
    ans += coin_change(denominations[0:-1], target_value)
    return ans


def main():
    dens = [2, 3, 5, 6]
    target_value = 100
    ans = coin_change(dens, target_value)
    print(ans)


if __name__ == "__main__":
    main()
