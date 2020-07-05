## ReentrantLock vs sychronized():
 - Lock can spread out across multiple methods, whereas sychronized can span upto only 1 method.
 - Lock supports interruped/timed lock waits.
 - Any object in Java can be turned into a monitor by the use of `sychronized()/wait()/notify()` but it will have only 1 condition variable, whereas a lock object can have multiple conditions.
 - Always prefer lock objects.

## `notifyAll()` vs `notify()`
- Use `notifyAll()` when one cv is used for multiple conditions.
- For eg. while solving producer-consumer using just one condition variable 'sizeChanged'.

## Why methods like `wait()`, `notify()` and `notifyAll()` are present in object class and not in Thread class?
- Because any object can be used as a lock.
- A thread never calls its own `wait()` method.

```java
Object lock = new Object();
synchronized (lock) {
    lock.wait(); // Will block until lock.notify() is called on another thread.
}

// Somewhere else...
...
synchronized (lock) {
    lock.notify(); // Will wake up lock.wait()
}
```