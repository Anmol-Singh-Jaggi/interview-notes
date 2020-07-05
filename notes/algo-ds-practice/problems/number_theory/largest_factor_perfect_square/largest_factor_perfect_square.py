"""
Given a number N. The task is to find the largest factor of that number which is a perfect square.

Solution:

If any prime number occurs even number of times in the prime factorization of the given number, then include prime ** power.
Else, include prime ** (power-1)
"""
from algo.number_theory.prime_factorization.prime_factorization import prime_factorize


def largest_factor_perfect_square(num):
    ans = 1
    factorization = prime_factorize(num)
    for prime, power in factorization.items():
        if power & 1:
            ans *= prime ** (power - 1)
        else:
            ans *= prime ** power
    return ans


def main():
    ans = largest_factor_perfect_square(75)
    print(ans)


if __name__ == "__main__":
    main()
