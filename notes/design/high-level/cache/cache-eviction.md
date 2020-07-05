# Cache eviction strategies

## FIFO

- Entry that has been in cache the longest will be evicted first.  
- It is different from LRU because it ignores the access order of entries. 

## LIFO

- Well you know the story.

## Least Recently Used

- The entry that has been untouched the longest gets evicted first.
- The drawback is that frequently used items will be evicted when a lot of new items are added to cache, even if they will never be accesed again.

## Most Recently Used

- Useful in situations where the older an item is, the more likely it is to be accessed.
- Imagine you were looking up the details of buses as they arrived at a bus stop, based on their bus number.
- It's somewhat reasonable to think that if you've just seen a number 36 bus, you're less likely to see another one imminently than to see one of the other buses that stops there.

## Time-To-Live Cache

- Each entry will have a TTL.
- Evict the entry which has the most expired TTL, or the one which will be expiring the soonest.
- **Implementation**:
  - Keep a min-heap with entries sorted according to `expire_at` field.
  - When an (existing) entry is accessed, remove the value:
    - If its not expired, return the value, refresh the `expire_at` field and reinsert.
    - If its expired, then refresh from backend and reinsert and then return value.
  - For eviction, pop from heap, insert the new entry.
  - We can also use Akka to greedily remove stale entries using schedulers.

##  Time-Aware Least Recently Used

- LRU + Time-To-Live for an entry.
- Can be used in CDNs.
- **Implementation**
  - Very similar to normal LRU.
  - Just that while accessing entry, if its expired then, refresh from backend.

## Least Frequently Used

- Uses a counter to keep track of how often an entry is accessed. 
- The entry with the lowest count is removed first.
- If there are multiple entries with same count, remove the least recently used.
- This method isn't used that often, as it does not account for an item that had an initially high access rate and then was not accessed for a long time.
- **Implementation**:
  - Keep a mapping of `entry` vs `frequency`.
  - Also keep a reverse mapping of `frequency` vs `LinkedList<Entry>`.
  - As soon as an entry is accessed, remove it from its current linked list (corresponding to `current_freq`), and append it to the list corresponding to `current_freq + 1`.
  - If a new entry is accessed, add it to the list corresponding to frequency 1.
  - If a new entry is accessed and the cache size is full, then remove the first element from list corresponding to frequency 1, and add this new entry at the end of that list.
- This approach has one major drawback when cache is full: a new saved item could cause the eviction of an item more frequently used than the new one. This is called cache pollution.