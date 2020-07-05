'''
You are given two arrays, A and B, of equal size N.
The task is to find the minimum value of A[0] * B[0] + A[1] * B[1] +…+ A[N-1] * B[N-1],
where shuffling of elements of arrays A and B is allowed.

Example:
Input:
2
3
3 1 1
6 5 4
5
6 1 9 5 4
3 4 8 2 4
Output:
23
80

Explanation:
For testcase1: 1*6+1*5+3*4 = 6+5+12 = 23 is the minimum sum
For testcase2: 2*9+3*6+4*5+4*4+8*1 =18+18+20+16+8 = 80 is the minimum sum
'''


def minimize_sum(arr1, arr2):
    arr1.sort()
    arr2.sort()
    size = len(arr1)
    ans = 0
    for i in range(size):
        ans += arr1[i] * arr2[size - i - 1]
    return ans
