def get_next_ncr(lst):
    '''
    Returns the lexicographically next list with the same number of 1's
    1. Find the righmost 0 that has a one 1 on the right. If not found then exit.
    2. Make that 0 as 1, and completely overwrite the right side of that 0 with
    the smallest lexico possible substring such that the number of 0's and 1's is maintained.
    3. This algo is essentially the same as next_permutation().
    '''
    pass


def main():
    lst = [1, 0, 1, 0]
    ans = get_next_ncr(lst)
    print(ans)


if __name__ == "__main__":
    main()
