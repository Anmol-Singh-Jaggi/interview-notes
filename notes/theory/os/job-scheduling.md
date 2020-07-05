# OS Scheduling Algorithmms

## Basics

- **Non-pre-emptive**:  means a process will run on the CPU as long as it wants.
- **Pre-emptive**:  means CPU will run a process only for a very small amount of time, then context-switch.
- **Ready-state**: When a process is ready to run in the queue.
- **Waiting-state**: When a process is blocked for IO.
- **Arrival Time**: The time at which a process arrives at the ready queue the first time.
- **Response Time**: The time after which a process gets the CPU for the first time after entering ready queue.
- **Burst Time**: The time/cycles that a process will take to complete.
- **Waiting Time**: The total time for which a process has waited in the ready queue before it got completed.
- **Completion Time**: The time at which a process is completed.
- **Turn-around Time**:  The total time spent by a process in the system.
- Turn-around = Burst + Waiting
- Turn-around = Completion - Arrival
- We are assuming that a process is not doing any IO at all.
- Criteria for evaluating scheduling algos:
  - Average waiting time.
  - Average Response Time.
  - CPU Utilization.
  - Throughput = No. of processes per second.
- **Gantt Chart**: A chart of current process vs time for a list of processes arrival and burst times.
- **Convoy effect**: Small process has to wait for long process to finish first.
- **Starvation**: A possibility of a process never getting executed due to the algo being biased.

## First Come First Serve (FCFS).

- As the name suggests.
- Always non-pre-emptive.
- Suffers from convoy effect.

## Shortest Job First (SJF).

- Chooses the process with the least burst time among all the processes.
- In the pre-emptive version, chooses the process with the shortest remaining burst time (SRTF).
- SRTF is theoretically the most optimal; least average waiting time.
- Cannot be implemented practically as it is impossible to know burst time in advance.
- May lead to starvation.
- No idea of priority.
- One interesting variant called 'Highest Response Ratio Next', which will increase the priority of the processes which have been waiting for long.


## Priority

- Chooses the process with the highest priority first.
- Both preemptive and non-preemptive.
- Starvation possible.
- 'Ageing' can be used to increase the priority which have been starving.

## Round Robin

- Schedule in a circular queue fashion.
- Small average response time.

## Multi-level queue

![Multi Level Queue](assets/multilevel-queue.png)

- Multiple queues for different types of processes.
- Queues are ordered by priority.
- However, the queues can have different scheduling algos.
- As long as there is even one process in the higher-priority queue, the lower-priority processes will never get any chance leading to starvation.
- So, as a solution, we use a **feedback** mechanism; The processes in lower queues are promoted to higher priorities periodically.