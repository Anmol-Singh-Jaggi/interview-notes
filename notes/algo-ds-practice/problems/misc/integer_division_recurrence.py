'''
Given a fraction, find recurring sequence of digits if exists, otherwise print “No recurring sequence”.

Examples:

Input  : Numerator = 8, Denominator = 3
Output : Recurring sequence is 6
Explanation : 8/3 = 2.66666666.......

Input : Numerator = 50, Denominator = 22
Output : Recurring sequence is 27
Explanation : 50/22 = 2.272727272.....

Input : Numerator = 11, Denominator = 2
Output : No recurring sequence
Explanation : 11/2 = 5.5

SOLUTION:
Let us simulate the process of converting fraction to decimal.
Let us look at the part where we have already figured out the integer part which is floor(numerator/denominator).
Now we are left with ( remainder = numerator%denominator ) / denominator.
If you remember the process of converting to decimal, at each step we do the following :

Multiply the remainder by 10.
Append remainder / denominator to result.
Remainder = remainder % denominator.
At any moment, if remainder becomes 0, we are done.

However, when there is a recurring sequence, remainder never becomes 0.
For example if you look at 1/3, the remainder never becomes 0.

Below is one important observation :
If we start with remainder ‘rem’ and if the remainder repeats at any point of time, the digits between the two occurrence of ‘rem’ keep repeating.

So the idea is to store seen remainders in a map. Whenever a remainder repeats, we return the sequence before the next occurrence.
'''
