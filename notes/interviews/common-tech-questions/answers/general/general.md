## Why not ternary or quaternary search instead of binary search?
- Because number of operations in binary search = log<sub>2</sub>n.
- For ternary search, it is = 2*log<sub>3</sub>n = (2 / log<sub>2</sub>3) * log<sub>2</sub>n = 1.26 * log<sub>2</sub>n.
- The factor of 2 is due to the fact at each step we have to compare `val` with 2 numbers - `pivot1` (at index 1/3) and `pivot2` (at index 2/3).

## Java vs Python
- Java is faster due to being a compiled language and also because of **Just-In-Time** compilation.
- Java has true multithreading, whereas Python does not due to **Global Interpreter Lock**.
  In Python, we can have multiple threads but they will always run on a single core.
  So its ok for IO-heavy tasks, but not for CPU-heavy.
- But still some web servers are there in Python as instead of multithreading people do multiprocessing.
- They basically pre-create multiple processes ready for use in case a request comes.
- Also Python does not have compile-time errors and warnings which can be risky in a web server.
- Java is older, so more mature also.

## Merge vs Quick sort
- Merge sort requires O(n) extra space.

## Online vs Offline algorithm

### Online algorithm
- Can process its input piece-by-piece in a serial fashion, without having the entire input available from the start.  
- Examples:
  - Insertion sort
  - Median of a stream of integers.
  - Kadane's algorithm.
  - Linear search.
  - Frequency counting.

### Offline algorithm 
- Requires the whole problem data from the beginning.
- Examples:
  - Selection sort.