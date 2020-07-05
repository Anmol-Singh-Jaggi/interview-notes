"""
Given an unsorted array of positive integers.
Find the number of triangles that can be formed with three different array elements as three sides of triangles.
For a triangle to be possible from 3 values, the sum of any two values (or sides) must be greater than the third value (or third side).
For example, if the input array is {4, 6, 3, 7}, the output should be 3.
There are three triangles possible {3, 4, 6}, {4, 6, 7} and {3, 6, 7}.
Note that {3, 4, 7} is not a possible triangle.
As another example, consider the array {10, 21, 22, 100, 101, 200, 300}.
There can be 6 possible triangles: {10, 21, 22}, {21, 100, 101}, {22, 100, 101}, {10, 100, 101}, {100, 101, 200} and {101, 200, 300}

SOLUTION:

Sort numbers (ascending order).
We will take triples ai <= aj <= ak, such that i <= j <= k.
For each i, j you need to find largest k that satisfy ak <= ai + aj.
Then all triples (ai,aj,al) j <= l <= k is triangle (because ak >= aj >= ai we can only violate ak < a i+ aj).

Consider two pairs (i, j1) and (i, j2) j1 <= j2.
It's easy to see that k2 (found on step 2 for (i, j2)) >= k1 (found one step 2 for (i, j1)).
It means that if you iterate for j, and you only need to check numbers starting from previous k.

So it gives you O(n) time complexity for each particular i, which implies O(n^2) for whole algorithm.
"""


def num_triangles(arr):
    ans = 0
    arr.sort()
    for i in range(0, len(arr)):
        k = i + 2
        for j in range(i+1, len(arr)):
            while k < len(arr) and arr[i] + arr[j] > arr[k]:
                k += 1
            ans += k - j - 1
    return ans


def main():
    arr = [3, 4, 6, 7]
    arr = [10, 21, 22, 100, 101, 200, 300]
    ans = num_triangles(arr)
    print(ans)


main()
