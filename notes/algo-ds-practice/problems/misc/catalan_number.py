'''
Catalan number `cat(n)`.

Recursive formula:
cat(5) = cat(0)*cat(4) + cat(1)*cat(3) + .. cat(4)*cat(0)

Direct formula:
cat(n) = (2n)! / (n+1)!(n)!

Answer for:

 - Number of BST given the number of unique keys.
 - Number of binary trees with the same preorder traversal.
 - Number of balanced parantheses sequence --> HOW??
 - Number of full binary trees with n+1 leaves.
 - Number of ways of associating n applications of a binary operator.
   For n = 3, for example, we have the following five different parenthesizations of four factors:
   ((ab)c)d     (a(bc))d     (ab)(cd)     a((bc)d)     a(b(cd))
   Actually, successive applications of a binary operator can be represented in terms of a full binary tree.

'''
