'''
https://www.spoj.com/problems/ABCDEF/

**Description**
You are given a set S of integers between -30000 and 30000 (inclusive).
Find the total number of sextuples that satisfy:
 a*b+c = (e+f)*d

**Input**
The first line contains integer N (1 ≤ N ≤ 100), the size of a set S.
Elements of S are given in the next N lines, one integer per line. Given numbers will be distinct.

**Output**
Output the total number of plausible sextuples.

SOLUTION:

It can be done by first iterating over the input array in a 3-nested loop and generating all the n^3 triplets for {a,b,c}, and storing LHS formed in a hashmap with the count.

Then do the same thing for {d,e,f}.

Now for each element in hashmap1 'x', multiply hashmap1[x]*hashmap2[x] and add it to the answer cumulatively.

Can alternatively be done by generating the 2 arrays of n^3 size, sorting them and doing binary-search (lower bound/upper bound).
'''
