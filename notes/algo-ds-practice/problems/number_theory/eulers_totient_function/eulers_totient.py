from algo.number_theory.prime_factorization.prime_factorization import prime_factorize


def etf(num):
    powers = prime_factorize(num)
    ans = num
    for prime in powers.keys():
        ans -= ans // prime
    return ans


def main():
    print(etf(90))


if __name__ == "__main__":
    main()
