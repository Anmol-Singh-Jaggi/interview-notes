Initialize 2 binary semaphores:
- read_count_access = 1 // For guarding modification to read_count variable
- exclusive_access = 1 // For guarding access to resource.
- int read_count = 0

Writer:

```python
wait(exclusive_access)
# Write
signal(exclusive_access)
```

Reader:

```python
wait(read_count_access)
readcount += 1
if readcount == 1:
    wait(exclusive_access)
signal(read_count_access)
# Read
wait(read_count_access)
readcount -= 1
if readcount == 0:
    signal(exclusive_access)
signal(read_count_access)
```

Note that the expensive read operation is not in critical section, ensuring efficiency.
This solution may starve writers.

Better solution ensuring fairness:

```java
int readCount = 0;              // init to 0; number of readers currently accessing resource

Semaphore resourceAccess = 1;   // controls access (read/write) to the resource
Semaphore readCountAccess = 1;  // for syncing changes to shared variable readCount
Semaphore serviceQueue = 1;     // FAIRNESS: preserves ordering of requests (signaling must be FIFO)

void writer()
{
    serviceQueue.P();           // wait in line to be serviced
    resourceAccess.P();         // request exclusive access to resource
    serviceQueue.V();           // let next in line be serviced
    writeResource();            // writing is performed
    resourceAccess.V();         // release resource access for next reader/writer
}

void reader()
{
    serviceQueue.P();           // wait in line to be serviced
    readCountAccess.P();        // request exclusive access to readCount
    if (readCount == 0)         // if there are no readers already reading:
        resourceAccess.P();     // request resource access for readers (writers blocked)
    readCount++;                // update count of active readers
    serviceQueue.V();           // let next in line be serviced
    readCountAccess.V();        // release access to readCount
    readResource();             // reading is performed
    readCountAccess.P();        // request exclusive access to readCount
    readCount--;                // update count of active readers
    if (readCount == 0)         // if there are no readers left:
        resourceAccess.V();     // release resource access for all
    readCountAccess.V();        // release access to readCount
}
```

- This is almost the same solution as the original one apart from the user of `serviceQueue`.