from problems.backtracking.combinatorial.generate_all_permutations import (
    generate_all_permutations,
    generate_all_permutations_iterator,
)
from problems.backtracking.combinatorial.generate_ncr import (
    generate_ncr_sets,
    generate_ncr_sets_iterator,
)


def generate_npr_sets(n, r):
    """
    Just compute nCr sets first.
    Then permute each one of them separately.
    """
    combinations = generate_ncr_sets(n, r)
    result = []
    for comb in combinations:
        solutions = []
        generate_all_permutations(comb, 0, len(comb), solutions)
        result.extend(solutions)
    return result


def generate_npr_sets_iterator(n, r):
    combinations = generate_ncr_sets_iterator(n, r)
    for comb in combinations:
        yield from generate_all_permutations_iterator(comb, 0, len(comb))


def main():
    n = 4
    r = 2
    ans = generate_npr_sets(n, r)
    print(sorted(ans))
    print(len(ans))
    print(sorted(list(generate_npr_sets_iterator(n, r))))


if __name__ == "__main__":
    main()
