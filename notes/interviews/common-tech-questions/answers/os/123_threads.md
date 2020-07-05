```python
sem1 = Semaphore(1)
sem2 = Semaphore(0)
sem3 = Semaphore(0)
sems = [sem1, sem2, sem3]

def thread(idx):
    while True:
        wait(sems[idx])
        print(idx)
        signal(sems[(idx+1)%3])
```