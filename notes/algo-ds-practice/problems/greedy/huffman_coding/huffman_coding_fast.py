'''
Time complexity of the algorithm discussed in above post is O(nLogn).
If we know that the given array is sorted (by non-decreasing order of frequency), we can generate Huffman codes in O(n) time. Following is a O(n) algorithm for sorted input.

1. Create two empty queues.
2. Create a leaf node for each unique character and enqueue it to the first queue in non-decreasing order of frequency.
Initially second queue is empty.
3. Dequeue two nodes with the minimum frequency by examining the front of both queues.
Repeat following steps two times:
 a) If second queue is empty, dequeue from first queue.
 b) If first queue is empty, dequeue from second queue.
 c) Else, compare the front of two queues and dequeue the minimum.
4. Create a new internal node with frequency equal to the sum of the two nodes frequencies.
5. Make the first dequeued node as its left child and the second dequeued node as right child.
5. Enqueue this node to second queue.
6. Repeat steps 3,4,5 until there is more than one node in the queues.
7. The remaining node is the root node and the tree is complete.

Note that 2 queues will always be in sorted order.
'''
