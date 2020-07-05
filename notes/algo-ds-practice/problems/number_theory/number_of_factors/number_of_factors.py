from algo.number_theory.prime_factorization.prime_factorization import prime_factorize


def number_of_factors(num):
    prime_factorization = prime_factorize(num)
    ans = 1
    for power in prime_factorization.values():
        ans *= (power+1)
    return ans


def main():
    print(number_of_factors(10))


if __name__ == "__main__":
    main()
