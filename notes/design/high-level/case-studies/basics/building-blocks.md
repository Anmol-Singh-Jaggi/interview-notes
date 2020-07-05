# Famous technologies
- Amazon DynamoDB -> NoSQL -> Key value + Document
- Amazon Aurora -> Distributed MySQL.
- Amazon Redshift -> Warehousing.
- Elasticsearch -> Search.
- CDN -> Cloudflare, Akamai.
- Reverse proxy -> Nginx, HAProxy.
- Cache -> Redis, Memcached.
- Redis also supports priority queues WTF!!!!

-------

# Storing images/media
- Uses: Facebook/Whatsapp/Twitter/Instagram etc.
- Store images/videos in an object store like Amazon S3.
- Or maybe a distributed file system like HDFS.
- `/root/user1/image1.jpg`

# Notifications
- Uses: Facebook/Whatsapp/Twitter/Instagram.
- Use a websocket or XMPP protocol.
- In websockets, the HTTP connection is upgraded to a full duplex persistent channel.
- In XMPP, the underlying mechanism is BOSH protocol.
- In BOSH, the client sends a request to the server.
- The server does not send the response immediately, but rather waits till there is an event for the client.
- After the client receives the event, it immediately sends another request to wait for another event.
- In case the client wants to send some other other while its waiting for the resonse, it can open another connection to the server.
- So there are at max 2 open connections at a time between the server and the client.

# Message Queue
- Uses: Facebook/Whatsapp/Twitter
- For example, Kafka, Active MQ, RabbitMQ etc.
- Note that message queues can be used a **task queues** also.
- Lets say there are more requests to a service per second than it can handle.
- It can append all those requests to a queue.
- Multiple processing consumers can then consume the tasks at their own rate asynchronously.
- Also note that it is generally persistent, distributed and fault tolerant.
- It can be both push or pull based.
- Its great for publisher-subscriber model.

# Distributed File System
- A file system spanning over multiple machines offering a logically unified of data to the user.
- For example - HDFS, GFS
- Amazon S3 is not a file system per se; its just 'infinite object storage', with every object associated with a key.
- Nowadays, S3 is replacing HDFS.

# Service Discovery
- A **service registry** maintains the info about all the alive instances of a service using heartbeat mechanism.
- Zookeeper can be used.

# Searching
- Uses: Facebook, Twitter, basically everything..
- Have a distinct **search service**.
- Parses/tokenizes the input query, determining what needs to be searched.
- Removes markup.
- Breaks up the text into terms.
- Fixes typos.
- Normalizes capitalization.
- Converts the query to use boolean operations.
- Queries the Search Cluster for the results:
  - Scatter gathers each server in the cluster to determine if there are any results for the query.
  - Merges, ranks, sorts, and returns the results.
- Lucene is a general-purpose seach engine; basically creates an inverted index.
- Solr and Elasticsearch are built on Lucene to provide a distributed search engine server.
- Elasticsearch is more popular, although both have similar features.

# Thundering Herd
- A single system failure cascading to an entire system.
- Among 4 servers all at full capacity, one server crashes due to high load.
- Now the requests going to that server will be routed to other 3, in turn crashing them one-by-one in the same way.
- Can be avoided by consistent hashing.

 
# Quorum Read/Writes

# Distributed Database
- First shard the database based on some user attribute.
- Then for each shard, create multiple **read-replicas** and multiple **master-slave write nodes**.

# Caching
- Use caching extensively.
- Either we can have a few global caches in the system.
- Or we can have one cache for every service.
- Or both.
- Use redis or memcached.

# News Feed
- Uses: Facebook/Twitter/Insta etc.
- Separate out the read and write API.
- Create a new **Timeline service**.
- When a new post is written, add its ID it to a cache.
- For example, `cache[user1] = {tweet10, tweet15...}`.
- This list will contain the top 100 posts which should be displayed on a user's timeline.
- If user X publishes a post, and X is followed by A, B and C, then add this post id to `cache[A]`, `cache[B]` and `cache[C]`.
- This will be done by a **fanout service**.
- The relationships will be stored in a **user graph** service.
- Dont forget to write the post data in a separate database also!
- Then when a user views their timeline, get the post ids from the cache.
- Then request the actual post details(content, author, likes etc) from a separate **Post Info Service**.
- The post author tweet can be fetched from **User Info Service**.
- Notifications about a new post will be sent using a notification service.
- Sharding can either on tweet id, or on user id.


# Manage profiles
- Uses: Facebook/Twitter basically every system.
- 

# Analytics:
- How many times is a resource accessed?
- Use Amazon Redshift.

# Serving videos
- Store low, medium, high quality of every video separately.
- Partition a video into segments.
- Segmentation can be done uniformly or on the basis of content (keep an action scene together).
- Buffer the next few segments only.
- Keep checking the internet speed; if low, then switch to lower quality video.
- Store in a distributed file system or an object store.