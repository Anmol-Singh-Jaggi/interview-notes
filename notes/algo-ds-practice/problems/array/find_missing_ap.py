"""
Given an array that represents elements of arithmetic progression in order.
One element is missing in the progression, find the missing number.
Examples:

Input: arr[]  = {2, 4, 8, 10, 12, 14}
Output: 6

Input: arr[]  = {1, 6, 11, 16, 21, 31};
Output: 26

SOLUTION 1:
First we need to find the common difference 'diff'.
We can do it in 2 ways:
Consider the first 2 pairs (arr[0], arr[1]) and (arr[1], arr[2]).
diff = min(diff1, diff2)
where diff1 = arr[1] - arr[0]
diff2 = arr[2] - arr[1]

Second way is just calculating (arr[n-1] - arr[0] // n)

Now we can just iterate over the array and find the missing number.

Solution 2:

We can do binary search.
The idea is to go to the middle element.
Check if the difference between middle and next to middle is equal to diff or not, if not then the missing element lies between mid and mid+1.
If the middle element is equal to n/2th term in Arithmetic Series, then missing element lies in right half.
Else element lies in left half.

Note that the same concept can be applied to Geometric progression or even Fibonacci series.
"""


def find_missing_binary_search(arr, low, high, diff):
    mid = (low + high) // 2
    if arr[mid + 1] - arr[mid] != diff:
        return arr[mid] + diff
    if mid > 0 and arr[mid] - arr[mid - 1] != diff:
        return arr[mid - 1] + diff
    if arr[mid] == arr[0] + mid * diff:
        return find_missing_binary_search(arr, mid + 1, high, diff)
    return find_missing_binary_search(arr, low, mid - 1, diff)


def find_missing(arr):
    diff = (arr[len(arr) - 1] - arr[0]) // len(arr)
    return find_missing_binary_search(arr, 0, len(arr) - 1, diff)


def main():
    arr = [2, 4, 8, 10, 12, 14]
    ans = find_missing(arr)
    print(ans)


main()
