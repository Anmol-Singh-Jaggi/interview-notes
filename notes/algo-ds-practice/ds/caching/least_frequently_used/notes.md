## Least Frequently Used

- Uses a counter to keep track of how often an entry is accessed. 
- The entry with the lowest count is removed first.
- This method isn't used that often, as it does not account for an item that had an initially high access rate and then was not accessed for a long time.
- Implementation:
  - Keep a mapping of `entry` vs `frequency`.
  - Also keep a reverse mapping of `frequency` vs `LinkedList<Entry>`.
  - As soon as an entry is accessed, remove it from its current linked list (corresponding to `current_freq`), and append it to the list corresponding to `current_freq + 1`.
  - If a new entry is accessed, add it to the list corresponding to frequency 1.
  - If a new entry is accessed and the cache size is full, then remove the first element from list corresponding to frequency 1, and add this new entry at the end of that list.
- This approach has one major drawback when cache is full: a new saved item could cause the eviction of an item more frequently used than the new one. This is called cache pollution.
