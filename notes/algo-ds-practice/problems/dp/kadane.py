def kadane(arr):
    max_global = -1e9
    max_local = max_global
    for elem in arr:
        max_local = max(elem, elem + max_local)
        max_global = max(max_global, max_local)
    return max_global


def main():
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    ret = kadane(arr)
    print(ret)


if __name__ == "__main__":
    main()