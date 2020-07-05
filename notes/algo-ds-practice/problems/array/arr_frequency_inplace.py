"""
Given an unsorted array of n integers which can contain integers from 1 to n.
Some elements can be repeated multiple times and some other elements can be absent from the array.
Count frequency of all elements that are present and print the missing elements.

Examples:

Input: arr[] = {2, 3, 3, 2, 5}
Output: Below are frequencies of all elements
        1 -> 0
        2 -> 2
        3 -> 2
        4 -> 0
        5 -> 1

Input: arr[] = {4, 4, 4, 4}
Output: Below are frequencies of all elements
        1 -> 0
        2 -> 0
        3 -> 0
        4 -> 4

SOLUTION 1:

The idea is to traverse the given array, use elements as index and store their counts at the index.
For example, when we see element 7, we go to index 6 and store the count.
There are few problems to handle, one is the counts can get mixed with the elements; this is handled by storing the counts as negative.
Other problem is loosing the element which is replaced by count, this is handled by first storing the element to be replaced at current index.

SOLUTION 2:
First decrement every arr[i] by 1 to bring the element range from [0, n-1] from [1, n]
Use every element arr[i] as index and add 'n' to element present at arr[i]%n to keep track of count of occurrences of arr[i]
for (int i=0; i < n; i++):
    arr[arr[i]%n] = arr[arr[i]%n] + n;

This way we are able to keep both the things; the frequency of i as well as the original arr[i] for every i.
"""


def solution1(arr):
    for i in range(0, len(arr)):
        arr[i] -= 1
    print(arr)
    i = 0
    while i < len(arr):
        idx = arr[i]
        if idx < 0:
            pass
        elif arr[idx] < 0:
            arr[idx] -= 1
            arr[i] = 0
        else:
            arr[i] = arr[idx]
            arr[idx] = -1
            i -= 1
        i += 1
    for i in range(0, len(arr)):
        arr[i] = -arr[i]
        print(f'{i+1} -> {arr[i]}')


def solution2(arr):
    for i in range(0, len(arr)):
        arr[i] -= 1
    for i in range(0, len(arr)):
        idx = arr[i] % len(arr)
        arr[idx] += len(arr)
    for i in range(0, len(arr)):
        arr[i] = arr[i] // len(arr)
        print(f'{i+1} -> {arr[i]}')


def main():
    arr = [2, 3, 3, 2, 5]
    solution1(arr)
    arr = [2, 3, 3, 2, 5]
    solution2(arr)


main()
