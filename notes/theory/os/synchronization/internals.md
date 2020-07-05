```java
// Basic parts of threading system:
// Assume "ThreadQueue" supports random access.
public volatile ThreadQueue readyQueue; // Thread-unsafe queue of ready threads.  Elements are (Thread*).
public volatile global Thread* currentThread; // Assume this variable is per-core.  (Others are shared.)

// Implements a spin-lock on just the synchronized state of the threading system itself.
// This is used with test-and-set as the synchronization primitive.
public volatile global bool threadingSystemBusy=false;

// Context-switch interrupt service routine (ISR):
// On the current CPU core, preemptively switch to another thread.
public method contextSwitchISR(){
    if (testAndSet(threadingSystemBusy)){
        return; // Can't switch context right now.
    }
    // Ensure this interrupt can't happen again which would foul up the context switch:
    systemCall_disableInterrupts();
    // Get all of the registers of the currently-running process.
    // For Program Counter (PC), we will need the instruction location of
    // the "resume" label below.  Getting the register values is platform-dependent and may involve
    // reading the current stack frame, JMP/CALL instructions, etc.  (The details are beyond this scope.)
    currentThread->registers = getAllRegisters(); // Store the registers in the "currentThread" object in memory.
    currentThread->registers.PC = resume; // Set the next PC to the "resume" label below in this method.
    readyQueue.enqueue(currentThread); // Put this thread back onto the ready queue for later execution.
    Thread* otherThread=readyQueue.dequeue(); // Remove and get the next thread to run from the ready queue.
    currentThread=otherThread; // Replace the global current-thread pointer value so it is ready for the next thread.
    // Restore the registers from currentThread/otherThread, including a jump to the stored PC of the other thread
    // (at "resume" below).  Again, the details of how this is done are beyond this scope.
    restoreRegisters(otherThread.registers);
    // *** Now running "otherThread" (which is now "currentThread")!  The original thread is now "sleeping". ***
    resume: // This is where another contextSwitch() call needs to set PC to when switching context back here.
    // Return to where otherThread left off.
    threadingSystemBusy=false; // Must be an atomic assignment.
    systemCall_enableInterrupts(); // Turn pre-emptive switching back on on this core.

}

// Thread sleep method:
// On current CPU core, a synchronous context switch to another thread without putting
// the current thread on the ready queue.
// Must be holding "threadingSystemBusy" and disabled interrupts so that this method
// doesn't get interrupted by the thread-switching timer which would call contextSwitchISR().
// After returning from this method, must clear "threadingSystemBusy".
public method threadSleep(){
    // Get all of the registers of the currently-running process.
    // For Program Counter (PC), we will need the instruction location of
    // the "resume" label below.  Getting the register values is platform-dependent and may involve
    // reading the current stack frame, JMP/CALL instructions, etc.  (The details are beyond this scope.)
    currentThread->registers = getAllRegisters(); // Store the registers in the "currentThread" object in memory.
    currentThread->registers.PC = resume; // Set the next PC to the "resume" label below in this method.
    // Unlike contextSwitchISR(), we will not place currentThread back into readyQueue.
    // Instead, it has already been placed onto a mutex's or condition variable's queue.
    Thread* otherThread=readyQueue.dequeue(); // Remove and get the next thread to run from the ready queue.
    currentThread=otherThread; // Replace the global current-thread pointer value so it is ready for the next thread.
    // Restore the registers from currentThread/otherThread, including a jump to the stored PC of the other thread
    // (at "resume" below).  Again, the details of how this is done are beyond this scope.
    restoreRegisters(otherThread.registers);
    // *** Now running "otherThread" (which is now "currentThread")!  The original thread is now "sleeping". ***
    resume: // This is where another contextSwitch() call needs to set PC to when switching context back here.
    
}

public method wait(Mutex m, ConditionVariable c){
    // Internal spin-lock while other threads on any core are accessing this object's
    // "held" and "threadQueue", or "readyQueue".
    while (testAndSet(threadingSystemBusy)){}
    // N.B.: "threadingSystemBusy" is now true.
    // System call to disable interrupts on this core so that threadSleep() doesn't get interrupted by
    // the thread-switching timer on this core which would call contextSwitchISR().
    // Done outside threadSleep() for more efficiency so that this thread will be sleeped
    // right after going on the condition-variable queue.
    systemCall_disableInterrupts();
    assert m.held; // (Specifically, this thread must be the one holding it.)
    m.release();
    c.waitingThreads.enqueue(currentThread);
    threadSleep();
    // Thread sleeps ... Thread gets woken up from a signal/broadcast.
    threadingSystemBusy=false; // Must be an atomic assignment.
    systemCall_enableInterrupts(); // Turn pre-emptive switching back on on this core.
    // Mesa style:
    // Context switches may now occur here, making the client caller's predicate false.
    m.acquire();
}

public method signal(ConditionVariable c){
    // Internal spin-lock while other threads on any core are accessing this object's
    // "held" and "threadQueue", or "readyQueue".
    while (testAndSet(threadingSystemBusy)){}
    // N.B.: "threadingSystemBusy" is now true.
    // System call to disable interrupts on this core so that threadSleep() doesn't get interrupted by
    // the thread-switching timer on this core which would call contextSwitchISR().
    // Done outside threadSleep() for more efficiency so that this thread will be sleeped
    // right after going on the condition-variable queue.
    systemCall_disableInterrupts();
    if (!c.waitingThreads.isEmpty()){
        wokenThread=c.waitingThreads.dequeue();
        readyQueue.enqueue(wokenThread);
    }
    threadingSystemBusy=false; // Must be an atomic assignment.
    systemCall_enableInterrupts(); // Turn pre-emptive switching back on on this core.
    // Mesa style: The woken thread is not given any priority.
    
}

public method broadcast(ConditionVariable c){
    // Internal spin-lock while other threads on any core are accessing this object's
    // "held" and "threadQueue", or "readyQueue".
    while (testAndSet(threadingSystemBusy)){}
    // N.B.: "threadingSystemBusy" is now true.
    // System call to disable interrupts on this core so that threadSleep() doesn't get interrupted by
    // the thread-switching timer on this core which would call contextSwitchISR().
    // Done outside threadSleep() for more efficiency so that this thread will be sleeped
    // right after going on the condition-variable queue.
    systemCall_disableInterrupts();
    while (!c.waitingThreads.isEmpty()){
        wokenThread=c.waitingThreads.dequeue();
        readyQueue.enqueue(wokenThread);
    }
    threadingSystemBusy=false; // Must be an atomic assignment.
    systemCall_enableInterrupts(); // Turn pre-emptive switching back on on this core.
    // Mesa style: The woken threads are not given any priority.
    
}


class Mutex {
    protected volatile bool held=false;
    private volatile ThreadQueue blockingThreads; // Thread-unsafe queue of blocked threads.  Elements are (Thread*).
    public method acquire(){
        // Internal spin-lock while other threads on any core are accessing this object's
        // "held" and "threadQueue", or "readyQueue".
        while (testAndSet(threadingSystemBusy)){}
        // N.B.: "threadingSystemBusy" is now true.
        // System call to disable interrupts on this core so that threadSleep() doesn't get interrupted by
        // the thread-switching timer on this core which would call contextSwitchISR().
        // Done outside threadSleep() for more efficiency so that this thread will be sleeped
        // right after going on the lock queue.
        systemCall_disableInterrupts();
        assert !blockingThreads.contains(currentThread);
        if (held){
            // Put "currentThread" on this lock's queue so that it will be
            // considered "sleeping" on this lock.
            // Note that "currentThread" still needs to be handled by threadSleep().
            readyQueue.remove(currentThread);
            blockingThreads.enqueue(currentThread);
            threadSleep();
            // Now we are woken up, which must be because "held" became false.
            assert !held;
            assert !blockingThreads.contains(currentThread);
        }
        held=true;
        threadingSystemBusy=false; // Must be an atomic assignment.
        systemCall_enableInterrupts(); // Turn pre-emptive switching back on on this core.
    }        
        
    public method release(){
        // Internal spin-lock while other threads on any core are accessing this object's
        // "held" and "threadQueue", or "readyQueue".
        while (testAndSet(threadingSystemBusy)){}
        // N.B.: "threadingSystemBusy" is now true.
        // System call to disable interrupts on this core for efficiency.
        systemCall_disableInterrupts();
        assert held; // (Release should only be performed while the lock is held.)
        held=false;
        if (!blockingThreads.isEmpty()){
            Thread* unblockedThread=blockingThreads.dequeue();
            readyQueue.enqueue(unblockedThread);
        }
        threadingSystemBusy=false; // Must be an atomic assignment.
        systemCall_enableInterrupts(); // Turn pre-emptive switching back on on this core.
    }
}

struct ConditionVariable {
    volatile ThreadQueue waitingThreads;
}
```

Semaphores using Monitors
=========================

```java
class Semaphore
{
  private volatile int s := 0
  invariant s >= 0
  private ConditionVariable sIsPositive /* associated with s > 0 */
  private Mutex myLock /* Lock on "s" */

  public method P()
  {
    myLock.acquire()
    while s = 0:
      wait(myLock, sIsPositive)
    assert s > 0
    s := s - 1
    myLock.release()
  }

  public method V()
  {
    myLock.acquire()
    s := s + 1
    assert s > 0
    signal sIsPositive
    myLock.release()
  }
}
```

Monitors using Semaphores
=========================

```java
public method wait(Mutex m, ConditionVariable c){
    assert m.held;
    c.internalMutex.acquire();
    c.numWaiters++;
    m.release(); // Can go before/after the neighboring lines.
    c.internalMutex.release();
    // Another thread could signal here, but that's OK because of how
    // semaphores count.  If c.sem's number becomes 1, we'll have no
    // waiting time.
    c.sem.Proberen(); // Block on the CV.
    // Woken
    m.acquire(); // Re-acquire the mutex.
}

public method signal(ConditionVariable c){
    c.internalMutex.acquire();
    if (c.numWaiters > 0){
        c.numWaiters--;
        c.sem.Verhogen(); // (Doesn't need to be protected by c.internalMutex.)
    }
    c.internalMutex.release();

}

public method broadcast(ConditionVariable c){
    c.internalMutex.acquire();
    while (c.numWaiters > 0){
        c.numWaiters--;
        c.sem.Verhogen(); // (Doesn't need to be protected by c.internalMutex.)
    }
    c.internalMutex.release();

}

class Mutex {
    protected boolean held=false; // For assertions only, to make sure sem's number never goes > 1.
    protected Semaphore sem=Semaphore(1); // The number shall always be at most 1.
    public method acquire(){
        sem.Proberen();
        assert !held;
        held=true;
    }
    
    public method release(){
        assert held; // Make sure we never Verhogen sem above 1.  That would be bad.
        held=false;
        sem.Verhogen();
    }
}

class ConditionVariable {
    protected int numWaiters=0; // Roughly tracks the number of waiters blocked in sem.
    protected Semaphore sem=Semaphore(0); // Provides the wait queue.
    protected Mutex internalMutex; // (Protects "numWaiters".)
}
```

# Semaphore basic implementation

## 1. Using while loop

```python
def wait(sem):
    while True:
       # Interrupt disabled!
       # This process cannot be preempted now!
       if sem >= 0:
            sem -= 1
            break
       # Interrupt enabled!


def signal(sem):
    # Interrupt disabled!
    sem += 1
    # Interrupt enabled!

```

## 2. Using `block()` and `wakeup()`

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

## 3. Binary semaphore using Ticket Lock.

- Can be used to implement a binary semaphore.
- Has the same principle when you go to a doctor and you get a token number.
- First lets see the pseudocode:

```python
max_ticket = now_serving = 0

def wait():
  # fetch_and_inc() is atomic.
  my_ticket = fetch_and_inc(max_ticket)
  while now_serving != my_ticket:
    # Someone else has the lock 
    pass


def signal():
  now_serving += 1
```

- The code is pretty self-explanatory.
- It is FIFO. Which means no starvation; ensures fairness!!
- The biggest disadvantage of the Ticket Lock is that the fairness property backfires once there are more threads competing for the lock than there are CPU cores in the system. The problem is that in that case the thread which can enter the CS next might be sleeping.
- This means that all other threads must wait, because of the strict fairness guarantee. This property is sometimes referred to as 'preemption intolerance'.