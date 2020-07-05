"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.
The length of the given array will be >= 3 and all elements are in the range [-1000, 1000].

Example 1:
Input: [1,2,3]
Output: 6

Example 2:
Input: [1,2,3,4]
Output: 24

SOLUTION:

Note that this is a bit tricky due to the presence of negative integers.
We cannot just return the product of max1*max2*max3.
Imagine input = [-6, -5, 1, 2, 3]
Here answer = -6*-5*3

So the final algo is:

case1 = max1*max2*max2
case2 = min1*min2*max1
ans = max(case1, case2)
"""
from heapq import nlargest, nsmallest


def max_product(nums):
    largests = nlargest(3, nums)
    smallests = nsmallest(2, nums)
    min1, min2 = smallests
    max1, max2, max3 = largests
    op1 = min1 * min2 * max1
    op2 = max1 * max2 * max3
    return max(op1, op2)


def main():
    arr = [1, 2, -3, -4]
    ans = max_product(arr)
    print(ans)


if __name__ == "__main__":
    main()
