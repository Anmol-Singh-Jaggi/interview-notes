def find_index_after_merge(arr1, arr2, target_idx):
    '''
    We are removing the (not necessarily the smallest) k/2 elements in each step.
    So complexity -> O(logk) -> O(log(n+m))
    WARNING: Code gives wrong output on geeks practice!
    '''
    if not arr1:
        return arr2[target_idx]
    if not arr2:
        return arr1[target_idx]
    if target_idx == 0:
        return min(arr1[0], arr2[0])
    len1 = len(arr1)
    len2 = len(arr2)
    idx1 = min((len1 - 1) // 2, target_idx // 2)
    idx2 = min((len2 - 1) // 2, target_idx // 2)
    if arr1[idx1] > arr2[idx2]:
        return find_index_after_merge(arr1, arr2[idx2 + 1:],
                                      target_idx - idx2 - 1)
    else:
        return find_index_after_merge(arr1[idx1 + 1:], arr2,
                                      target_idx - idx1 - 1)


def main():
    arr1 = [1, 2, 3, 4]
    arr2 = [1, 2, 3, 4]
    arr1 = [1, 2, 4, 6, 10]
    arr2 = [4, 5, 6, 9, 12]
    arr1 = [0, 1, 2]
    arr2 = [3]
    ans = find_index_after_merge(arr1, arr2, 3)
    print(ans)


main()
