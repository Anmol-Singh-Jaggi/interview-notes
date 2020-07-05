def sieve_of_erato(range_max):
    '''
    Complexity = O(nloglogn)
    Because sum of reciprocals of primes = O(loglogn)
    '''
    is_prime = [True for i in range(range_max + 1)]
    # Cross out all even numbers first.
    for i in range(4, range_max, 2):
        is_prime[i] = False
    i = 3
    while i * i <= range_max:
        if is_prime[i]:
            # Update all multiples of this prime number
            # CAREFUL: Take note of the range args.
            # Reason for i += 2*i instead of i += i:
            # Since p and p*p, both are odd, (p*p + p) will be even,
            # which means that it would have already been marked before
            for multiple in range(i * i, range_max + 1, i * 2):
                is_prime[multiple] = False
        i += 1

    # Print all prime numbers
    primes = []
    for i in range(2, range_max + 1):
        if is_prime[i]:
            primes.append(i)

    return primes


def main():
    primes = sieve_of_erato(100)
    print(primes)


if __name__ == "__main__":
    main()
