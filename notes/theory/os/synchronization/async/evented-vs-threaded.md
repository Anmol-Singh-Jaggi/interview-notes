# Evented vs Threaded architecture
- https://www.kislayverma.com/post/event-based-asynchronous-programming (**Fantastic article series**)
- https://en.wikipedia.org/wiki/Thread_pool


## Why is Node server single-threaded yet capable of handling multiple concurrent connections?
- Because it assumes that most of the time is spent in IO for a request.
- It actually is not single-threaded per-se.
- The main event loop is single threaded.
- However, it has multiple 'worker threads' which have the responsiblity of handling all the long-running tasks.
- Hence, rather than creating 10k threads for 10k requests and letting them wait idly for the IO to finish, its better to offload them to the worker thread pool.
- Once a callback starts executing, it will keep executing until it finishes; no time slicing!
- The node model is often called as the *reactor* pattern, as opposed to the *actor* pattern (akka).
- References:
  - https://stackoverflow.com/a/6782438/1925388
  - https://stackoverflow.com/a/8685968/1925388 (Node on multi-core machines)
  - https://stackoverflow.com/a/25280366/1925388 (Evented vs threaded)
  - https://stackoverflow.com/questions/17959663/why-is-node-js-single-threaded/
  - https://stackoverflow.com/a/14797071/1925388
  - https://stackoverflow.com/a/48242227/1925388
  - https://stackoverflow.com/questions/22644328/when-is-the-thread-pool-used/
  - https://kariera.future-processing.pl/blog/on-problems-with-threads-in-node-js/
  - https://stackoverflow.com/a/12332546/1925388
  - https://nodejs.org/uk/docs/guides/dont-block-the-event-loop/ (**Fantastic article!**)
  - https://nodejs.org/uk/docs/guides/event-loop-timers-and-nexttick


## Can disk handle parallel IO?
- Yes for SSD:
  - https://engineering.linkedin.com/blog/2016/05/designing-ssd-friendly-applications-for-better-application-perfo.
- No for HDD:
  - https://superuser.com/questions/365875/can-hard-disks-read-and-write-simultaneously-on-different-tracks-how/
  - quora.com/How-does-an-HDD-deal-with-multiple-simultaneous-read-write-requests
  - https://stackoverflow.com/questions/1993699/how-to-parallelize-file-reading-and-writing/


## What's the optimal size for threadpool?
- For completely CPU intesive tasks, thread pool size should never be more than the number of physical cores.
- Practically speaking, its generally considered optimal to allocate 1-2x the number of cores.

## What's the advantage of a threadpool?
- If we allocate 1 thread per request, it will waste a lot of time and memory. Also, its very hard on the OS to maintain so many threads. The OS scheduler algo becomes slow.
- Basically, it is always better to reuse an idle thread rather than to destroy it and create a new one.
- The concept of threadpool has got nothing to do with threaded vs event-driven architecture.
- Its just another application of the very common object-pooling design pattern.
- Even in 'threaded' one-thread-per-request architecture, we must have a max number of parallel threads.

## Why to use asynchronous programming?
- Because writing regular multithreaded code is hard; reading and debugging is even harder (locks, deadlocks, race conditions etc).

## Akka vs Java concurrency
- Akka is an abstraction over java concurrency primitives.
- Its an actor/message based programming model rather than a future/promise based one.

## If parallel filesystem IO is not possible at the hardware level, what's the point of doing parallel downloads from a server?
- https://serverfault.com/q/1015170/339626
