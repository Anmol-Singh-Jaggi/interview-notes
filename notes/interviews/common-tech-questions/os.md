# General
- Print even and odd numbers alternatively using 2 different threads (one thread for odd and other for even).
- Print `1,2,3,1,2,3,1,2,3....` using 3 threads where Thread Ti prints 'i' in an infinite pool.
- How to avoid deadlocks?
- How to detect deadlocks? - `jstack <pid> > out.txt` will clearly mention deadlocks (This is called a thread dump).
   Another way: Java provides an API for this - `long[] threadIds = ManagementFactory.getThreadMXBean().findDeadlockedThreads()`.
- Implement blocking queue.
- Implement concurrent hash map.

# Java specific
- Coroutines/Fibres?
- <https://stackoverflow.com/q/58154466/1925388>.
- Fail-safe vs Fail-fast iterators.
- Callable vs Runnable.
- Load-balanced web requests using concurrency.
- Timeout a thread after 20 seconds.
- How to wait before 3 threads have completed their tasks?
- How to run tasks asynchronously?
- ThreadPoolExecutor vs ScheduledThreadPoolExecutor vs ForkJoinPool
- Ideal thread size for CPU vs IO tasks??
- `ExecutorService.submit()` vs `ExecutorService.execute()`??
- `Executors` vs `ExecutorService`??
- `ConcurrentHashMap` implementation - **Striped locks** ??
- https://stackoverflow.com/questions/817856/when-and-how-should-i-use-a-threadlocal-variable?rq=1
- https://www.baeldung.com/java-fork-join
- `CountDownLatch` use??
- Daemon thread?
- `service.shutdown()` -> Will schedule shutdown -> Not immediately -> Will call `thread.interrupt()` internally -> Thread might not have the code to process it!
- `SynchronousQueue` -> Same as a `BlockingQueue` of size 1 (almost; put() operation is slightly different).
- Runnable vs Callable.
- FixedThreadPool vs CachedThreadPool vs ScheduledThreadPool vs WorkStealingPool vs ForkJoinPool?? - See `java.util.concurrent.Executors` class once.
- In what scenarios should we use ForkJoinPool??
- CountDownLatch vs CyclicBarrier?? -> A CountDownLatch is a one-shot phenomenon -- the count cannot be reset. If you need a version that resets the count, consider using a CyclicBarrier.