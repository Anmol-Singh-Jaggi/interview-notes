from algo.number_theory.prime_factorization.prime_factorization import prime_factorize


def sum_of_factors(num):
    prime_factorization = prime_factorize(num)
    sum = 1
    for prime, power in prime_factorization.items():
        sum *= (prime**(power+1) - 1) // (prime-1)
    return sum


def main():
    print(sum_of_factors(1100))


if __name__ == "__main__":
    main()
