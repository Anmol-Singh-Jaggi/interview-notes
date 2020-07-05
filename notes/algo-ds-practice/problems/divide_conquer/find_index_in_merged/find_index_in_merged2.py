def find_index_after_merge(arr1, arr2, target_idx):
    '''
    We are removing either half of arr1 or half of arr2 at each step.
    So complexity -> O(logn + logm)
    Just remember the implementation properly.
    '''
    if not arr1:
        return arr2[target_idx]
    if not arr2:
        return arr1[target_idx]
    len1 = len(arr1)
    len2 = len(arr2)
    # CAREFUL: Not (len-1) // 2
    mid_idx1 = len1 // 2
    mid_idx2 = len2 // 2
    if target_idx > mid_idx1 + mid_idx2:
        if arr1[mid_idx1] > arr2[mid_idx2]:
            return find_index_after_merge(arr1, arr2[mid_idx2 + 1:],
                                          target_idx - mid_idx2 - 1)
        else:
            return find_index_after_merge(arr1[mid_idx1 + 1:], arr2,
                                          target_idx - mid_idx1 - 1)
    else:
        if arr1[mid_idx1] > arr2[mid_idx2]:
            return find_index_after_merge(arr1[:mid_idx1], arr2, target_idx)
        else:
            return find_index_after_merge(arr1, arr2[:mid_idx2], target_idx)


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
