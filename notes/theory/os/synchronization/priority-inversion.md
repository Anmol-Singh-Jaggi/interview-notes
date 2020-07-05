# Priority Inversion

- In a priority based scheduling, if a lower priority task (L) is running and if a higher priority task (H) also needs to run, the lower priority task (L) would be preempted by higher priority task (H).
- Now, suppose both lower and higher priority tasks need to share a common resource to achieve their respective work.
- In this case, since there’s resource sharing and task synchronization is needed, several methods can be used for handling such scenarios.
- For sake of our topic on Priority Inversion, let us mention a synchronization method say mutex/semaphore.
- Coming to our discussion of priority inversion, let us examine some scenarios.
  - L is running but not in CS; H needs to run; H preempts L; H starts running; H relinquishes or releases control; L resumes and starts running
  - L is running in CS; H needs to run but not in CS; H preempts L; H starts running; H relinquishes control; L resumes and starts running.
  - L is running in CS; H also needs to run in CS; H waits for L to come out of CS; L comes out of CS; H enters CS and starts running
- Please note that the above scenarios don’t show the problem of any Priority Inversion (not even scenario 3).
- Basically, so long as lower priority task isn’t running in shared CS, higher priority task can preempt it.
- But if L is running in shared CS and H also needs to run in CS, H waits until L comes out of CS.
- The idea is that CS should be small enough so that it doesn’t result in H waiting for a long time while L was in CS. That’s why writing a CS code requires careful consideration.
- In any of the above scenarios, priority inversion (i.e. reversal of priority) didn’t occur because the tasks are running as per the design.
- Now let us add another task of middle priority say M. Now the task priorities are in the order of L < M < H.
- In our example, M doesn’t share the same Critical Section (CS).
- In this case, the following sequence of task running would result in ‘Priority Inversion’ problem; L is running in CS ; H also needs to run in CS ; H waits for L to come out of CS ; M interrupts L and starts running ; M runs till completion and relinquishes control ; L resumes and starts running till the end of CS ; H enters CS and starts running.
- Note that neither L nor H share CS with M.
- Here, we can see that running of M has delayed the running of both L and H.
- Precisely speaking, H is of higher priority and doesn’t share CS with M; but H had to wait for M.
- This is where Priority based scheduling didn’t work as expected because priorities of M and H got inverted in spite of not sharing any CS. This problem is called Priority Inversion.
- In a system with priority based scheduling, higher priority tasks can face this problem and it can result in unexpected behavior/result.
- In general purpose OS, it can result in slower performance. In RTOS, it can result in more severe outcomes.
- The most famous ‘Priority Inversion’ problem was what happened at Mars Pathfinder.
- It can be solved using **Priority inheritance**.

# Priority inheritance

- In Priority Inheritance, when L is in critical section, L inherits priority of H at the time when H starts contending for critical section.
- By doing so, M doesn’t interrupt L and H doesn’t wait for M to finish.
- Please note that inheriting of priority is done temporarily i.e. L goes back to its old priority when L comes out of critical section.