def sieve(range_max):
    """
    Is is O(n) because every number is marked prime/composite exactly once.
    Lets say there is a number num = p1^e1 * p2^e2 * p3^e3.
    It will be marked only once when i = p1^(e1-1) * p2^e2 * p3^e3 and primes[j] = p1.
    Very clever, yet easy to implement.
    https://cp-algorithms.com/algebra/prime-sieve-linear.html
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

    return primes


def main():
    print(sieve(100))


if __name__ == "__main__":
    main()
