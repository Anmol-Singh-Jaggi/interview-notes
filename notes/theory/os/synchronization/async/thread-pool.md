# Thread Pools

Thread pools on the JVM should usually be divided into the following categories:

1. CPU-bound
2. Blocking IO
3. Non-blocking IO polling

Each of these categories has a different optimal configuration and usage pattern.

For CPU-bound tasks, you want a *bounded* thread pool which is pre-allocated and fixed to exactly the number of CPUs.  The only work you will be doing on this pool will be CPU-bound computation, and so there is no sense in exceeding the number of CPUs unless you happen to have a really particular workflow that is amenable to hyperthreading (in which case you could go with double the  number of CPUs).  Note that the old wisdom of "number of CPUs + 1" comes from mixed-mode thread pools where CPU-bound and IO-bound tasks were merged.  We won't be doing that.

The problem with a fixed thread pool is that any blocking IO operation (well, any blocking operation *at all*) will eat a thread, which is an extremely finite resource.  Thus, we want to avoid blocking at all costs on the CPU-bound pool.  Unfortunately, this isn't always possible (e.g. when being forced to use a blocking IO library).  When this is the case, you should always push your blocking operations (IO or otherwise) over to a separate thread pool.  This separate thread pool should be caching and *unbounded* with no pre-allocated size.  To be clear, this is a *very* dangerous type of thread pool.  It isn't going to prevent you from just allocating more and more threads as the others block, which is a very dangerous state of affairs.  You need to make sure that any data flow which results in running actions on this pool is *externally* bounded, meaning that you have semantically higher-level checks in place to ensure that only a fixed number of blocking actions may be outstanding at any point in time (this is often done with a non-blocking bounded queue).  
To reiterate, the basic reason why we are having a separate pool for IO is because we dont want the CPU to be underutilized.  
While IO is being done, atleast the CPU bound task can happen in the CPU thread pool.  
To understand the severity if the problem, imagine a system with just 1 process running with 4 threads. Imagine that all 4 threads are busy in IO and a new task comes up. Now that task is totally stuck until all threads are finished. Meanwhile CPU is sitting totally idle!

The final category of useful threads (assuming you're not a Swing/SWT application) is asynchronous IO polls.  These threads basically just sit there asking the kernel whether or not there is a new outstanding async IO notification, and forward that notification on to the rest of the application.  You want to handle this with a very small number of fixed, pre-allocated threads.  Many applications handle this task with just a single thread!  These threads should be given the maximum priority, since the application latency will be bounded around their scheduling.  You need to be careful though to *never* do any work whatsoever on this thread pool!  Never ever ever.  The moment you receive an async notification, you should be *immediately* shifting back to the CPU pool.  Every nanosecond you spend on the async IO thread(s) is added latency on your application.  For this reason, some applications may find slightly better performance by making their async IO pool 2 or 4 threads in size, rather than the conventional 1.

## Global Thread Pools

I've seen a lot of advice floating around about not using global thread pools, such as `scala.concurrent.ExecutionContext.global`.  This advice is rooted in the fact that global thread pools can be accessed by arbitrary code (often library code) and you cannot (easily) ensure that this code is using the thread pool appropriately.  How much of a concern this is for you depends a lot on your classpath.  Global thread pools are pretty darn convenient, but by the same token, it also isn't all that hard to have your own application-internal global pools.  So… it doesn't hurt.

On that note, view with *extreme* suspicion any framework or library which either a) makes it difficult to configure the thread pool, or b) just straight-up defaults to a pool that you cannot control.

Either way, you're almost always going to have some sort of singleton object somewhere in your application which just has these three pools, pre-configured for use.  If you ascribe to the "implicit `ExecutionContext` pattern", then you should make the CPU pool the implicit one, while the others must be explicitly selected.