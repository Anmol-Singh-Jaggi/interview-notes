"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

SOLUTION:

This is very similar to the "max cumulative sum subarray" problem.
Here you keep 2 values: the max cumulative product UP TO current element starting from SOMEWHERE in the past, and the minimum cumuliative product UP TO current element.
It would be easier to see the DP structure if we store these 2 values for each index, like maxProduct[i], minProduct[i] .

Pseudocode:

def maxProduct(arr):
    # store the result that is the max we have found so far
    ans = A[0]
    max_ending_here = ans
    min_ending_here = ans
    for i in range(1, len(arr)):
        # multiplied by a negative makes big number smaller, small number bigger
        # so we redefine the extremums by swapping them
        if arr[i] < 0:
            swap(max_ending_here, min_ending_here)

        # max/min product for the current number is either the current number itself
        # or the max/min by the previous number times the current one
        max_ending_here = max(A[i], max_ending_here * A[i])
        min_ending_here = min(A[i], min_ending_here * A[i])

        # the newly computed max value is a candidate for our global result
        ans = max(ans, max_ending_here);
    return ans

At each new element, we could either add the new element to the existing product, or start fresh the product from current index (wipe out previous results), hence the 2 `max()` lines.

if we see a negative number, the "candidate" for max should instead become the previous min product, because a bigger number multiplied by negative becomes smaller, hence the `swap()`.


ALTERNATE WAY:

Swapping adds some cognitive complexity, instead just take all three as candidates for each comparison, i.e. (python):

candidates = (arr[i], max_ending_here * arr[i], min_ending_here * arr[i])
max_ending_here = max(candidates)
min_ending_here = min(candidates)

"""


def max_product_subarray(arr):
    if not arr:
        return 0
    max_ending_here, min_ending_here = arr[0], arr[0]
    ans = arr[0]
    for i in range(1, len(arr)):
        candidates = (arr[i], max_ending_here * arr[i], min_ending_here * arr[i])
        max_ending_here = max(candidates)
        min_ending_here = min(candidates)
        ans = max(max_ending_here, ans)
    return ans


def main():
    arr = [-2, 0, -1]
    ans = max_product_subarray(arr)
    print(ans)


main()
