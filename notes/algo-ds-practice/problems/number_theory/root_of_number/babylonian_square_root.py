def square_root_babylonian(num, acc=0.000001):
    first = num
    second = 1
    # first * second will always be = n
    # The idea is to decrease first and increase second gradually,
    # until they converge together to the value sqrt(n).F
    while first - second > acc:
        first = (first + second) / 2
        second = num / first
    return first


def main():
    print(square_root_babylonian(100))


if __name__ == "__main__":
    main()
