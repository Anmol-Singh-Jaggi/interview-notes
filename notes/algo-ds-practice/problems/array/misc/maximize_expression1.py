"""
Given an array of n integers, and three integers x, y and z,
maximise the value of (x * a[i]) + (y * a[j]) + (z * a[k])
where i ≤ j ≤ k.

Examples :

Input : arr[] = {-1, -2, -3, -4, -5}
         x = 1
         y = 2
         z = -3
Output: 12
Explanation: The maximized values is
(1 * -1) + (2 * -1) + ( -3 * -5) = 12

Input: arr[] = {1, 2, 3, 4, 5}
       x = 1
       y = 2
       z = 3
Output: 30
(1*5 + 2*5 + 3*5) = 30

SOLUTION:

For every index i, compute left_max[i] such that left_max[i] = max value of (x * arr[j]) for j = 0 to i-1
For every index i, compute right_max[i] such that right_max[i] = max value of (z * arr[j]) for j = i+1 to n-1
Then, for every index, compute the expression and take max of that as the answer.
Expression = left_max[i] + arr[i] * y + right_max[i]
Complexity -> O(n)
"""


from math import inf


def maximize_triplet_expression(arr, x, y, z):
    # Traverse the whole array and compute left maximum for every index.
    left_max = [0] * len(arr)
    left_max[0] = x * arr[0]
    for i in range(1, len(arr)):
        left_max[i] = max(left_max[i - 1], x * arr[i])

    # Compute right maximum for every index.
    right_max = [0] * len(arr)
    right_max[len(arr) - 1] = z * arr[len(arr) - 1]
    for i in range(len(arr) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], z * arr[i])

    # Traverse through the whole array to maximize the required expression.
    ans = -inf
    for i in range(0, len(arr)):
        ans = max(ans, left_max[i] + y * arr[i] + right_max[i])
    return ans


def main():
    arr = [-1, -2, -3, -4, -5]
    x = 1
    y = 2
    z = -3
    ans = maximize_triplet_expression(arr, x, y, z)
    print(ans)


main()
