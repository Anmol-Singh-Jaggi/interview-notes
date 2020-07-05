from collections import deque


def get_min_coins(denominations, amount):
    '''
    A state is defined by {amount}.
    And every amount has edges going towards
    {amt - denom[0], amt - denom[1], .... amt - denom[n]}
    So complexity = O(N*A)
    '''
    dq = deque()
    dq.append((0, amount))
    visited = {amount}
    while dq:
        dist, amt = dq.popleft()
        if amt == 0:
            return dist
        for denom in denominations:
            rem_amt = amt - denom
            if rem_amt >= 0 and rem_amt not in visited:
                visited.add(rem_amt)
                dq.append((dist + 1, rem_amt))
    return -1


def main():
    amount = 43
    denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
    amount = 11
    denominations = [1, 5, 6, 9]
    ans = get_min_coins(denominations, amount)
    print(ans)


main()
