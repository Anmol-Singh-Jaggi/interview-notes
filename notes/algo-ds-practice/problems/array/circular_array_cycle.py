'''
You are given a circular array nums of positive and negative integers.
If a number k at an index is positive, then move forward k steps.
Conversely, if it's negative (-k), move backward k steps.
Since the array is circular, you may assume that the last element's next element is the first element, and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in nums.
A cycle must start and end at the same index and the cycle's length > 1.
Furthermore, movements in a cycle must all follow a single direction. In other words, a cycle must not consist of both forward and backward movements.

Example 1:

Input: [2,-1,1,2,2]
Output: true
Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.

Example 2:

Input: [-1,2]
Output: false
Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because the cycle's length is 1. By definition the cycle's length must be greater than 1.

Example 3:

Input: [-2,1,-1,-2,-2]
Output: false
Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle, because movement from index 1 -> 2 is a forward movement, but movement from index 2 -> 1 is a backward movement. All movements in a cycle must follow a single direction.

SOLUTION:

Lets first think how to detect cycles only in the forward direction.
We can start traversing from index 0.
We will maintain a visited set during a traversal.
If we encounter an index which is already visited before in this traversal, then cycle exits.
On the other hand, if we encounter a -ve element, the cycle cannot exist in this traversal.
If the current traversal is not cyclic, then at the end of the traversal, we can mark all the elements of this traversal as 'safe'.
This is the basic idea.
See the code for detail.
Also, for the other direction, we just reverse the array and reverse the sign of the elements and re-run the exact same algo on that.

For O(1) solution, we can detect cycle using slow and fast pointer, and for marking 'safe' indices, we can use some dummy -ve value.
But its not that simple; we need to distinguish between 'safe' indices and 'visited' (in current run) indices.
For that we can use 2 dummy values; We can first modify every arr[i] to arr[i]%n; it will not affect the final result.
Then we can use the dummy value 'n' for round 1, '2n' for round 2  and so on...


VARIATION:
What if forward and backward steps are allowed in one cycle?
Then we can just model the array as a directed graph and find cycle in that.
'''
def is_cycle(arr, start, safe):
    i = start
    visited = set()
    visited.add(i)
    while True:
        i = (i + arr[i]) % len(arr)
        if i in safe:
            break
        if i in visited:
            if len(visited) == 1:
                # We cannot mark it as safe yet.
                # What if some other vertex redirects to here?
                return False
            return True
        visited.add(i)
    for i in visited:
        safe.add(i)
    return False


def is_cyclic(arr):
    i = 0
    start = 0
    safe = set()
    for i in range(len(arr)):
        if arr[i] <= 0:
            safe.add(i)
    while start < len(arr):
        if start in safe:
            start += 1
            continue
        if is_cycle(arr, start, safe):
            return True
    return False


def is_cyclic_outer(arr):
    arr_copy = list(arr)
    if is_cyclic(arr):
        return True
    arr = arr_copy
    arr.reverse()
    for i in range(len(arr)):
        arr[i] = -arr[i]
    return is_cyclic(arr)


def main():
    arr = [2, -1, 1, 2, 2]
    arr = [-1, 2]
    arr = [-2, 1, -1, -2, -2]
    arr = [1, 2]
    ans = is_cyclic_outer(arr)
    print(ans)


main()
