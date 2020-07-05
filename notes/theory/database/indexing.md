- File is divided into records.
- Hard disk is divided into blocks.
- Block size is usually greater than record size.
- **Sorted vs Non-sorted**:
  - A table can either be stored in a sorted way wrt to a particular attribute.
  - Or it can be randomly stored.
  - If sorted, then searching is easy(binary search), but insertions and deletions are hard.
- **Spanned vs Unspanned mapping**:
  - Lets say a block size is 1024 bytes and record size is 100 bytes.
  - Now 100 records will fit in fully. But we're left with 24 bytes.
  - In unspanned, we'll let that space go waste.
  - In spanned, we'll use that space to fill 24 bytes of a record, the rest of the record will be stored somewhere else.
  - Today, we mostly use unspanned because of ease of implementation and speed.

# Indexing

- Lets say that we have a *Student* table, with *student_id* as the primary attribute and a few other attributes.
- Now lets say the one block of hard disk can contain 10 records of Student.
- Lets say there are 1000 records; meaning 100 blocks.
- Now, we will first of all store all the records in a sorted manner, wrt student id.
- Now we can easily find the block of a particular record by binary search.
- We can also create another **Index Table** storing `student-id` vs `block-number`.
- Its sort of an inverted index.
- Lets say that each block has 100 records. That means those 100 records will have the same block number.
- So in the index table it will be stupid to store the entries for all the 100 records as the value will be the same.
- So instead of storing student ids `[1, 2, 3, 4, ...]`,  the index table will store `[1, 101, 201, 301 ...]`.
- Of course we'll have to store each individual id if the records are not stored in sorted order.
- **Index file is always sorted no matter what to enable binary search.**
- **Sparse vs Dense Indexing**:
  - Lets say we have a list of tuples `[{1, data}, {5, data}, {4, data}, {2, data}, {4, data}]`.
  - Where id is unique and data denotes a set of non-primary attributes.
  - An inverted hash table can be used to store `id` vs `index of id in list` for fast access.
  - If we are storing every entry of a list in the inverted hash table, its called dense.
  - If we are not storing every entry, its called sparse.
  - For example, if the list of tuples is sorted wrt to some non-unique attribute `[{1, data}, {1, data}, {1, data}, {2, data}, {2, data}]`
  - Then in the inverted hash table, we can just store the entry for `1->0` and `2->3`, that is only for the first occurences.
  - This is an example of sparse indexing.
  - Dense indexes are faster but sparse are space-efficient.
  - Sparse indexes will only be possible in case of sorted records. 

## Types of Indexing

### Primary Indexing / Clustering Index

- Records are sorted based on primary key.
- Indexing based on the primary key.
- Since its sorted, sparse indexing is used.
- Will do binary search in the index table for a search.


### Secondary Indexing / Non-Clustering Index

- Records are not sorted in any way.
- Can be done on both primary and non-primary attribute.
- With a clustered index the rows are stored physically on the disk in the same order as the index. Therefore, there can be only one clustered index.
- With a non clustered index there is a second list that has pointers to the physical rows.
- You can have many non-clustered indices, although each new index will increase the time it takes to write new records.
- It is generally faster to read from a clustered index if you want to get back all the columns. You do not have to go first to the index and then to the table.
- Writing to a table with a clustered index can be slower, if there is a need to rearrange the data.
- Example of clustered - **dictionary**; No need of any other index, its already indexed according to words.
- Example of non-clustered - An index in a book. The data is stored in one place but the index is stored in another place and the index have pointers to the storage location of the data.

# Hash table vs B-Trees

- B-Trees are far more popular.
- Hash tables dont support range scans.
- Hash tables require more space.
- Hash table lookup can be more than O(1) sometimes due to collision; unacceptable in certain scenarios.
- TODO: B Trees vs B+ Trees

<https://stackoverflow.com/a/24470091/1925388>