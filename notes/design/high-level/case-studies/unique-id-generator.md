# How to generate a unique id (required for TinyUrl for example)

## Single machine

### Solution 1
- int i=0; i++ forever.
- What if server crashes?
- We'll have to store in some db/disk.

### Solution 2
- Return current time.
- What if if precision is not enough?
- We'll wait for the next nanosecond to return. Not a big deal.

### Solution 3
- Generate a random number between 0 and 10^18.
- Or maybe use already existing UUID libraries.
- But clashes can still happen.
- For every new random number we will have to check the db if it is already in use or not.
- Race condition possible if db not acid compliant.
- Can be slow therefore.

## Multiple machines

### Solution 1
- A machine can be responsible for allocation a range of ids.
- After its exhausted, it can request the central coordinator for the next range.
- Every machine will have to persist the current counter value (to prevent against crashes/reboots).
- The coordinator will have be in a master-slave replication.
- For example, the coordinator will hand out range 1-10^5 to server 1 and 10^5 to 2*10^5 to server 2 and so on...

### Solution 2
- Use timestamp + server-id as the counter value.
- The server mac address is its server id.
- This way even if 2 requests come on 2 machines at the same time, they will get different values.
- Do not server multiple requests in the same nanosecond.
- This will also satisfy the optional requirement of **monotonically increasing** numbers.
- Note that `timestamp + machineID` is the one we will use, not `machineId + timestamp` otherwise monotonically increasing will not work!

### Solution 3
- Every machine can have its own auto-incrementing static integer `int`.
- It can return `int + machineId`.
- But we'll have to persist the last generated value to handle crashes/restarts.

