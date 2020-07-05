'''
Compute integer average of 2 numbers without overflow.
For the sake of this problem, consider 3 bit numbers (-7 -> 7).

SOLUTION:

If we just do `(a + b)//2`, then we'll get overflow when a=7 and b=7.
But average of 7 and 7 = 7 which is withing 3 bits.

If we do `a + (b-a)//2`, then it will overflow when a = -7 and b = 7.

The correct solution is this:

a//2 + b//2 + (a%2 + b%2)//2
'''
