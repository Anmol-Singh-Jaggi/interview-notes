from algo.number_theory.ncr.ncr import ncr


def ncr_lucas(n, r, pmod):
    """
    Complexity -> O(logn base pmod).
    """
    if r == 0:
        return 1
    next_n, n = divmod(n, pmod)
    next_r, r = divmod(r, pmod)
    return ncr(n, r, pmod) * ncr_lucas(next_n, next_r, pmod) % pmod


def main():
    print(ncr_lucas(10, 5, 1000000007))


if __name__ == "__main__":
    main()
