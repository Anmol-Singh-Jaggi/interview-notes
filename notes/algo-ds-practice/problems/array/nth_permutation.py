from collections import Counter
from functools import lru_cache


@lru_cache(maxsize=None)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def get_num_permutations(char_counter):
    num = 0
    den = 1
    for value in char_counter.values():
        num += value
        den *= factorial(value)
    num = factorial(num)
    return num // den


def nth_permutation(char_counter, n):
    """
    1. First count frequencies of all characters in an array freq[].
    2. Now from the first smallest character present in the string (smallest index i such that freq[i] > 0), we compute the number of maximum permutation possible after setting that particular i-th character as the first character.
    If n <= num_perms, then we set that character as the first result output character, decrement freq[i], and continue same for remaining n-1 characters.
    3. On the other hand, if n > num_perms, iterate for the next character in the frequency table and update the count over and over again until we find a character that produces a count greater than the required n.
    Time Complexity: O(n)
    To understand, simulate for ('abcd', 13).
    """
    if n == 1:
        return "".join(sorted(char_counter.elements()))
    ans = None
    # One-by-one try to put every char in the first place
    # to find the right character suitable for first place.
    for char in sorted(char_counter.keys()):
        if char_counter[char] > 0:
            char_counter[char] -= 1
        num_perms = get_num_permutations(char_counter)
        if n <= num_perms:
            ans = char + nth_permutation(char_counter, n)
            break
        else:
            n -= num_perms
        char_counter[char] += 1

    return ans


def main():
    str = "abcd"
    char_counter = Counter(str)
    n = 13
    ans = nth_permutation(char_counter, n)
    print(ans)


if __name__ == "__main__":
    main()
