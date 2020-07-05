def extended_gcd(a, b):
    '''
    No need to remember it.
    Just derive it on the spot.
    https://cp-algorithms.com/algebra/extended-euclid-algorithm.html
    Also, we can have infinitely many solutions:
    (x1, y1) = (x0 − kb, y0 + ka) for any integer k. (Try to derive this.)
    '''
    if b == 0:
        return 1, 0, a
    if a == 0:
        return 0, 1, b
    x1, y1, gcd = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (x, y, gcd)


def main():
    print(extended_gcd(35, 15))


if __name__ == "__main__":
    main()
