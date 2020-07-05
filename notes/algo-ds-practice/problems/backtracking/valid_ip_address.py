'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A, B, C, and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

Examples :

Input : 25525511135
Output : [“255.255.11.135”, “255.255.111.35”]
Explanation:
These are the only valid possible
IP addresses.

Input : "25505011535"
Output : []
Explanation :
We cannot generate a valid IP
address with this string.

SOLUTION:

Place the dots in all the n^3 places one by one and check if the result is a valid IP.
'''
