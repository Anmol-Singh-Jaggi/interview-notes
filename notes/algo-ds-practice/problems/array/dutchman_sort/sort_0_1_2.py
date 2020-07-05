"""
Sort a list of 0's, 1's and 2's just in one iteration (not 2!)

SOLUTION:

Let's use here three pointers to track the rightmost boundary of zeros, the leftmost boundary of twos and the current element under the consideration.
p0 = Rightmost boundary of zeroes (index just after the last 0).
p2 = Leftmost boundary of 2's (index just before the first 2).
curr = Index of current element.

Algorithm
- p0 = 0. Invariant: nums[idx < p0] = 0.
- p2 = n - 1. Invariant: nums[idx > p2] = 2.
- Initialise the index of current element to consider: curr = 0.
- While curr <= p2 :
  - If nums[curr] = 0 : swap curr and p0 and move both pointers to the right.
  - If nums[curr] = 2 : swap curr and p2 and move pointer p2 to the left.
  - If nums[curr] = 1 : move pointer curr to the right.
"""


def sortColors(nums):
    p0 = curr = 0
    p2 = len(nums) - 1
    # CAREFUL: Tricky implementation!
    while curr <= p2:
        if nums[curr] == 0:
            nums[p0], nums[curr] = nums[curr], nums[p0]
            p0 += 1
            curr += 1
        elif nums[curr] == 2:
            nums[curr], nums[p2] = nums[p2], nums[curr]
            p2 -= 1
        else:
            curr += 1


arr = [0, 1, 2, 0, 1, 1, 1]
sortColors(arr)
print(arr)
