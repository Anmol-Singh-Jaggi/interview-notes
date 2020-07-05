'''
Implement a data structure supporting the following operations:

    Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
    Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
    GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
    GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".

Challenge: Perform all these in O(1) time complexity.

SOLUTION:

Use a doubly linked list + hashmap.
Main idea is to maintain a list of Bucket's, each Bucket contains all keys with the same count.
head and tail can ensure both getMaxKey() and getMaxKey() be done in O(1).
keyCountMap maintains the count of keys, countBucketMap provides O(1) access to a specific Bucket with given count. Deleting and adding a Bucket in the Bucket list cost O(1), so both inc() and dec() take strict O(1) time.

'''
