import itertools


def combinations(iterable, r):
    '''
    combinations('ABCD', 2) --> AB AC AD BC BD CD
    combinations(range(4), 3) --> 012 013 023 123
    Taken from Python docs
    Do not understand how it works!!
    '''
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


def combinations2(iterable, r):
    '''
    Implementing using `permutations()`.
    '''
    pool = tuple(iterable)
    n = len(pool)
    for indices in itertools.permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)


def main():
    print(list(combinations('ABC', 2)))


if __name__ == "__main__":
    main()
