from collections import Counter


def sieve(range_max):
    """
    Is is O(n) because every number is marked prime/composite exactly once.
    Very clever, yet easy to implement.
    """
    is_prime = [True] * range_max
    primes = []
    spf = [None] * range_max
    is_prime[0] = is_prime[1] = False
    for i in range(2, range_max):
        if is_prime[i]:
            primes.append(i)
            # A prime number is its own smallest prime factor
            spf[i] = i

        j = 0
        while j < len(primes) and i * primes[j] < range_max and primes[j] <= spf[i]:
            # This loop will only run once for even numbers.
            is_prime[i * primes[j]] = False
            spf[i * primes[j]] = primes[j]
            j += 1

    return spf


def prime_factorize(num, spf, cache_factors):
    # Complexity -> O(logn)
    if num in cache_factors:
        return cache_factors[num]
    if num == 1:
        cache_factors[num] = Counter({1: 1})
        return cache_factors[num]
    cache_factors[num] = Counter({spf[num]: 1}) + prime_factorize(
        num // spf[num], spf, cache_factors
    )
    return cache_factors[num]


def factorize_factorial(num, spf, cache_factorial, cache_factors):
    # Complexity -> O(nlogn)
    if num in cache_factorial:
        return cache_factorial[num]
    if num == 0:
        cache_factorial[num] = Counter({1: 1})
        return cache_factorial[num]
    cache_factorial[num] = prime_factorize(
        num, spf, cache_factors
    ) + factorize_factorial(num - 1, spf, cache_factorial, cache_factors)
    return cache_factorial[num]


def compute_ncr(n, r, mod, spf):
    cache_factorial = {}
    cache_factors = {}
    ans_factorization = (
        factorize_factorial(n, spf, cache_factorial, cache_factors)
        - factorize_factorial(r, spf, cache_factorial, cache_factors)
        - factorize_factorial(n - r, spf, cache_factorial, cache_factors)
    )
    ans = 1
    for key, value in ans_factorization.items():
        ans *= pow(key, value, mod)
    return ans % mod


def main():
    n = 10
    r = 5
    spf = sieve(n + 1)
    ans = compute_ncr(n, r, 1000000007, spf)
    print(ans)


if __name__ == "__main__":
    main()
