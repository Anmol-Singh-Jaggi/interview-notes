'''
Given three integers x,y and z you need to find the sum of all the numbers formed by
having 4 atmost x times, 5 atmost y times and 6 atmost z times as a digit.
Note : Output the sum modulo 10^9+7.

EXAMPLE:

Input - 1 1 1
Output - 3675
The ans for the input is
4 + 5 + 6 + 45 + 54 + 56 + 65 + 46 + 64 + 456 + 465 + 546 + 564 + 645 + 654 = 3675

SOLUTION:

Let us say f(x,y,z) represents the sum of all numbers formed using  exactly x 4's, y 5's and z 6's.
So, the required value can be calculated as given below.

for (int i = 0; i <= x; ++ i)
    for (int j = 0; j <= y; ++ j)
      for (int k = 0; k <= z; ++ k)
            ans += f(i,j,k);


Now, let us see how to calculate the value of f(x,y,z).
Let us consider that g(x,y,z) represents number of numbers which have x number of 4's, y number of 5's and z number of 6's.
then the recurrence relation is:

f(x,y,z) = A + B + C
where
A = 10*f(x-1,y,z) + 4*g(x-1,y,z)
B = 10*f(x,y-1,z) + 5*g(x,y-1,z)
C = 10*f(x,y,z-1) + 6*g(x,y,z-1)

Explanation:
Take A:
Lets say we are trying to find f(4, 3, 5).
g(3, 3, 5) will return the number of numbers that can be formed by 3 x, 3 y, 5 z
Now what if we want to append one 4 at the end of each of those numbers.
Lets say 456 is a number. If we multiply it by 10 and then add 4, we'll get 4564.
Now if we have 2 numbers 456 and 654, if we multiply their sum by 10 and add 4 twice, we'll get the sum of (4564 + 6544).
This is the idea.

Note that g(x, y, z) is simply (x+y+z)! / (x! * y! * z!)
'''
