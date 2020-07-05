"""
Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline.
It is also given that every job takes single unit of time, so the minimum possible deadline for any job is 1.
How to maximize total profit if only one job can be scheduled at a time.

Examples:

Input: Four Jobs with following deadlines and profits
JobID  Deadline  Profit
  a      4        20
  b      1        10
  c      1        40
  d      1        30
Output: Following is maximum  profit sequence of jobs - [c, a]


Input:  Five Jobs with following deadlines and profits
JobID   Deadline  Profit
  a       2        100
  b       1        19
  c       2        27
  d       1        25
  e       3        15
Output: Following is maximum profit sequence of jobs - [c, a, e]

SOLUTION:
1) Sort all jobs from highest to lowest profit.
2) Initialize the result sequence as first job in sorted jobs.
3) Do following for remaining n-1 jobs:
 - If the current job can fit in the current result sequence without missing the deadline, add current job to the result.
   Else ignore the current job.
Complexity -> O(n*n)

How to check if a job can fit in the current deadline:
Maintain a boolean array 'slots'. If slots[i] is true, means that some job has already been scheduled for time i.
Lets a job has deadline 'x'.
Now, check if any slot from x down to 0 is false (empty) or not.
Assign this job to the highest such empty index found.
Highest because we want the lower time slots to be available for future jobs with lower deadlines.

SOLUTION 2:
Use disjoint-set:
Let parent[i] signify the latest empty slot <= i.
Then we can keep on using and updating ds.parent to get the latest empty slot in almost O(1).
Total complexity -> O(n)
"""
from ds.disjoint_set.disjoint_set import DisjointSet


def find_latest_available_slot(time_slots, deadline):
    # O(n)
    start = min(deadline, len(time_slots) - 1)
    for i in range(start, 0, -1):
        if time_slots[i] is None:
            return i
    return None


def find_latest_available_slot_disjoint_set(time_slots, deadline, ds):
    # Almost O(1)
    deadline = min(deadline, len(time_slots) - 1)
    latest_slot = ds.find_parent(deadline)
    if latest_slot == 0:
        return None
    # Update this node's parent.
    new_parent = ds.find_parent(latest_slot - 1)
    ds.parent[latest_slot] = new_parent
    assert time_slots[latest_slot] is None
    return latest_slot


def job_sequencing(jobs):
    jobs.sort(reverse=True)
    time_slots = [None] * (len(jobs) + 1)
    ds = DisjointSet()
    for i in range(len(jobs)):
        job = jobs[i]
        job_deadline = job[1]
        latest_available_slot_idx = find_latest_available_slot_disjoint_set(
            time_slots, job_deadline, ds
        )
        if latest_available_slot_idx is not None:
            time_slots[latest_available_slot_idx] = job
    return time_slots


def main():
    jobs = []
    jobs.append((100, 2))
    jobs.append((19, 1))
    jobs.append((27, 2))
    jobs.append((25, 1))
    jobs.append((15, 3))
    ans = job_sequencing(jobs)
    print(ans)


main()
