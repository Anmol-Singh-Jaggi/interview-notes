'''
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive at the same time.

Example:

Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true;

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;

SOLUTIONS:

Solution 1:
Use a Map of message vs its latest timestamp.
The problem is that memory keeps growing (no key is ever deleted).

Solution 2:
Use a queue and a set.
The set will contain the messages that are present right now in the queue.
The queue will only hold messages that are not expired.
At every method call, we will keep popping from queue until the top is withing 10 seconds window.
Note that we are using a queue and not a priority queue as in the input timestamp will always be monotonicall increasing.

Solution 3:
Radix sort style solution.
For every digit 'd' from 0-9, we can keep an integer value denoting the latest timestamp 't' such that t % 10 = d.
Also for every digit 'd', we can maintain a set of messages that arrived at bucket[d]. Note that we have to maintain a set and not just 1 string since there can be multiple messages in 1 second.
Then for every function call, we will iterate through all the buckets whose timestamp is within 10 seconds to see if that set contains this message or not.
We will also keep clearing the buckets.

Solution 4:
Use 2 hashmaps.
I am not able to fully understand this solution.

Source - https://leetcode.com/problems/logger-rate-limiter/discuss/391558/Review-of-four-different-solutions%3A-HashMap-Two-Sets-Queue-with-Set-Radix-buckets-(Java-centric)


Also read this - https://www.geeksforgeeks.org/design-a-hit-counter/
'''
