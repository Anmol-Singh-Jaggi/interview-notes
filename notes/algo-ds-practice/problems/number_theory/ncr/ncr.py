from functools import lru_cache


def ncr(n, r, mod):
    dp = [0] * (r + 1)
    dp[0] = 1  # Since nC0 is 1
    for i in range(1, n + 1):
        # We are actually computing Pascal's triangle this way
        # CAREFUL: Note that we are iterating in reverse.
        for j in range(min(i, r), 0, -1):
            dp[j] += dp[j - 1] % mod
        print(dp)

    return dp[r] % mod


@lru_cache(maxsize=None)
def compute_ncr(n, r):
    if n == r:
        return 1
    if n == 0:
        return 0
    if r == 0:
        return 1
    return compute_ncr(n - 1, r - 1) + compute_ncr(n - 1, r)


def main():
    print(ncr(10, 5, 10000000))


if __name__ == "__main__":
    main()
