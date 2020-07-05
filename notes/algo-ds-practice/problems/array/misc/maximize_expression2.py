"""
Maximize arr[j] – arr[i] + arr[l] – arr[k],
such that i < j < k < l.
Find the maximum value of arr[j] – arr[i] + arr[l] – arr[k], such that i < j < k < l

Example:

Let us say our array is {4, 8, 9, 2, 20}
Then the maximum such value is 23 (9 - 4 + 20 - 2)

SOLUTION:

We will use Dynamic Programming to solve this problem.
For this we create four 1-Dimensional DP tables.
Let us say there are four DP tables as – table1[], table2[], table3[], table4[]
Then to find the maximum value of arr[l] – arr[k] + arr[j] – arr[i], such that i < j < k < l:
table1[] should store the maximum value of arr[l]
(table1[i] = the max of all elements from i to n-1)

table2[] should store the maximum value of arr[l] – arr[k]
(table2[k] = the max of arr[l] - arr[k] from arr[k] to arr[n-1] and l > k)

table3[] should store the maximum value of arr[l] – arr[k] + arr[j]
(table3[j] = the max of arr[l] - arr[k] + arr[j] from arr[j] to arr[n-1] and l > k and k > j)

Same thing for table4 as well.

Then the maximum value would be present in index 0 of table4 which will be our required answer.
Complexity -> O(n)

See the code for better explanation.
NOTE: The input array will always have atleast 4 elements.
NOTE 2:
This problem is simple yet powerful.
The problem can be generalized to any expression under the given conditions.
For example:
Find the maximum value of arr[j] – 2*arr[i] + 3*arr[l] – 7*arr[k], such that i < j < k < l.
"""
from math import inf


def max_quad_expression(arr):
    table1 = [-inf] * (len(arr) + 1)
    table2 = [-inf] * len(arr)
    table3 = [-inf] * (len(arr) - 1)
    table4 = [-inf] * (len(arr) - 2)

    for i in range(len(arr) - 1, -1, -1):
        table1[i] = max(table1[i + 1], arr[i])

    for i in range(len(arr) - 2, -1, -1):
        table2[i] = max(table2[i + 1], table1[i + 1] - arr[i])

    for i in range(len(arr) - 3, -1, -1):
        table3[i] = max(table3[i + 1], table2[i + 1] + arr[i])

    for i in range(len(arr) - 4, -1, -1):
        table4[i] = max(table4[i + 1], table3[i + 1] - arr[i])

    return table4[0]


def main():
    arr = [4, 8, 9, 2, 20]
    ans = max_quad_expression(arr)
    print(ans)


main()
