'''
Given a queue of length n, reverse the queue in groups of k.
You need to it recursively without using any temporary data structure.

Example:
n = 9
queue = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
Output: [3, 2, 1, 6, 5, 4, 9, 8, 7]

SOLUTION:

def reverse_queue_in_batches(queue, k):
  num_iterations = len(queue) // k
  while (num_iterations):
    num_iterations -= 1
    recurse(queue, k)
  recurse(queue, len(queue) % k)


def recurse(queue, k):
  if(k == 0):
    return
  top = queue.pop()
  recurse(queue, k-1)
  queue.push(top)

Just simulate and see how it works.
'''
