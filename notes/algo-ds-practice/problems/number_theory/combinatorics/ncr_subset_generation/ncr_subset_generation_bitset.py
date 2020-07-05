def generate_next(bitset_string):
    # TODO: Implement while revisings
    return bitset_string


def generate_subsets(n, r):
    # TODO: Set to 0000...1111(r)
    bitset_string = [0] * (n - r) + [1] * r
    while True:
        print(bitset_string)
        bitset_string_old = bitset_string
        bitset_string = generate_next(bitset_string)
        if bitset_string_old == bitset_string:
            break


generate_subsets(5, 2)