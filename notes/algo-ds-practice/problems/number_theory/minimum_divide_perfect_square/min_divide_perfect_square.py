"""
Find minimum number to be divided to make a number a perfect square.

Solution:
A number is perfect square if all prime factors appear even number of times.
The idea is to find the prime factor of n and find each prime factor power.
Now, find and multiply all the prime factor whose power is odd.
The resultant of the multiplication is the answer.
"""
from algo.number_theory.prime_factorization.prime_factorization import prime_factorize


def min_divide_perfect_square(num):
    ans = 1
    factorization = prime_factorize(num)
    for prime, power in factorization.items():
        if power & 1:
            ans *= prime
    return ans


def main():
    num = 18945
    min_divide = min_divide_perfect_square(num)
    print(min_divide)
    print(num / min_divide)


if __name__ == "__main__":
    main()
