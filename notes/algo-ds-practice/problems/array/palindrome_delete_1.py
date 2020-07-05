'''
Given a non-empty string s, you may delete at most one character.
Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True

Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.


SOLUTION:

If the beginning and end characters of a string are the same (ie. s[0] == s[s.length - 1]), then whether the inner characters are a palindrome (s[1], s[2], ..., s[s.length - 2]) uniquely determines whether the entire string is a palindrome.

Suppose we want to know whether s[i], s[i+1], ..., s[j] form a palindrome.
If s[i] == s[j] then we may make i++; j--.
Otherwise, the palindrome must be either s[i+1], s[i+2], ..., s[j] or s[i], s[i+1], ..., s[j-1], and we should check both cases.
'''
