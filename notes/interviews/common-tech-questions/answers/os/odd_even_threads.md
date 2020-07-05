```python
sem_odd = Semaphore(1)
sem_even = Semaphore(0)

def thread_odd():
    i = 1
    while True:
        wait(sem_odd)
        print(i)
        i += 2
        signal(sem_even)

def thread_even():
    i = 2
    while True:
        wait(sem_even)
        print(i)
        i += 2
        signal(sem_odd)
```

**SOLUTION 2:**


```python
lock = ReentrantLock()
turn_changed = lock.newCondition()
turn = False

def thread_odd():
    i = 1
    while True:
        lock.acquire()
        while turn:
            turn_changed.wait() 
        print(i)
        i += 2
        turn = not turn
        turn_changed.signal()
        lock.release()

def thread_even():
    i = 2
    while True:
        lock.acquire()
        while not turn:
            turn_changed.wait() 
        print(i)
        i += 2
        turn = not turn
        turn_changed.signal()
        lock.release()
```