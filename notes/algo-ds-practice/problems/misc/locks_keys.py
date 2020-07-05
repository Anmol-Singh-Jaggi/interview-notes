'''

Given a set of n nuts of different sizes and n bolts of different sizes.
There is a one-one mapping between nuts and bolts.
Match nuts and bolts efficiently.

Constraint: Comparison of a nut to another nut or a bolt to another bolt is not allowed.
It means nut can only be compared with bolt and bolt can only be compared with nut to see which one is bigger/smaller.

Other way of asking this problem is, given a box with locks and keys where one lock can be opened by one key in the box.
We need to match the pair.


SOLUTION:

Brute force Way:
Start with the first bolt and compare it with each nut until we find a match.
In the worst case we require n comparisons.
Doing this for all bolts gives us O(n^2) complexity.

Quick Sort Way:
We can use quick sort technique to solve this.
We represent nuts and bolts in character array for understanding the logic.

Nuts represented as array of character
char nuts[] = {‘@’, ‘#’, ‘$’, ‘%’, ‘^’, ‘&’}

Bolts represented as array of character
char bolts[] = {‘$’, ‘%’, ‘&’, ‘^’, ‘@’, ‘#’}

This algorithm first performs a partition by picking last element of bolts array as pivot, rearrange the array of nuts and returns the partition index ‘i’ such that all nuts smaller than nuts[i] are on the left side and all nuts greater than nuts[i] are on the right side.
Next using the nuts[i] we can partition the array of bolts.
Partitioning operations can easily be implemented in O(n).
This operation also makes nuts and bolts array nicely partitioned.
Now we apply this partitioning recursively on the left and right sub-array of nuts and bolts.
At the end, both lists will be sorted.
As we apply partitioning on nuts and bolts both so the total time complexity will be Θ(2*nlogn) = Θ(nlogn) on average.

Here for the sake of simplicity we have chosen last element always as pivot.
We can do randomized quick sort too.
'''
