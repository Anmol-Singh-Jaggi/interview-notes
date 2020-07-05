"""
Search for needle in an array which is almost sorted.
Meaning that after sorting some elements are moved to either of the adjacent positions, i.e., arr[i] may be present at arr[i+1] or arr[i-1].

For example consider the array {2, 3, 10, 4, 40}.
4 is moved to next position and 10 is moved to previous position.

Example :

Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 40
Output: 2
Output is index of 40 in given array.

Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 90
Output: -1
-1 is returned to indicate element is not present.

SOLUTION:
We can do a modified binary search.
The idea is to compare the key with middle 3 elements, if present then return the index.
If not present, then compare the key with middle element to decide whether to go in left half or right half.
Comparing with middle element is enough as all the elements after
mid+2 must be greater than element mid and all elements before
mid-2 must be smaller than mid element.
"""


def search_almost_sorted(items, needle):
    # CAREFUL: Tricky implementation!
    start_index = 0
    end_index = len(items) - 1
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        if items[mid_index] == needle:
            return mid_index
        if mid_index - 1 >= 0 and items[mid_index - 1] == needle:
            return mid_index - 1
        if mid_index + 1 < len(items) and items[mid_index + 1] == needle:
            return mid_index + 1
        if items[mid_index] < needle:
            start_index = mid_index + 2
        else:
            end_index = mid_index - 2
    return -1


def main():
    arr = [10, 3, 40, 20, 50, 80, 70]
    needle = 40
    ans = search_almost_sorted(arr, needle)
    print(ans)


main()
