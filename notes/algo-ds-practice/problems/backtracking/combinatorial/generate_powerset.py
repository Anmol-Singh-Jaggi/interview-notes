def generate_powerset(n, selected, solutions):
    if n < 0:
        solutions.append(selected)
        return
    # Exclude n-1.
    generate_powerset(n - 1, selected, solutions)
    # Include n-1.
    generate_powerset(n - 1, selected + [n], solutions)


def generate_powerset_iterator(n, selected):
    if n < 0:
        yield list(selected)
        return
    # Exclude n-1.
    yield from generate_powerset_iterator(n - 1, selected)
    # Include n-1.
    yield from generate_powerset_iterator(n - 1, selected + [n])


def main():
    for elem in generate_powerset_iterator(2, []):
        print(elem)


main()
