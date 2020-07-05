"""
Given two strings str1 and str2, write a function that prints all interleavings of the given two strings.
You may assume that all characters in both strings are different.
Example:

Input: str1 = "AB",  str2 = "CD"
Output:
    ABCD
    ACBD
    ACDB
    CABD
    CADB
    CDAB

Input: str1 = "AB",  str2 = "C"
Output:
    ABC
    ACB
    CAB

An interleaved string of given two strings preserves the order of characters in individual strings.
For example, in all the interleavings of above first example, ‘A’ comes before ‘B’ and ‘C’ comes before ‘D’.

SOLUTION:

Let the length of str1 be m and the length of str2 be n.
Let us assume that all characters in str1 and str2 are different.
Let count(m, n) be the count of all interleaved strings in such strings.

The value of count(m, n) can be written as following:
count(m, n) = count(m-1, n) + count(m, n-1)
count(1, 0) = 1 and count(0, 1) = 1

To print all interleavings, we can first fix the first character of str1[0..m-1] in output string, and recursively call for str1[1..m-1] and str2[0..n-1].
And then we can fix the first character of str2[0..n-1] and recursively call for str1[0..m-1] and str2[1..n-1].
"""


def print_all_interleaving(arr1, arr2, right1, right2):
    if right1 == -1:
        ans = [arr2[0: right2 + 1]]
        return ans
    if right2 == -1:
        ans = [arr1[0: right1 + 1]]
        return ans
    ans1 = print_all_interleaving(arr1, arr2, right1 - 1, right2)
    ans = []
    for interleaving in ans1:
        interleaving_new = interleaving.copy()
        interleaving_new.append(arr1[right1])
        ans.append(interleaving_new)
    ans2 = print_all_interleaving(arr1, arr2, right1, right2 - 1)
    for interleaving in ans2:
        interleaving_new = interleaving.copy()
        interleaving_new.append(arr2[right2])
        ans.append(interleaving_new)
    return ans


def main():
    arr1 = [1, 2]
    arr2 = [3, 4]
    ans = print_all_interleaving(arr1, arr2, len(arr1) - 1, len(arr2) - 1)
    print(ans)


main()
