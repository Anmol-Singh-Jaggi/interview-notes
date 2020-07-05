'''
Given an array A of size N having distinct elements, the task is to
find the next greater element for each element of the array in order
of their appearance in the array.
If no such element exists, output -1.

Example:
Input
2
4
1 3 2 4
4
4 3 2 1
Output
3 4 4 -1
-1 -1 -1 -1
'''


def next_larger(arr):
    stack = []
    ans = [-1] * len(arr)
    stack = [arr[-1]]
    for i in range(len(arr) - 2, -1, -1):
        while stack:
            stack_top = stack.pop()
            if stack_top > arr[i]:
                ans[i] = stack_top
                stack.append(stack_top)
                break
        stack.append(arr[i])
    return ans


def main():
    t = int(input())
    while t:
        t -= 1
        input()
        arr = [int(x) for x in input().split()]
        ans = next_larger(arr)
        print(' '.join(ans))


main()
