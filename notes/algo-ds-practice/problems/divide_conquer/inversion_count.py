'''
Inversion Count for an array indicates – how far (or close) the array is from being sorted.
If array is already sorted then inversion count is 0.
If array is sorted in reverse order that inversion count is the maximum.
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

Example:
The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

SOLUTION:

Suppose we know the number of inversions in the left half and right half of the array (let be inv1 and inv2), what kinds of inversions are not accounted for in Inv1 + Inv2?
The answer is – the inversions we have to count during the merge step.
Therefore, to get number of inversions, we need to add number of inversions in left subarray, right subarray and merge().

How to get number of inversions in merge()?
In merge process, let i is used for indexing left sub-array and j for right sub-array.
At any step in merge(), if a[i] is greater than a[j], then there are (mid – i) inversions,
because left and right subarrays are sorted, so all the remaining elements in left-subarray (a[i+1], a[i+2] … a[mid]) will be greater than a[j].

Pseudocode:

merge():

while i <= mid and j <= right:
    if arr[i] <= arr[j]:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
    else:
        # Inversion will occur.
        temp_arr[k] = arr[j]
        inv_count += (mid-i + 1)
        k += 1
        j += 1

mergeSort():

inv_count = mergeSort(arr, temp_arr, left, mid)
inv_count += mergeSort(arr, temp_arr, mid + 1, right)
inv_count += merge(arr, temp_arr, left, mid, right)
return inv_count


ALTERNATE SOLUTION:

Use self balanced BST.
The tree is augmented such that every node also maintains size of subtree rooted with this node.
For each element arr[i], we will try to insert it into the tree.
The insertion operation also updates the inversion count.
The idea is to keep counting greater nodes when tree is traversed from root to a leaf for insertion.
When we insert arr[i], elements from arr[0] to arr[i-1] are already inserted into AVL Tree.
All we need to do is count these nodes.
For insertion into AVL Tree, we traverse tree from root to a leaf by comparing every node with arr[i[].
When arr[i[ is smaller than current node, we increase inversion count by 1 plus the number of nodes in right subtree of current node.
Which is basically count of greater elements on left of arr[i], i.e., inversions.
'''
