"""
Giving a dictionary and a string ‘str’, find the longest string in dictionary which can be formed by deleting some characters of the given ‘str’.

Examples:

Input : dict = {"ale", "apple", "monkey", "plea"}
        str = "abpcplea"
Output : apple

Input  : dict = {"pintu", "geeksfor", "geeksgeeks",
                                        " forgeek"}
         str = "geeksforgeeks"
Output : geeksgeeks


SOLUTION:

Iterate through all the words in the dictionary and check if dict_word is a subsequence of input_word.
Take the best of all the answers.

How to check subsequence??

SOLUTION 1:
Just iterate.
Complexity -> O(n), where n is the length of the larger string.

SOLUTION 2:
Create a list of indices of a every character in the larger string.
For example, if s="abc", t="bahbgdca"
t_indices = {'a':[1,7], 'b':[0,3], 'c':[6]}

Now iterate through the smaller string and keep doing upper bound on the larger string.
Complexity -> O(n) for preprocessing
O(m*log(n)) for upper bound.
This solution is better if n >>> m, and we have multiple queries.

"""
from bisect import bisect


def is_subsequence_linear(smaller, larger):
    sidx, lidx = 0, 0
    while sidx < len(smaller) and lidx < len(larger):
        if smaller[sidx] == larger[lidx]:
            sidx += 1
            lidx += 1
            continue
        lidx += 1
    return sidx == len(smaller)


def is_subsequence(smaller, larger):
    char_indices = {}
    for i in range(0, len(larger)):
        lst = char_indices.get(larger[i], [])
        lst.append(i)
        char_indices[larger[i]] = lst
    curr_idx = -1
    for i in range(0, len(smaller)):
        indices = char_indices.get(smaller[i], None)
        if indices is None:
            return False
        next_idx = bisect(indices, curr_idx)
        if next_idx == len(indices):
            return False
        curr_idx = indices[next_idx]
    return True


def main():
    smaller = 'abc'
    larger = 'bahbgdca'
    ans = is_subsequence(smaller, larger)
    print(ans)


main()
