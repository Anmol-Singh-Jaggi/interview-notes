def next_permutation(lst):
    """
    1. Find the highest index k such that str[k] < str[k+1].
       If no such index exists, the permutation is the last permutation.
       Note that all the elements after k will be in non-ascending order.
    2. Find the highest index l > k such that str[l] > str[k].
       Such an 'l' must exist, since k+1 is such an index.
       Basically we want the smallest element in the range [k+1, end)
       bigger than str[k].
    3. Swap str[k] with str[l].
    4. Reverse the order of all of the elements after index k.
       Basically we want to sort it, but since its already in decreasing order
       so reversing is same as swapping.
    """
    k_idx = None
    for i in range(0, len(lst) - 1):
        if lst[i] < lst[i + 1]:
            k_idx = i
    if k_idx is None:
        return None
    l_idx = None
    # CAREFUL: l_idx cannot simply be the last index of the array
    # as it is possible that the number there is smaller than arr[k_idx].
    # For example: 1 2 5 4 3 1
    for i in range(k_idx + 1, len(lst)):
        if lst[i] > lst[k_idx]:
            l_idx = i
    lst[k_idx], lst[l_idx] = lst[l_idx], lst[k_idx]
    return lst[: k_idx + 1] + lst[len(lst): k_idx: -1]


def main():
    lst = [1, 2, 3, 3]
    while True:
        lst = next_permutation(lst)
        print(lst)
        if not lst:
            break


if __name__ == "__main__":
    main()
