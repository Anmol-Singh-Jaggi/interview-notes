"""
Given an integer array, find 4 numbers whose product is maximum and output the maximum product.
The length of the given array will be >= 4 and all elements are in the range [-1000, 1000].

Example 1:

Input: [1,2,3,4]
Output: 24

SOLUTION:

Note that this is a bit tricky due to the presence of negative integers.
We cannot just return the product of max1*max2*max3*max4.
Imagine input = [-6, -5, -4, 0, 1, 2, 3, 4]
Here answer = -6*-5*4*3

So the final algo is:

case1 = max1*max2*max3*max4
case2 = min1*min2*min3*min4
case3 = max1*max2*min1*min2
ans = max(case1, case2, case3)
"""
from heapq import nlargest, nsmallest


def max_product(nums):
    largests = nlargest(4, nums)
    smallests = nsmallest(4, nums)
    min1, min2, min3, min4 = smallests
    max1, max2, max3, max4 = largests
    case1 = max1 * max2 * max3 * max4
    case2 = min1 * min2 * min3 * min4
    case3 = max1 * max2 * min1 * min2
    return max(case1, case2, case3)


def main():
    arr = [-6, -5, -4, 0, 1, 2, 3, 4]
    ans = max_product(arr)
    print(ans)


if __name__ == "__main__":
    main()
