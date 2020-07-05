# Verified on https://leetcode.com/problems/implement-strstr
import string
from functools import lru_cache


@lru_cache(maxsize=None)
def get_char_code(ch, char_set=string.ascii_letters + string.digits):
    # We could have also used:
    # return ord(ch) - ord('0')
    return char_set.index(ch)


def rabin_karp(haystack, needle):
    # CAREFUL: Beware of these corner cases!
    if needle == "":
        return 0
    if len(needle) == 0 or len(needle) > len(haystack):
        return -1
    HASH_MOD = 1000000007
    # We can use any number as base, but its better to
    # take the alphabet size to minimize collisions
    BASE = 26
    needle_hash = 0
    haystack_hash = 0
    for i in range(needle):
        needle_char = get_char_code(needle[i])
        haystack_char = get_char_code(haystack[i])
        needle_hash = (BASE * needle_hash + needle_char) % HASH_MOD
        haystack_hash = (BASE * haystack_hash + haystack_char) % HASH_MOD
    if haystack_hash == needle_hash and needle == haystack[0 : len(needle)]:
        return 0
    # Now compute hashes on a rolling basis
    base_power_up = pow(BASE, (len(needle) - 1), HASH_MOD)
    for i in range(len(needle), len(haystack)):
        haystack_start_pos = i + 1 - len(needle)
        haystack_end_pos = i + 1
        old_char = get_char_code(haystack[haystack_start_pos - 1])
        ch = get_char_code(haystack[i])
        haystack_hash = (
            (haystack_hash - base_power_up * old_char) * BASE + ch
        ) % HASH_MOD
        if (
            haystack_hash == needle_hash
            and needle == haystack[haystack_start_pos:haystack_end_pos]
        ):
            return haystack_start_pos
    return -1


def main():
    haystack = "abcs"
    needle = ""
    print(rabin_karp(haystack, needle))


if __name__ == "__main__":
    main()
