'''
You have a list of programmers who can code 'x' solutions per day. Lets call it their 'skill'.
We have a *jealousy* value 'j' signifying that they are jealous of any other
programmer whose skill >= j more than themselves.
You have to form groups of all these programmers such that there is no jealousy in any of the groups.
Also, each of the programmers have some money with them.
You need to return the maximum total money of any of any group possible.

For example:

skills = [3, 2, 3, 4, 5]
money = [5, 4, 3, 2, 1]
jealousy = 2

Answer = 12
(First, second and third programmers)

SOLUTION:

Let a programmer be defined as (skill, money).
Now sort the programmer list.
Employ a 2-pointer window algorithm while maintaining non-jealousy in every window.
The max money of any window generated is the answer.
'''
