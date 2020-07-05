'''
Print matrix in spiral order.

Examples:

Input:
        1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10


Input:
        1   2   3   4  5   6
        7   8   9  10  11  12
        13  14  15 16  17  18
Output:
1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11

SOLUTION:

Recursively print the perimeters:

void print(int arr[R][C], int i,
                     int j, int m, int n)
{
    // If i or j lies outside the matrix
    if (i >= m or j >= n)
        return;

    // Print First Row
    for (int p = i; p < n; p++)
        cout << arr[i][p] << " ";

    // Print Last Column
    for (int p = i + 1; p < m; p++)
        cout << arr[p][n - 1] << " ";

    // Print Last Row, if Last and
    // First Row are not same
    if ((m - 1) != i)
        for (int p = n - 2; p >= j; p--)
            cout << arr[m - 1][p] << " ";

    // Print First Column,  if Last and
    // First Column are not same
    if ((n - 1) != j)
        for (int p = m - 2; p > i; p--)
            cout << arr[p][j] << " ";

    print(arr, i + 1, j + 1, m - 1, n - 1);
}
'''
