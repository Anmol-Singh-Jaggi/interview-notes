import itertools


def combinations_with_replacement(iterable, r):
    '''
    combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    Taken from Python docs.
    Do not understand how it works!!
    '''
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)


def combinations_with_replacement2(iterable, r):
    '''
    Implementing using `product()`
    '''
    pool = tuple(iterable)
    n = len(pool)
    for indices in itertools.product(range(n), repeat=r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)


def main():
    print(list(combinations_with_replacement('ABC', 2)))


if __name__ == "__main__":
    main()
