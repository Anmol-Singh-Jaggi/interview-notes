def generate_ncr_sets(n, r):
    """
    This is exactly same as the dp formula to compute nCr.
    C(n,r) = (n-1, r-1)[Choose the nth element] + C(n-1, r)[Dont choose]
    """
    if r <= 0 or n <= 0 or r > n:
        return [[]]
    if r == n:
        # CAREFUL: Dont forget this base case!
        return [[i for i in range(1, n + 1)]]
    choose_current = generate_ncr_sets(n - 1, r - 1)
    for lst in choose_current:
        lst.append(n)
    dont_choose_current = generate_ncr_sets(n - 1, r)
    return choose_current + dont_choose_current


def generate_ncr_sets_iterator(n, r):
    if r <= 0 or n <= 0 or r > n:
        yield []
        return
    if r == n:
        yield [i for i in range(1, n + 1)]
        return
    choose_current = generate_ncr_sets(n - 1, r - 1)
    for lst in choose_current:
        lst.append(n)
    dont_choose_current = generate_ncr_sets(n - 1, r)
    yield from choose_current + dont_choose_current


def main():
    n = 5
    r = 2
    ans = list(generate_ncr_sets(n, r))
    print(sorted(ans))
    print(len(ans))


if __name__ == "__main__":
    main()
