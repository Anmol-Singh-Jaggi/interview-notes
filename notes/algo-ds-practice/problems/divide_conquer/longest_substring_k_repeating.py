"""
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

SOLUTION:

Count the frequency of all the characters.
Then split the string about the characters which have less than k frequency.
Do this recursively and return the max element.
The split will happen not more than 26 times.
So complexity -> O(n*26) = O(n).

"""
from collections import Counter


def longest_substring(self, s: str, k: int) -> int:
    counter = Counter(s)
    for c, count in counter.items():
        if count < k:
            return max(self.longest_substring(sub, k) for sub in s.split(c))
    return len(s)
