'''
Given a Binary Tree, find size of the Largest Independent Set(LIS) in it.
A subset of all tree nodes is an independent set if there is no edge between any two nodes of the subset.
See Geeks for example.

SOLUTION:

Let LISS(X) indicates size of largest independent set of a tree with root X.

LISS(X) = MAX
{
    (1 + sum of LISS for all grandchildren of X),
    (sum of LISS for all children of X)
}
'''
