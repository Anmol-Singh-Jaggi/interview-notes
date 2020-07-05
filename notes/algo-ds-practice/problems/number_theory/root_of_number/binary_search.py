def nth_root_binary_search(num, n, acc=0.0000001):
    if num <= 1:
        return num

    start = 1
    end = num / 2
    while start <= end:
        mid = (start + end) / 2
        # If num is a perfect square
        if abs(mid ** n - num) <= acc:
            return mid
        elif mid ** n < num:
            start = mid
            ans = mid
        else:
            end = mid
    return ans


def main():
    n = 4
    root = nth_root_binary_search(100, n)
    print(root ** n)


if __name__ == "__main__":
    main()
