Unlike my C++ implementation, this one used open-probing as the hash collision strategy. Why???  
 - Locality of reference advantage.
 - Less memory overhead.

Another difference is that it does not use any advanced data structures like `set` internally.
The C++ implementation's complexity is `O(logn)` because of using `set`, but the Python one is O(1).

Also, remember that in a hash table, keys should always be immutable.
That is why in Python, dictionary/list etc are not allowed to be used as keys in a dictionary.

The open probing key index recurrence `index = ((5*index) + 1) mod size` is beautiful in the sense that it will cover all the numbers from 0 to `size` exactly once. WTF!!!!!
In fact this is the one that is used in the actual Python dict implementation as well.

There is something called `Round robin hashing` which helps minimize the average probe sequence length by basically moving elements from a large probe sequence to a smaller one. Its pretty easy to understand bu I am too lazy to implement it right now. See [this](https://www.sebastiansylvan.com/post/robin-hood-hashing-should-be-your-default-hash-table-implementation/) for explanation.


**Note:**

Hash table can also be implemented without dummy object. (**Update:** No it cannot. See the end)
(**Update 2**: It can, but probably only in the case of simple linear probing. See my `cs.stackexchange` account.)
In that case, `get()` and `put()` would be more efficient, but `remove()` would become inefficient and very hard to implement. Here is the algorithm for `remove()` in such a case:

Notations used:
 - `e[i]` => Element at index `i`.
 - `pl[i]` => Probe length at index `i`.
 - `subseq[i]` => The probe subsequence starting at the index `i`. 
 - A probe subsequence `e[m]`...`e[n]` refers to a subsequence where `pl[m] != pl[m-1]` and `pl[i] == pl[i-1] + 1` for all `i` from `m+1` to `n`.

An example:

Lets say there is a probe sequence:
`1 2 3 4 3 4 5 2 3 1 None`
`0 1 2 3 4 5 6 7 8 9` (indices of those elements)
where the numbers represent the probe length of the respective elements.
It has four probe subsequences starting at indices 0, 4, 7 and 9.
An element of a subsequence `el[i]` had its original hash at the index `i - el[i]`.

Lets say we have to remove `el[5]`, then we can just not simply mark it as `None`.
Now you might think we can just bring the last element of the probe sequence `el[9]` to its place.
But this would result in `get(el[9])` being `None` because its original hash was at index `9`. So the probe search would start at `9` and find `None` there.
So the correct solution is to move the last element of the removed element's probe **subsequence** to its place.
So we will bring `el[6]` to `el[5]`. But now `el[6]` is `None`, which means there is a hole in the probe sequence as a whole.
So `get(el[7])` would return `None` as its starting hash `el[6]` would be `None`.
So the complete algorithm is:
 - Mark the removed element `el[r]` as `None`.
 - Bring the last element of its subsequence `el[last1]` to `el[r]`.
 - If the next subsequence's first element has a probe length of 1, then just stop.
 - Bring the last element of the next subsequence `el[last2]` to `last1` and update its probe length `pl[last1] = pl[last1+1] - 1`.
 - Go to previous step.


Wait but this algorithm is still wrong, because I was assuming that the there are probe `subsequences`. But there are actually probe `subsets`, implying elements whose original hash is the same can be scattered around the hash table, not in a contigous way.
For example the following probe sequence:
`1 2 3 4 2 6 4 8`

This is getting harder than I thought. I guess thats why they use the dummy.
Will think about a proper algorithm later on.
