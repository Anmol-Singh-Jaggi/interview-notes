'''
Brian Kernighan’s Algorithm:
Subtraction of 1 from a number toggles all the bits (from right to left) till the rightmost
set bit(including the rightmost set bit).
So if we subtract a number by 1 and do bitwise & with itself (n & (n-1)), we unset the rightmost set bit.
If we do n & (n-1) in a loop and count the no of times loop executes we get the set bit count.
The beauty of this solution is the number of times it loops is equal to the number of set bits in a given integer.

   1  Initialize count: = 0
   2  If integer n is not zero
      (a) Do bitwise & with (n-1) and assign the value back to n
          n: = n&(n-1)
      (b) Increment count by 1
      (c) go to step 2
   3  Else return count

'''


def countSetBits(n):
    count = 0
    while (n):
        n &= (n - 1)
        count += 1
    return count
