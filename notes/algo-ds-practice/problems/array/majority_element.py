"""
Write a function which takes an array and prints the majority element (if it exists), otherwise prints “No Majority Element”.
A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element).

Examples :
Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
Output : 4

Input : {3, 3, 4, 2, 4, 4, 2, 4}
Output : No Majority Element

SOLUTION:
We can ofcourse do it using hashmaps, but that requires O(n) space.
Alternatively, we can use Moore's voting algo:

1. The first step gives the element that may be majority element in the array.
If there is a majority element in an array, then this step will definitely return majority element, otherwise it will return candidate for majority element.
2. Check if the element obtained from above step is majority element
This step is necessary as we are not always sure that element return by first step is majority element.

"""


def find_majority_element(arr):
    candidate_index = 0
    count = 1
    for i in range(1, len(arr)):
        if count == 0:
            candidate_index = i
            count = 1
            continue
        if arr[i] == arr[candidate_index]:
            count += 1
        else:
            count -= 1
    print(candidate_index)
    if arr.count(arr[candidate_index]) > len(arr) // 2:
        return candidate_index
    return None


def main():
    arr = [1, 2, 4, 4, 5, 4, 4]
    arr = [2, 2, 1, 1, 1, 2, 2]
    maj_index = find_majority_element(arr)
    if maj_index is None:
        print(None)
    else:
        print(arr[maj_index])


main()
