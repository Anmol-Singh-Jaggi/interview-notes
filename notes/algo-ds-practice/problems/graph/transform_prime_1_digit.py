'''
Given two four digit prime numbers, suppose 1033 and 8179, we need to find the shortest path from 1033 to 8179 by altering only single digit at a time such that every number that we get after changing a digit is prime. For example a solution is 1033, 1733, 3733, 3739, 3779, 8779, 8179

Examples:

Input : 1033 8179
Output :6

Input : 1373 8017
Output : 7

Input  :  1033 1033
Output : 0


SOLUTION:

We will make a graph and run BFS.
Generate all the 4-digit primes until 9999.
Then run a nested loop on the prime list, and connect 2 primes if they differ just by 1 digit.
Then start a BFS from source to destination.
'''
