"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

"""


def move_zeroes(arr):
    left = 0
    right = 0
    while right < len(arr):
        if arr[right] != 0:
            if right != left:
                arr[left] = arr[right]
                arr[right] = 0
            left += 1
        right += 1


def main():
    arr = [0, 1, 0, 3, 12]
    arr = [1, 1, 0, 3, 12]
    move_zeroes(arr)
    print(arr)


main()
