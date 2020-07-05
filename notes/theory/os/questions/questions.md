- **Paging**: Fixed-size non contiguous memory allocation to achieve multitasking.
- **Segmentation**: Variable-size non contiguous memory allocation. One function is kept in one segment.
- Paging and segmentation can be combined.
- **Memory allocation policies:** Best-fit, Worst-fit, First-Fit
- Virtual memory vs paging.
- Inverted page table.
- Multiprogramming vs Multitasking vs Multiprocessing
- Parallelism vs concurrency
- How to create a thread?
- How to wait for a thread to complete?
- How to kill a thread?
- How to interrupt a thread?
- Process vs thread? When to use both?
- fork()
- Deadlock:
  - 4 conditions.
  - Resource allocation graph.
- Livelock (Dining philosopher).
- Priority Inversion and remedy??
- Using semaphore to order thread executions.
- Disadvantages of mutex over semaphores?
- Monitors vs semaphore?
- wait/notify/notifyAll
- Condition variables?
- Producer-Consumer:
  - Using semaphores.
  - Using monitors.
  - Blocking queues.
- Readers-Writers problem:
  - Concurrent hash-map.
  - Using semaphores.
  - Using monitors.
  - Using Readers-Writers lock.
  - Implement readers-writer lock.
- Dining philosopher.
- Implement a semaphore?
- Why is `object.wait()` public?
- `synchronized/wait/notify` vs `ReentrantLock` and condition variables.
- Why methods like `wait()`, `notify()` and `notifyAll()` are present in object class and not in Thread class?
- `notifyAll()` vs `notify()`

-----

- https://www.careercup.com/question?id=5082791237648384
- https://www.careercup.com/page?pid=threads-interview-questions
- https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/doc-files/threadPrimitiveDeprecation.html
https://www.javatpoint.com/java-multithreading-interview-questions
https://javarevisited.blogspot.com/2014/07/top-50-java-multithreading-interview-questions-answers.html
https://www.journaldev.com/1162/java-multithreading-concurrency-interview-questions-answers
https://career.guru99.com/top-40-multithreading-interview-questions-and-answers/
https://www.geeksforgeeks.org/tag/java-multithreading/
https://www.baeldung.com/java-concurrency-interview-questions
- Multithreaded Task Scheduler Service/ Executor Service:
https://www.baeldung.com/java-executor-service-tutorial
https://github.com/FreemanZhang/system-design/blob/master/multiThreading.md