"""
A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
Expected complexity = O(logn)
"""


def findPeakElement(self, nums):
    if len(nums) == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[len(nums) - 2]:
        return len(nums) - 1
    start = 1
    end = len(nums) - 2
    while end >= start:
        mid = (start + end) // 2
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid] > nums[mid - 1]:
            start = mid + 1
        else:
            end = mid - 1
    return None
