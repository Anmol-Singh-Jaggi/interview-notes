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


def prime_factorize(num, spf, cache):
    '''
    spf -> Smallest-prime-factor list; computed using sieve.
    '''
    # Complexity -> O(logn)
    if num in cache:
        return cache[num]
    if num == 1:
        cache[num] = Counter({1: 1})
        return cache[num]
    cache[num] = Counter({spf[num]: 1}) + prime_factorize(num // spf[num], spf, cache)
    return cache[num]


def main():
    n = 99
    spf = sieve(n + 1)
    ans = prime_factorize(n, spf, {})
    print(ans)


if __name__ == "__main__":
    main()
