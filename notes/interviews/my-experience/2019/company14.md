- Given a class `Person` with fields `name` and `id`, implement `compareTo()` method so that we can make a TreeMap out of it.
- While iterating through a list (using `iterator.next()`), is `list.remove()` safe??
- Difference between `list.remove()` vs `Collections.remove(list)`??
- Given a string, reverse it without touching special characters.
- Design Swiggy.
- Design a system which can generate random six-digit string(consisting of a-z and 0-9).
  I told we can generate ever increasing numbers and convert them into base 36.
  Then the problem came down to generating auto incrementing numbers and scaling it (similar to TinyUrl).
- Given a matrix:
1 2 3
4 5 6
7 8 9
use 3 threads to print it such that thread 1 prints 1,4,7. Thread 2 prints 2,5,8 and thread 3 prints 3, 6, 9.
Note that numbers should be printed in the order 1,2,3,4,5,6,7,8,9 only.
Solution - Use 3 semaphores. Keep an integer k and increment it from 0-8. (For every k, compute [i, j] = [k/3, k%3]).
Then print `matrix[i][j]`.
- Why are `wait()`, `notify()` in Object class?
- Write code for LRU Cache.
- One puzzle - Given a cuboidal box (open at the top), it is filled with water. Find a way to empty half of it. You dont have any equipment.