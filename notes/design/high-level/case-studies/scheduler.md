# How will you implement library like Quartz/Cron?

## Approach 1:
- We can have a main thread which will monitor the crontab file for any job additions.
- As soon as there is a new job added, we can fire a new thread dedicated to that command.
- This thread will keep running in an infinite loop:
```
void run()
{
    job.execute()
    sleep(job.nextExecutionTime() - currentTime())
}
```
- This is a very simple approach. However, it suffers from performance issues as a system can only contain so many threads at a time. Moreover, thread creation and deletion is expensive and time-consuming.

## Approach 2:
- We can have a finite thread-pool which will execute all the tasks by picking them up from a blocking priority queue(heap) sorted on `job.nextFireTime()`.
- We will have one thread which will be running in an infinite loop and submitting new jobs to the thread pool after consuming them from the queue. Lets call it **Thread1**.
```
// Thread1:

void goToSleep(job){
    queue.push(job)
    duration = job.nextFireTime() - currentTime
    sleep(duration)
}

void executeJob(job){
    threadpool.submit(new Thread(() -> job.execute()));
    if(job.isRecurring()){
        /*
        Note that adding the next job iteration at this point might not
        be what we want for long-running tasks, because the next iteration 
        will start even before the current one is finished.
        As an alternate, we can insert this logic in the thread-pool Runnable itself
        so that the next job iteration is scheduled only when the current 
        one is complete.
        */
        job = job.copy()
        job.setNextFireTime(getCurrentTime() + job.getFiringInterval())
        queue.add(new Job())
    }
}

void run(){
    while(true)
    {
        currentTime = getCurrentTime()
        job = queue.pop()
        if(job.nextFireTime() > currentTime){
            goToSleep(job)
        }
        else{
            executeJob(job)
        }
    }
}
```
- There will be one more thread **Thread2** which will be monitoring the crontab file for any new job additions and will push them to the queue.
- There is one problem with this:
  - Imagine that Thread1 is sleeping and will wake up after an hour.
  - Meanwhile a new task arrives which is supposed to run every minute.
  - This new task will not be able to start executing until an hour later.
- To solve this problem, we can make Thread2 wakeup Thread1 from its sleep forcefully whenever the new task has to run sooner than the front task in queue.
```
// Thread2:

void run()
{
    while(true){
        newJob = getNewJobFromCrontabFile() // either blocking call or interrupt driven
        nextJob = queue.peek()
        if(newJob.getNextFiringTime() < nextJob.getNextFiringTime()){
            queue.push(newJob)
            thread1.interrupt()
        }
        else{
            queue.push(newJob)
        }
    }
}
```
- Bonus: What will happen if the system crashes? How will the jobs be resumed? Should we ignore all the missed recurring jobs?

# Distributed scheduler
- If we have the scheduler service running on just one machine, it is unreliable(what if the machine crashes).
- It can also suffer from high load.
- To solve the high load problem, we can simply do sharding(execute 10% of the jobs in one machine if there are 10 machines).
- https://landing.google.com/sre/sre-book/chapters/distributed-periodic-scheduling/