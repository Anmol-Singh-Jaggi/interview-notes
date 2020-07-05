# Monitors
- A monitor simply encapsulates the shared resource and the locking mechanism into a single construct (e.g. a C++ Object that encapsulates the mutex mechanism).
- Access to the shared resource, then, is through a controlled interface which cannot be bypassed (i.e. the application never explicitly calls the mutex, but calls upon access functions).
- A monitor is an object designed to be accessed from multiple threads.
- The member functions or methods of a monitor object will enforce mutual exclusion, so only one thread may be performing any action on the object at a given time.
- If one thread is currently executing a member function of the object then any other thread that tries to call a member function of that object will have to wait until the first has finished.
- A Semaphore is a lower-level object. You might well use a semaphore to implement a monitor.
- So a monitor is basically a wrapper over a binary semaphore.
- Note that another definition of a monitor is 'Mutex + Condition-variables'.

```java
class Account {
  private int balance = 0;
  public boolean withdraw(int amount)
  {
    balance -= amount;
  }
  public method deposit(int amount)
  {
    balance += amount;
  }
}
```

The above code suffers from race conditions.
We can fix it easily using mutex though:


```java
class Account {
  private int balance = 0;
  public synchronized boolean withdraw(int amount)
  {
    balance -= amount;
  }
  public synchronized method deposit(int amount)
  {
    balance += amount;
  }
}
```

Which is equivalent to:

```java
class Account {
  private int balance = 0;
  public boolean withdraw(int amount)
  {
    synchronized(this) {
      balance -= amount;
    }
  }
  public synchronized method deposit(int amount)
  {
    synchronized(this) {
      balance += amount;
    }
  }
}
```

Which is also equivalent to:

```java
class Account {
  private int balance = 0;
  private Mutex mutex = new Mutex();
  public boolean withdraw(int amount)
  {
    mutex.wait()
    balance -= amount;
    mutex.signal();
  }
  public method deposit(int amount)
  {
    mutex.wait();
    balance += amount;
    mutex.signal();
  }
}
```

- Note that we can write `synchronized(obj)` because in Java, each object has an implicit mutex associated to it.
- `public synchronized foo() {...}` is same as `public foo(){ synchronized(this) {...} }`.
- If we write a class in such a way that that mutual exclusion is handled properly, it can be called as a Monitor class.


# Condition variables

- One problem with semaphores is it only lets you wait over a numeric counter, not over a general condition.
- Conditional variables were created to do that.
- Conditional variables (CVs) are always associated with a mutex, they dont exist on their own.
- One mutex can have multiple CVs but one CV cannot be associated with multiple mutexes.
- The combination of Mutex + its CVs can be called as a Monitor.
- Monitors provide a mechanism for threads to temporarily give up exclusive access in order to wait for some condition to be met, before regaining exclusive access and resuming their task.
- For many applications, mutual exclusion is not enough. Threads attempting an operation may need to wait until some condition `P holds true`.
- A busy waiting loop inside the critical section `while not P { continue; }` will not work, as mutual exclusion will prevent any other thread from entering the monitor to make the condition true.
- Other "solutions" exist such as having a loop that unlocks the monitor, waits a certain amount of time, locks the monitor and check for the condition P.
- Theoretically, it works and will not deadlock, but issues arise. It's hard to decide an appropriate amount of waiting time, too small and the thread will hog the CPU, too big and it will be apparently unresponsive.
- What is needed is a way to signal the thread when the condition P is true (or could be true).
- There are three main operations on condition variables - `wait`, `notify`, `notifyAll`.

## Wait()

- `cv.wait(mutex)`: `cv` is a condition variable and `mutex` is a mutex lock associated with the monitor.  
- This operation is called by a thread that needs to wait until some condition is true before proceeding.  
- While the thread is waiting, it does not occupy the monitor.  
- The function, and fundamental contract, of the "wait" operation, is to do the following steps:
```
1. Atomically:
  a. Release the mutex m.
  b. Move this thread from the "running" to cv's "wait-queue" (a.k.a. "sleep-queue") of threads.
  c. Sleep this thread. (Context is synchronously yielded to another thread.)
2. Once this thread is subsequently notified/signalled and resumed, then automatically re-acquire the mutex m.
```
- The atomicity of the operations within step 1 is important to avoid race conditions that would be caused by a preemptive thread switch in-between them.
- One failure mode that could occur if these were not atomic is a ***missed wakeup***, in which the thread could be on cv's sleep-queue and have released the mutex, but a preemptive thread switch occurred before the thread went to sleep, and another thread called a signal/notify operation on cv moving the first thread back out of cv's queue.
- As soon as the first thread in question is switched back to, its program counter will be at step 1c, and it will sleep and be unable to be woken up again, violating the invariant that it should have been on cv's sleep-queue when it slept.
- Other race conditions depend on the ordering of steps 1a and 1b, and depend on where a context switch occurs.

## Notify()

- `cv.notify()/cv.signal()` is called by a thread to indicate that the waiting condition is true.
- Depending on the type and implementation of the monitor, this moves one or more threads from cv's sleep-queue to the "ready queue" for it to be executed.
- It is usually considered a best practice to perform the notify operation before releasing mutex m that is associated with cv. 

## NotifyAll()

- Wakes up all threads in cv's wait-queue. This empties the wait-queue.
- Generally, when more than one predicate condition is associated with the same condition variable, the application will require broadcast instead of signal because a thread waiting for the wrong condition might be woken up and then immediately go back to sleep without waking up a thread waiting for the correct condition that just became true.
- Otherwise, if the predicate condition is one-to-one with the condition variable associated with it, then signal may be more efficient than broadcast.

The proper usage of a monitor, thus, is:

```java
mutex.lock() // Acquire monitor's lock.

while ( !pred ) { // While the condition that we are waiting for is not true
	cv.wait(mutex); // Wait on this monitor's lock and condition variable.
}
// Critical Section
cv2.signal(); // cv2 might be the same as cv or different.

mutex.unlock(); // Release this monitor's lock.
```

- **Note:** the `notify()` and `notifyAll()` methods don't release the lock; this means that the thread or threads awakened will not return from their `wait()` call immediately, but only when the thread that called `notify()` or `notifyAll()` finally relinquishes ownership of the lock. 

## Example 1: Producer-Consumer

The following is the naive solution as it suffers from race conditions:

```java
Queue<?> queue; // A thread-unsafe queue of tasks.

public method producer(){
    while(true){
        task myTask= newTask(); 
        while(queue.isFull()){} // Busy-wait until the queue is non-full.
        queue.enqueue(myTask);
    }
}

public method consumer(){
    while(true){
        while (queue.isEmpty()){} // Busy-wait until the queue is non-empty.
        myTask=queue.dequeue();
        doStuff(myTask);
    }
}
```

We can correct it:

```java
Queue<?> queue;
Mutex queueLock;

public method producer(){
    while(true){
        task myTask= new Task();
        queueLock.acquire(); // Acquire lock for initial busy-wait check.
        while(queue.isFull()){ // Busy-wait until the queue is non-full.
            queueLock.release();
            // Drop the lock temporarily to allow a chance for other threads
            // needing queueLock to run so that a consumer might take a task.
            queueLock.acquire(); // Re-acquire the lock for the next call to "queue.isFull()".
        }
        queue.enqueue(myTask); // Add the task to the queue.
        queueLock.release(); // Drop the queue lock until we need it again to add the next task.
    }
}

public method consumer(){
    while(true){
        queueLock.acquire(); // Acquire lock for initial busy-wait check.
        while (queue.isEmpty()){ // Busy-wait until the queue is non-empty.
            queueLock.release();
            // Drop the lock temporarily to allow a chance for other threads
            // needing queueLock to run so that a producer might add a task.
            queueLock.acquire(); // Re-acquire the lock for the next call to "queue.isEmpty()".
        }
        myTask=queue.dequeue(); // Take a task off of the queue.
        queueLock.release(); // Drop the queue lock until we need it again to take off the next task.
        doStuff(myTask); // Go off and do something with the task.
    }
}
```

The above solution is correct, but suffers from a performance loss due to the busy waiting.  
**Note**: Mutexes themselves can also be spin-locks which involve busy-waiting in order to get the lock, but in order to solve this problem of wasted CPU resources, we assume that queueLock is not a spin-lock and properly uses a blocking lock queue itself.

We can solve the above busy waiting issue by using condition variables:

```java
Queue<?> queue;
Mutex queueLock;

// A condition variable for consumer threads waiting for the queue to become non-empty.
CV queueEmptyCV;
// A condition variable for producer threads waiting for the queue to become non-full
CV queueFullCV;

public method producer(){
    while(true){
        task myTask= new Task();
        queueLock.acquire(); // Acquire lock for initial predicate check.
        while(queue.isFull())
        {
            // Atomically release queueLock, enqueue this thread onto queueFullCV,
            // and sleep this thread.
            queueFullCV.wait(queueLock);
            // Then, "wait" automatically re-acquires "queueLock" for re-checking
            // the predicate condition.
        }
        // Critical section that requires the queue to be non-full.
        // We are holding queueLock.
        queue.enqueue(myTask);
        // Now the queue is guaranteed to be non-empty, so signal a consumer thread
        // or all consumer threads that might be blocked waiting for the queue to be non-empty:
        queueEmptyCV.notify();
        queueLock.release();
    }
}

public method consumer(){
    while(true){
        queueLock.acquire();
        while (queue.isEmpty())
        {
            queueEmptyCV.wait(queueLock);
        }
        myTask=queue.dequeue();
        queueFullCV.notify();
        queueLock.release();
        doStuff(myTask);
    }
}
```

- We can also use just a single condition variable `queueSizeChanged`.
- But then we'll need to use `notifyAll()`.
- This is because the regular signal might wake up a thread of the wrong type whose condition has not yet been met, and that thread would go back to sleep without a thread of the correct type getting signalled.
- For example, a producer might make the queue full and wake up another producer instead of a consumer, and the woken producer would go back to sleep.

```java
Queue<?> queue;
Mutex queueLock;
CV queueSizeChanged;

public method producer(){
    while(true){
        task myTask= new Task();
        queueLock.acquire();
        while(queue.isFull())
        {
            queueSizeChanged.wait(queueLock);
        }
        queue.enqueue(myTask);
        queueSizeChanged.notifyAll();
        queueLock.release();
    }
}

public method consumer(){
    while(true){
        queueLock.acquire();
        while (queue.isEmpty())
        {
            queueSizeChanged.wait(queueLock);
        }
        myTask=queue.dequeue();
        queueSizeChanged.notifyAll();
        queueLock.release();
        doStuff(myTask);
    }
}
```

## Example 2: Pizza

```java
class MyHouse {
  private boolean pizzaArrived = false;

  public synchronized void eatPizza()
  {
    while(!pizzaArrived){
        wait();
    }
  }
  
  public void pizzaGuy()
  {
    this.pizzaArrived = true;
    notifyAll();
  }
}
```

A few important points:

-  **NEVER** do this:
    ```java
    if(!pizzaArrived)
    {
      wait();
    }
    ```
    Always use `while(condition)`, because:
      - Threads can sporadically awake from waiting state without being notified by anyone; **spurious wakeups**. This is due to OS internals.
      - You should check for the condition again after acquiring the synchronized lock. Let's say pizza don't last forever. You awake, line-up for the pizza, but     it's not enough for everybody. If you don't check, you might eat paper! :)

- You must hold the lock (synchronized) before invoking `wait()`/`notify()`. Threads also have to acquire lock before waking.
- Try to avoid acquiring any lock within your synchronized block. If you have to, make sure to take measures to avoid deadlocks.  
- Be careful with `notify()`. Stick with `notifyAll()` until you know what you are doing.
- **It is highly encouraged to not use `wait()/notify()` directly, but to use higher-level concurrency abstractions.**

## Example 3: BlockingQueue

```java
public class BlockingQueue<T>
{
    private Queue<T> queue = new LinkedList<T>();
    private int capacity;
    private Lock lock = new ReentrantLock();
    private Condition notFull = lock.newCondition();
    private Condition notEmpty = lock.newCondition();

    public BlockingQueue(int capacity) {
        this.capacity = capacity;
    }

    public void put(T element) throws InterruptedException {
        lock.lock();
        try {
            while(queue.size() == capacity) {
                notFull.await();
            }
            
            queue.add(element);
            notEmpty.signal();
        } finally {
            lock.unlock();
        }
    }

    public T take() throws InterruptedException {
        lock.lock();
        try {
            while(queue.isEmpty()) {
                notEmpty.await();
            }
            
            T item = queue.remove();
            notFull.signal();
            return item;
        } finally {
            lock.unlock();
        }
    }
}
```
