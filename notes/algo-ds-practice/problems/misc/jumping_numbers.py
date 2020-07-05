'''
A number is called as a Jumping Number if all adjacent digits in it differ by 1.
The difference between ‘9’ and ‘0’ is not considered as 1.
All single digit numbers are considered as Jumping Numbers.
For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.

Given a positive number x, print all Jumping Numbers smaller than or equal to x.
The numbers can be printed in any order.

Example:



Input: x = 20
Output:  0 1 2 3 4 5 6 7 8 9 10 12

Input: x = 105
Output:  0 1 2 3 4 5 6 7 8 9 10 12
         21 23 32 34 43 45 54 56 65
         67 76 78 87 89 98 101

Note: Order of output doesn't matter,
i.e. numbers can be printed in any order

SOLUTION:

An Efficient Solution can solve this problem in O(k) time where k is number of Jumping Numbers smaller than or equal to x.
The idea is use BFS or DFS.

State transition logic for BFS:

q = [0]
while (not q.is_empty()):
    num = q.dequeue()
    if num<= x:
        print(str(num), end =' ')
        last_dig = num % 10
        if last_dig == 0:
            q.enqueue((num * 10) + (last_dig + 1))
        elif last_dig == 9:
            q.enqueue((num * 10) + (last_dig - 1))
        else:
            q.enqueue((num * 10) + (last_dig - 1))
            q.enqueue((num * 10) + (last_dig + 1))
'''
