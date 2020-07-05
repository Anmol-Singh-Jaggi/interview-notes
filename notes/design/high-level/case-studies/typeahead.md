# Operations:
- Get top 20 suggestions based on a prefix string.
- Add new word to the dictionary.
- Remove word from the dictionary.
- Update frequency of a word.

# Basics
- We can build a trie obviously.


# Suggestions
- Lets say we have a trie and a prefix string `cat`.
- Now first of all, at the tail node of every word, we will maintain the frequency of that word.
- We can do a DFS starting from the tail node to get all the words and put them in a priority queue based on the frequency.
- But this is slow.
- Alternatively, at every node (not necessarily end-of-word node), we can maintain a map of top 20 words starting from this prefix.
- So, when we want a suggestion, we can simply return that map.
- But how do we update and maintain this map?
- While inserting a word, we'll have to update the map of every node along the path starting from the root.
- If the word already exists in the map, we will simply increment its count.
- Otherwise, if the new count > min(map), then we will replace the lowest key in the map with this entry.
- So reads are fast and writes are slow, but thats perfect as the number of reads will be far more than writes.
- The hashmap can also be stored separately in Redis.


# Adding a new word or updating the frequency
- Rather than doing it for every word, we can first create a buffer of say 1000 words, then do the insertions in a batch at night.
- Or we can create a copy of the trie, and then update that trie.
- Then finally just point to that trie.
- So any modifications to the trie happen in this way.
- This avoids the need of locking and synchronization.


# Removing a word
- We can simply remove a word in the copy of the trie and update the necessary maps along the path.


# Scaling
- Actually even for a large dictionary, it can easily fit inside a 32 GB RAM.
- There will be no database involved.
- For persistence, we can simply persist the tree into a file.
- We dont even need any HDFS kind of a setup, since the serialization will be 32 GB itself.
- But still, if we want to scale, we can do it in a couple of ways:

## Range-based
- We can have the portion of the trie starting with 'a' in server 1, 'b' in server 2 and so on...
- But this might lead to an imbalance.

## Memory-based
- Lets say we constraint the memory consumption of a single machine to 4 GB.
- If the total size of the trie was 32 GB, then we would need 8 machines.
- Lets say we store the words 'Aa' to 'Abcd' in machine 1 such that 4GB is full.
- Now the rest of the words we can start filling in machine 2, 3 ... 8.
- We will have to maintain a config hash map containing a mapping of these ranges to the machine id.
- Also it might happen that a certain prefix's children are half in machine 1 and half in machine 2.
- So we'll need to send the requests to all the machines and then aggregate the results.

For example:

```
# The hashmap
Server 1, A-AABC
Server 2, AABD-BXA
Server 3, BXB-CDA
```

- For querying, if the user has typed ‘A’ we have to query both server 1 and 2 to find the top suggestions.
- When the user has typed ‘AA’, we still have to query server 1 and 2, but when the user has typed ‘AAA’ we only need to query server 1.

## Consistent hashing
- We can hash a word onto a server.
- But we will need to query all the machines and aggregate the results for the suggestions.
- Also, each server will be of a master-slave form for fault tolerance.


# Caching
- Remember that Caching will be of extreme use in this problem as 20% of all the words will be searched 80% of the time.
- So we can cache the suggestions for most popular prefixes.


# Typeahead Client
- The client should only try hitting the server if the user has not pressed any key for 50ms.
- If the user is constantly typing, the client can cancel the in-progress requests.
- Initially, the client can wait until the user enters a couple of characters.
- Clients can store the recent history of suggestions locally. Recent history has a very high rate of being reused.
