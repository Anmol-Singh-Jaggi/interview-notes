'''
A trip to mystical land is going to be organized in ByteLand, the city of Bytes.
Unfortunately, there are limited seats say A and there are N number of groups of people.
Every group can have old person o, child c, man m and woman w.
The organizing committee wants to maximize the happiness value of the trip.
Happiness value of the trip is the sum of the happiness value of all the groups that are going.
A group will go for the trip if every member can get a seat (Breaking a group is not a good thing).

The happiness of child c = 4
The happiness of woman w = 3
The happiness of man m = 2
The happiness of the old person o = 1
The happiness of group G, H(G) = (sum of happiness of people in it) * (number of people in the group).
The happiness of the group (‘coow’) = (4 + 1 + 1 + 3) * 4 = 36.

Given the groups and the total seating capacity, the task is to maximize the happiness and print the maximized happiness of the groups going on the trip.



Examples:

Input: groups[] = {“mmo”, “oo”, “cmw”, “cc”, “c”}, A = 5
Output: 43
Pick these groups [‘cmw’, ‘cc’] to get the maximum profit of (4 + 2 + 3) * 3 + (4 + 4) * 2 = 43

Input: groups[] = {“ccc”, “oo”, “cm”, “mm”, “wwo”}, A = 10
Output: 77


SOLUTION:

Its exactly same as Knapsack problem.
Consider one group as an item with weight as the number of people in that group.
And compute an item's value using the rules provided.

Now just apply Knapsack.
'''
