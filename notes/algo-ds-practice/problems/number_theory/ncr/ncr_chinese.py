'''
Lets say we have to find nCr(1000, 500) % 20.
20's prime factors are 2 and 5.
We can computer ncr % 2 = r1 and ncr % 5 = r2 using Lucas Theorem.
Now we have 2 equations:
ans = r1 (mod 2)
ans = r2 (mod 5)

We can compute the answer using Chinese Remainder Theorem.

Total time complexity = O(sqrt(p)) + O(logn)**2
Absolutely blazing fast!!
'''
