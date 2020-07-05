For LRU cache, you really need a doubly linked list with O(1) random **iterator** removal for the cache to be O(1).
It is important that calling `remove()` does not invalidate all the other iterators.

C++ contains such a list. Python and Java do not. But they make it even more easier.
In Python, we can actually use just a single data structure `OrderedDict` for all of this. 
In Java, a `LinkedHashMap` will do the job.

The drawback is that frequently used items will be evicted when a lot of new items are added to cache, even if they will never be accesed again.
