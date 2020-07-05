'''
You have a list of unique integers `arr`.
You have to insert these integers into a BST in that order.
You have to return another list `height` such that `height[i]` is the height of arr[i] in the BST.

Example:
arr = [10, 5, 2, 7, 15]
heights = [1, 2, 3, 3, 2]

SOLUTION:

We can just insert into a BST and then tell height.
But it will take O(n*n) in the case of a degenerate BST.
We can instead do the following:
For every arr[i]:
1. If `arr[i] > max(arr[0...i-1])`, then `height[arr[i]] = height[max] + 1`; `arr[i]` will be the child of `max`.
2. If `arr[i] < min(arr[0...i-1])`, then `height[arr[i]] = height[min] + 1`; `arr[i]` will be the child of `min`.
3. Compute `ub = upper_bound(arr[0..i-1], arr[i])`.
   This will return the index of the smallest element which is greater than `arr[i]`.
4. Assign `greater = arr[ub]` and `smaller = arr[ub-1]`, denoting the elements that are closest to `arr[i]`.
5. If `idx[greater] > idx[smaller]`, then `height[arr[i]] = height[greater] + 1`. `arr[i]` is child of `greater`.
   Else, `height[arr[i]] = height[smaller] + 1`; `arr[i]` is child of `smaller`.
   Where `idx[elem]` means index of `elem` in `arr`.
Complexity -> O(nlogn).
Draw some examples to see why case 3 works.

Note: We'll need to have a 'sorted-set' like data structure to do the `upper_bound()`.
Which means that we'll have to use C++ or Java :(
'''
