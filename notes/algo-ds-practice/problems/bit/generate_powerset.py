def get_bit_list(bitmask, list_size):
    bit_list = [0] * list_size
    i = list_size - 1
    while bitmask:
        last_bit = bitmask & 1
        bit_list[i] = last_bit
        i -= 1
        bitmask >>= 1
    return bit_list


def generate_powerset(n):
    powerset_size = 2 ** n
    powerset = []
    for bitmask in range(powerset_size):
        powerset.append(get_bit_list(bitmask, n))
    return powerset


def main():
    ans = generate_powerset(10)
    print(len(ans))
    print(ans)


if __name__ == "__main__":
    main()
