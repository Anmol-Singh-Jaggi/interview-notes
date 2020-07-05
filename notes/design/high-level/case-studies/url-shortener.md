# Features
- getShortLink(long_url)
- getLongLink(short_url)
- Expiry time.
- Unique ID generation.
- Deleting short url.


# Traffic and data estimation
??


# Getting short link
- We can convert the long url string to an integer first.
- We can take the help of a ID generation service for that (described in other file).
- Then in the database, we can insert a mapping of short url to long url.
- Note that this will generate different short urls for even the same long url, if we are using auto-incrementing id.
- This is generally a good thing, however if we dont want it, then we can also store an inverse mapping of long url to short url.


# Getting long URL.
- Just check the database to search for the short url.


# Expiry time.
- We can have a separate dedicated expiry time service for periodically deleting old entries.
- It can be scheduled to run at nights when the traffic is less.
- Or we can expire entries only at the time of the api request itself (lazy expiration).
- Note that we can easily accomodate the feature of separate expiry time per short url in this design.


# Database
- Note that we dont have any complex relational data.
- So we should use NoSQL like Cassandra or Redis or Amazon DynamoDB.

# Sharding database
- The servers can be completely stateless.
- Databases can be sharded using either range-based partitioning(keys starting with 'A' go to db1, 'B' go to db2 etc..)
- But this might result in unbalanced load distribution.
- A better approach is to use consistent hashing.

# Caching
- We can use LRU or LFU caching between DB and servers.

# Analytics
- We can use some database warehousing solutions like Amazon Redshift.

# Deleting short url
- The user can either manually delete short url mappings or they can get expired.
- We can reclaim the integer id corresponding to that key by sending that key to the id generation service.
