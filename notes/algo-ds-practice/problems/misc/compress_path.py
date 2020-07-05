'''
A person wants to go from origin to a particular location, he can move in only 4 directions(i.e East, West, North, South) but his friend gave him a long route, help a person to find minimum moves so that he can reach to the destination.

Note: You need to print the lexicographically sorted string. Assume the string will have only ‘E’ ‘N’ ‘S’ ‘W’ characters.

Example:
Input
2
SSSNEEEW
NESNWES

Output
EESS
E

SOLUTION:

1. Traverse through the string and note down the number of times the directions were addressed in route.
2. Check the maximum of South and North directions and add the (MAX - MIN) to the route.
E.g, SSSNNNNN - S(3) & N(5) - Result - NN
3. Repeat the step 2 for East and West directions.
4. Compile the result by combining the results of 2 & 3 steps such that they are lexicographically sorted.(If Es are the result of 3, they come first.)

'''
