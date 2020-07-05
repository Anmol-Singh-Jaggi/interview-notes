'''
Given a matrix consisting of 2 elements 'X' and 'O', where 'O' represents water and 'X' represents land, convert all the 'O's covered by X's to X.
'Covered' meaning covered on all 8 sides.
Also, if there are 3 neighbouring O's covered by X's from everywhere, then all of them need to be converted.
So basically image O's as an island. We need to destroy all islands.
We can assume that the matrix is surrounded by all water.

SOLUTION:

We can basically do a DFS and mark all the boundary O's and their neighbouring O's as 'safe' meaning they wont be converted.
We can store all of these positions in a set.
Then we can simply iterate through the matrix and check if (i,j) in safe_set or not.
If it is, then convert it to X.
But this requires O(n*m) space complexity.

We can do it in-place by converting all O's to a third character (for example '-') in the DFS stage.
'''
