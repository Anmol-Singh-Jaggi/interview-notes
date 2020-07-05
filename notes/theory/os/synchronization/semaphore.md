# Semaphores

- A useful way to think of a semaphore as used in the real-world system is as a record of how many units of a particular resource are available, coupled with operations to adjust that record safely (i.e. to avoid race conditions) as units are required or become free, and, if necessary, wait until a unit of the resource becomes available.
- Semaphores are a useful tool in the prevention of race conditions; however, their use is by no means a guarantee that a program is free from these problems.  
- Semaphores which allow an arbitrary resource count are called **counting semaphores**, while semaphores which are restricted to the values 0 and 1 (or locked/unlocked, unavailable/available) are called **binary semaphores** and are used to implement locks. 
- To avoid starvation, a semaphore has an associated queue of processes (usually with FIFO semantics).
- If a process performs a P(Procure) operation on a semaphore that has the value zero, the process is added to the semaphore's queue and its execution is suspended.
- When another process increments the semaphore by performing a V(Vacate) operation, and there are processes on the queue, one of them is removed from the queue and resumes execution.
- When processes have different priorities the queue may be ordered by priority, so that the highest priority process is taken from the queue first.

```python
def wait(sem):
    sem -= 1
    if sem < 0:
        # Atomically, add process to queue and go to sleep
        sem.queue.add(this.thread)
        sleep()

def signal(sem):
    sem += 1
    if sem <= 0:
        # remove process from queue
        sem.wakeup()
```

## Semaphore uses:

### 1. Critical Section problem.
As seen in the critical section file.

### 2. Process execution ordering.
Sometimes we want the processes to access the shared resource in a specific order.  
For example, we want P2 -> P1 -> P3.  
We'll use 2 semaphores - `S1 = 0` and `S2 = 0`.

Logic for P2:

```
Critical Section
signal(s1)
```

Logic for P1:

```
wait(s1)
Critical Section
signal(s2)
```

Logic for P3:

```
wait(s2)
Critical Section
```

### 3. Managing multi-instance resource shared access.

- Lets say a printer can serve 5 processes at a time.
- We just need a very simple change to the original semaphore logic to achieve this.
- Instead of initializing the semaphore to 1, we'll initialize it to 5.


# Mutex

- A mutex is basically a binary semaphore that has a concept of ownership.
- A mutex can be unlocked only by the same thread that locked it.
- Which means that a semaphore can be (irresponsibly) used for things other than mutual exclusion.
- For example, with semaphores, I can signal from one thread so that the other can do something.
- Also, we cannot do process ordering using mutexes.


## Disadvantages of binary semaphores over mutexes:
- **Accidental Release**: A thread mistakenly releases a lock without acquiring it first. May cause incorrect results.
- **Recursive deadlock**: A recursive deadlock occurs when the lock is being acquired in a recursive function.
  ```python

  def foo(num):
    if num == 0:
      return
    wait(sem)
    foo(num-1)
    signal(sem)

  foo(5)
  ```
  If we use mutex, we can determine if the lock is being requested again by the same thead, so that we let it re-acquire as an exception.

- **Deadlock by process death**: If the process holding the semaphore gets killed, we'll end up in a deadlock. However, if have ownership info, the OS can do clean all the mutexes held post kill.
- **Priority inversion**: Consider 3 processes of priority 1, 2, 3. Lets say 1 and 3 share a critical section. Lets say 1 acquires it first. 3 is waiting for it.. But then 2 enters and preempt out 1 since it does not share critical section. Now 3 is blocked due to 2. What if many processes like 2 come again?? For more details, see the priority inversion file.
- **Semaphore signalling**: We can implement some sort of asynchronous signalling system between multiple threads (remember process ordering using semaphores). Although, this is not a disadvantage as such, but many people misuse it, as semaphores were designed for mutual exclusion. We have better ways to implement signalling.

------

- So, mutexes addresses the above mentioned 5 shortcomings of semaphores.  
- However, it does not prevent circular deadlock (the standard classical 'A waits for B; B waits for A' deadlock).
- We should use mutex for mutual exclusion and semaphores for signalling (producer-consumer etc.). 