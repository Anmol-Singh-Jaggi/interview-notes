from collections import Counter


def prime_factorize(num):
    powers = Counter()
    # First take care of powers of 2.
    i = 2
    while num % i == 0:
        num //= i
        powers[i] = powers.get(i, 0) + 1

    # Since 2 is taken care of, we can check for 3, 5, 7...
    i = 3
    while i * i <= num:
        while num % i == 0:
            num //= i
            powers[i] = powers.get(i, 0) + 1
        i += 2
    if num > 2:
        powers[num] = powers.get(num, 0) + 1
    return powers


def main():
    c1 = prime_factorize(2)
    c2 = prime_factorize(5)
    c1 += c2
    print(c1)


if __name__ == "__main__":
    main()
