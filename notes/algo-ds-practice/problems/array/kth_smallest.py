'''
**Solution 1:**

1. Max-heapify the first k elements.
2. For every index i > k, heap.pushpop(n[i]).
3. At the end, we will have a max-heap containing the k smallest elements.
O(k + (n-k)logk)


**Solution 2:**
1. Min-heapify the whole array in O(n).
2. Call heap.pop() k times.
O(n + klogk)

**Solution 3:**
1. Call the quicksort partition() on array (either on the first or the last element).
2. If the pivot position == k, then return it straightaway.
3. Else, recur for left or right array accordingly.
O(n*n) worst case but O(n) average.

**Solution 4:**
1. Same as solution 3 but use randomized pivot selection.
Expected O(n).

**Solution 5:**
1. Same as solution 4 but use median-of-median to get the median as the pivot.
Guaranteed O(n)
'''
