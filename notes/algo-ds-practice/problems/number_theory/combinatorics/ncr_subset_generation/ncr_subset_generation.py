def generate_subsets(n, r, start):
    '''
    Choose r from [n-start] elements.
    This small code handles ALL the edge cases! :D
    Just remember the base cases for interview prep.
    '''
    subsets = []
    if n == start:
        return subsets
    if r == 0:
        subsets.append([0] * (n - start))
        return subsets
    if n - start == r:
        subsets.append([1] * (n - start))
        return subsets
    # We can select current element at index `start`,
    # and then generate subsets for (n, r-1, start+1).
    # Answer would be '1'(signifying selection of current element) prepended to all of these subsets.
    #
    # Or we can not select this element and then generate subsets for (n, r, start+1)
    # Answer would be '0' prepended to all of these subsets.
    subsets_include_current = generate_subsets(n, r - 1, start + 1)
    subsets_exclude_current = generate_subsets(n, r, start + 1)
    for subset in subsets_exclude_current:
        subsets.append([0] + subset)
    for subset in subsets_include_current:
        subsets.append([1] + subset)
    return subsets


def get_subsets(n, r):
    subsets = generate_subsets(n, r, 0)
    return subsets


subsets = get_subsets(10, 5)
print(len(subsets))
for subset in subsets:
    print(subset)