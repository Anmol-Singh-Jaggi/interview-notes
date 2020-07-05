'''
The Celebrity Problem

In a party of N people, only one person is known to everyone.
Such a person may be present in the party, if yes, he doesn’t know anyone in the party.
We can only ask questions like “does A know B? “.
Find the celebrity in minimum number of questions.

We can describe the problem input as an array of numbers/characters representing persons in the party.
We also have a hypothetical function `knows(A, B) which returns true if A knows B, false otherwise.
How can we solve the problem?

SOLUTION:

Solution 1 (Graph):
Construct a directed graph where an edge (u,v) denotes u knows v.
The finally find if there is a vertex whose in-degree is n-1 and out-degree is 0.
Complexity -> O(n*2).
No. of comparisons -> O(n*2)

Solution 2 (DFS):
Lets say there are 10 people 1..10.
Now starting from smallest to largest... First start from 1.
Lets say 1 does not know people 2-4, but knows 5.
Means that 2-4 can definitely not be a celebrity. Also 1 cannot be a celebrity.
Now switch to 5.
Lets say 5 does not know 6 and 7.
Means 5, 6, 7 cannot be celebrity.
Now switch to 8.
Lets say 8 does not know 9 and 10.
Now 9 and 10 cannot be a celebrity.
8 might or might not be a celebrity.
We'll have to check for every x: `knows(x, 8) == True and knows(8, x) == False`.
Total number of comparisons = Around 3n.
Complexity = O(n)

Solution 3 (Recursion):
We can decompose the problem into combination of smaller instances.
Say, if we know celebrity of N-1 persons, can we extend the solution to N?
We have two possibilities, Celebrity(N-1) may know N, or N already knew Celebrity(N-1).
In the former case, N will be celebrity if N doesn’t know anyone else.
In the latter case, we need to check that Celebrity(N-1) doesn’t know N.
The recurrence of the recursive decomposition is T(N) = T(N-1) + O(N)
T(N) = O(N2)

Solution 4 (Using two Pointers):
The idea is to use two pointers, one from start and one from the end.
Assume the start person is A, and the end person is B.
If A knows B, then A must not be the celebrity.
Else, B must not be the celebrity.
We will find a celebrity candidate at the end of the loop.
Go through each person again and check whether this is the celebrity.
'''
