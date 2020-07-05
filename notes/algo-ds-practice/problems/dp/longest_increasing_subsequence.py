from bisect import bisect_left


def longest_increasing_subsequence(arr):
    """
    https://stackoverflow.com/a/2631810/1925388
    Verified on Leetcode.
    """
    # smallest[x] = Smallest element that ends an increasing subsequence of length 'x+1'.
    smallest = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] > smallest[-1]:
            # We have found a new LIS!
            smallest.append(arr[i])
        else:
            # idx is the smallest index in arr such that arr[idx] >= arr[i]
            # The idea is that arr[i] can potentially replace a previous ending element
            # in `smallest`.
            # For example, if smallest is `1, 5, 10, 15`, and arr[i] = 9
            # Then we know that 9 can replace 10, meaning that 9 is now the
            # smallest element which ends an increasing subsequence of length 3.
            # Basically we are trying to minimize every smallest[x].
            # For an increasing subsequence of length x, we are interested in the
            # subsequence with the lowest end value, so that further options to extend
            # are maximized.
            idx = bisect_left(smallest, arr[i])
            smallest[idx] = arr[i]
    return len(smallest)


def main():
    arr = [5, 6, 2, 5, 7, 10]
    ans = longest_increasing_subsequence(arr)
    print(ans)


if __name__ == "__main__":
    main()
