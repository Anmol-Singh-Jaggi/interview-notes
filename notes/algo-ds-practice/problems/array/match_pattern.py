'''
Find all strings that match specific pattern in a dictionary

Given a dictionary of words, find all strings that matches the given pattern where every character in the pattern is uniquely mapped to a character in the dictionary.

Examples:

Input:
dict = ["abb", "abc", "xyz", "xyy"];
pattern = "foo"
Output: [xyy abb]
Explanation:
xyy and abb have same character at index 1 and 2 like the pattern

Input:
dict = ["abb", "abc", "xyz", "xyy"];
pat = "mno"
Output: [abc xyz]
Explanation:
abc and xyz have all distinct characters, similar to the pattern

Input:
dict = ["abb", "abc", "xyz", "xyy"];
pattern = "aba"
Output: []
Explanation:
Pattern has same character at index 0 and 2.
No word in dictionary follows the pattern.

Input:
dict = ["abab", "aba", "xyz", "xyx"];
pattern = "aba"
Output: [aba xyx]
Explanation:
aba and xyx have same character at index 0 and 2 like the pattern


SOLUTION 1:

Encode all strings in a certain way such that finding the pattern becomes trivial.
For example:
abb -> 122
bcc -> 122
abca -> 1231

Now encode all the strings in the dictionary, and put them into a hashset.
Then just check if the input string's encoding is present in the hashmap.


SOLUTION 2:
Keep 2 pointers i and j on the 2 strings being matched.
Also, keep 2 dictionaries which map one string's char to another and vice-versa.
Think about why we need bidirectional map and not unidirectional.
Then just start iterating both strings simulatenously, and keep updating the hashmaps.
While iterating, keep a check on any inconsistency.
Let char1 = str1[i] and char2 = str[j].
If char1 not in dict1 and char2 not in dict2, then insert new mappings.
Then if char1 in dict1, then dict1[char1] == char2 else return False
Also, if char1 not in dict1, then dict2[char2] == char1 else return False.
'''
