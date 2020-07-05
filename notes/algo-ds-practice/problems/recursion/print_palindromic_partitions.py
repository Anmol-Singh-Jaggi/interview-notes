"""
Given a string, find all possible palindromic partitions of given string.
For example:

Input = 'nitin'
Output:
n, i, t, i, n
n, iti, n
nitin

Input = 'geeks'
Output:
g, e, e, k, s
g, ee, k, s

Input = 'daddad'
Output:
d a d d a d
d a d dad
d a dd a d
d adda d
dad d a d
dad dad
daddad
"""
from collections import deque
from functools import lru_cache


inp = ""


@lru_cache(maxsize=None)
def is_palindrome(start, end):
    rev = inp[end : start - 1 : -1]
    if start == 0:
        rev = inp[end::-1]
    return inp[start : end + 1] == rev


@lru_cache(maxsize=None)
def palin_partitions(start):
    '''
    Returns a list of dequeus where each deque represents 1 partioning combo.
    '''
    ans = []
    if start == len(inp):
        ans.append(deque())
        return ans
    if start == len(inp) - 1:
        dq = deque()
        dq.append(inp[start])
        ans.append(dq)
        return ans
    for i in range(start, len(inp)):
        if is_palindrome(start, i):
            sub_ans = palin_partitions(i + 1)
            for elem in sub_ans:
                elem_copy = deque(elem)
                elem_copy.appendleft(inp[start : i + 1])
                ans.append(elem_copy)
    return ans


def main():
    global inp
    inp = "daddad"
    ans = palin_partitions(0)
    print(ans)


main()
