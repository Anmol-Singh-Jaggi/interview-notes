# The Critical Section Problem

Let this be a process's code:

```
// Private resources
// Shared resources
// Private resources
```

Now the private resources section has no conflict, but we need to handle the shared part.

There can be multiple solutions to the Critical Section problem. However, we need to keep in mind 3 criterias to evaluate a solution:

- **Mutual exclusion**: Only 1 process should have control over shared resources at a time.
- **Progress**: Lets say there are 3 processes in conflict. We can easily give them turns to the shared resources in a round-robin manner. But all the resources might not even want to take those resources. So, it is very inefficient to forcefully handle control to processes which dont even want it. Also, progress means no deadlock.
- **Bounded-Wait**: A process will wait only for a finite amount of time (that is, no starvation!!). This is optional constraint though

# Solution 1: Turn variable

Process 0:

```python
while True:
    while turn != 0:
        pass
    # Critical section
    turn = 1
    # Remainder section
```

Process 1:

```python
while True:
    while turn != 1:
        pass
    # Critical section
    turn = 0
    # Remainder section
```

This satisfies mutual exclusion and bounded-wait but not progress.

# Solution 2: Flag variable

Process 0:

```python
while True:
    flag[0] = True
    while flag[1]:
        pass
    # Critical section
    flag[0] = False
```

Process 1:

```python
while True:
    flag[1] = True
    while flag[0]:
        pass
    # Critical section
    flag[1] = False
```

This satisfies mutual exclusion, but not progress (due to deadlock possibility).  
Imagine if `flag[0]` and `flag[1]` both become true before the internal while. We'll end up in deadlock.

# Solution 3: Peterson

This combines the turn and flag-based approaches.

Process 0:

```python
while True:
    flag[0] = True
    turn = 1
    while turn == 1 and flag[1]:
        pass
    # Critical Section
    flag[0] = False
```

Process 1:

```python
while True:
    flag[1] = True
    turn = 0
    while turn == 0 and flag[0]:
        pass
    # Critical Section
    flag[1] = False
```

This satisfies all the constraints.  
But it suffers from redundant busy-waiting.

# Solution 4: Locking

Process:

```python
sem = Semaphore()
while True:
    wait(sem)
    # Critical section
    signal(sem)
    # Remainder section
```

This satisfies mutual exclusion and progress.  
But bounded wait is dependent on the lock implementation.  
If locks are implemented as FIFO-based, then it satisfies bounded-wait also.

