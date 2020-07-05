'''
Given a matrix, sort the rows of matrix in ascending order followed by sorting the columns in descending order.
Examples :

Input : a[3][3] = {{1, 2, 3},
                  {4, 5, 6},
                  {7, 8, 9}};
Output : 7 8 9
         4 5 6
         1 2 3

Input : a[3][3] = {{3, 2, 1},
                  {9, 8, 7},
                  {6, 5, 4}};
Output : 7 8 9
         4 5 6
         1 2 3

SOLUTION:

1) Traverse all rows one by one and sort rows in ascending order using simple array sort.
2) Convert matrix to its transpose.
3) Again sort all rows, but this time in descending order.
4) Again convert matrix to its transpose.
'''
