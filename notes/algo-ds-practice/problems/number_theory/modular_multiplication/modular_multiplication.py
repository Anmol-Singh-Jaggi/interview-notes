def modmul(first, second, mod):
    """
    Multiplies 2 numbers without using the '*' operator.
    Also prevents overflow.
    """
    if second == 0:
        return 0
    if second & 1:
        return (first % mod + modmul(first << 1, second >> 1, mod)) % mod
    else:
        return modmul(first << 1, second >> 1, mod)


def main():
    x = modmul(5, 41, 10000)
    print(x)


if __name__ == "__main__":
    main()
