![](assets/garbage-collection.png)

# Tracing Garbage Collection

## Mark and Sweep
- We basically create a graph of objects, where the edges are references.
- For example, if we create a linked list class, the head node has references to all the nodes indirectly.
- Now we do a DFS on this graph, and any vertex that was not visited at all will be eligible for garbage.
- The nodes at which we start doing DFS are called **roots**.
- Example of root objects:
  - Local variable and input parameters of the currently executing methods.
  - Active threads.
  - Static field of the loaded classes.
- For example, if the code flow is in a function `foo()`, and gc happens during this time, then all the local variables of this function will be in the root set.
- Also all variables declared in the functions prior to `foo()` will also be in the root set.
- For example, `main() -> main.foo1() -> main.foo1.foo2()`, then all these 3 functions' variables are in the root set, if gc happened inside `foo2()`.
- The application threads need to be stopped for the marking to happen as you cannot really traverse the graph if it keeps changing under your feet all the time
- Such a situation when the application threads are temporarily stopped so that the JVM can indulge in housekeeping activities is called a **safe point** resulting in a **Stop The World pause**.
- Safe points can be triggered for different reasons but garbage collection is by far the most common reason for a safe point to be introduced.
- The duration of this pause depends neither on the total number of objects in heap nor on the size of the heap but on the number of alive objects.
- So increasing the size of the heap does not directly affect the duration of the marking phase.
- This is also called **Mark and Sweep Algorithm**.
- All the unvisited objects will be destroyed or sweeped.
- When GC destroys an object, it calls the `finalize()` method.
- `finalize()` can be useful when, say, you want to close a connection.
- But in most cases, its not required at all, as when the JVM gets killed, the connection will get killed too.
- Otherwise, we would be in trouble when, say, there is some network outage or power outage.
- We can invoke gc manually by `System.gc()`, however its completely implementation specific if it actually runs the gc or not. It might just return immediately without doing anything.
- As per JVM specs, even `finalize()` might or might not be called on gc. It is also deprecated in Java 9.
- The correct way to close connections/resources is to actually implement a proper dedicated `close()` method.
- There is **one and only one** reason for overriding `finalize()` but its a **very good reason**; To place error logging code in `finalize()` which notifies you if you ever forget to invoke `close()`.
- Note that we are intentionally not calling `close()` again in `finalize()` because there must be only one right way to do anything.
- We can potentially add a static reference back to the resource being killed in the `finalize()` method. This is called **reviving** the object.
- Note that `finalize()` gets called only once by GC thread. If object revives itself, then `finalize()` will not be called again.
- Java has a `Closable` interface implementing `close()` method.
- All closable objects can be used in a **try-with-resources** statement.
- For example:
```java
try (
        java.util.zip.ZipFile zf =
             new java.util.zip.ZipFile(zipFileName);
        java.io.BufferedWriter writer = 
            java.nio.file.Files.newBufferedWriter(outputFilePath, charset)
    ) {
        // Use the resources.
      }
```
- All the resources are automatically closed at the end of the block (**even if there is an exception**).
- A try-with-resource statement can have `catch` and `finally` blocks, but they will be called only after resources are closed.

## Generational Mark and Sweep
- The GC keeps objects in 2 areas: `young` and `old`.
- The idea is that the objects that are still alive after multiple GC cycles are probably going to stay alive for a while.
- So, GC will explore the old area only once in multiple cycles.
- However, it will explore young area every time.
- If an object survives GC in young area multiple times, it will be promoted to old area.

# Automatic Reference Counting
- This is an alternate solution apart from Mark-and-sweep algorithm.
- Used in Python.
- Objects are deallocated once there are no more references to them, i.e. no other variable refers to the object in particular.
- Each object contains a reference counter, stored as an extra field in memory, which is incremented every time you set a variable to that object (i.e. a new reference to the object is created), and is decremented every time you set a reference to the object to nil/null, or a reference goes out of scope (i.e. it is deleted when the stack unwinds), once the reference counter goes down to zero, the object takes care of deleting itself, calling the destructor and freeing the allocated memory.
- They are generally considered to be inferior to tracing algos because:
  - **Cyclic references:** Reference counting alone leaks cycles so reference counted smart pointers will leak memory in general unless other techniques are added to catch cycles.  
  Once those techniques are added, reference counting's benefit of simplicity has vanished.  
  Also, note that scope-based reference counting and tracing GCs collect values at different times, sometimes reference counting collects earlier and sometimes tracing GCs collect earlier.
  This can be handled by using weak references though.
  - **Throughput:** Smart pointers are one of the least efficient forms of garbage collection, particularly in the context of multi-threaded applications when reference counts are bumped atomically (Python's GIL).  
  - **Latency:** Typical smart pointer implementations allow destructors to avalanche, resulting in unbounded pause times.  
    Other forms of garbage collection are much more incremental and can even be real time, e.g. Baker's treadmill.

# Strong vs Soft vs Weak references
- Strong reference means a normal reference; will cause a `count++` to the object's reference count.
- Weak reference means the object's reference count will not be incremented.
- The idea is to avoid holding on to an object when it should have been destroyed (for example, cache).
- Also, it helps avoid cyclic dependencies (in a Tree node, child should only have a weak reference to the parent).
- Soft reference is almost identical to weak, the difference being that it might not be destroyed even if its count is 0.
  JVM will delete a softly referenced object only if its low on memory.
- `Strong > Soft > Weak > Phantom`.
- I have no idea what phantom reference does.