Initialize 3 semaphores:
- mutex = 1
- empty = n
- occupied = 0

Producer:

```python
while True:
    # produce()
    wait(empty)
    wait(mutex)
    # append()
    signal(mutex)
    signal(occupied)
```

Consumer:

```python
while True:
    wait(occupied)
    wait(mutex)
    # consume()
    signal(mutex)
    signal(empty)
    # use()
```