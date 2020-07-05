from algo.number_theory.modular_multiplication.modular_multiplication import modmul


def modpow(first, second, mod):
    if second == 0:
        return 1
    if second == 1:
        return first % mod
    temp = modpow(modmul(first, first, mod), second >> 1, mod)
    if second & 1:
        temp = modmul(temp, first, mod)
    return temp % mod


def main():
    x = modpow(10, 8, 1000000007)
    print(x)


if __name__ == "__main__":
    main()
