def generate_all_permutations(lst, start, end, solutions):
    if start >= end:
        solutions.append(list(lst))
    for i in range(start, end):
        lst[start], lst[i] = lst[i], lst[start]
        generate_all_permutations(lst, start + 1, end, solutions)
        lst[start], lst[i] = lst[i], lst[start]


def generate_all_permutations_iterator(lst, start, end):
    if start >= end:
        yield list(lst)
        return
    for i in range(start, end):
        lst[start], lst[i] = lst[i], lst[start]
        yield from generate_all_permutations_iterator(lst, start + 1, end)
        lst[start], lst[i] = lst[i], lst[start]


def main():
    lst = [1, 2, 3, 4]
    solutions = []
    generate_all_permutations(lst, 0, len(lst), solutions)
    print(sorted(solutions))
    print(len(solutions))
    print(list(generate_all_permutations_iterator(lst, 0, len(lst))))


if __name__ == "__main__":
    main()
