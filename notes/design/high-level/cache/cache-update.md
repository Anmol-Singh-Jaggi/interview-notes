# Caching

## Types of caching based on the layer

- Client caching (browser).
- CDN caching.
- Web server caching (reverse proxies).
- Database builtin caching.
- Application caching (Memcached/Redis).

## DB caching

- Row level.
- Query-level.
  - Whenever you query the database, hash the query as a key and store the result to the cache.
  - This approach suffers from expiration issues:
  - Hard to delete a cached result with complex queries.
  - If one piece of data changes such as a table cell, you need to delete all cached queries that might include the changed cell.
- Fully-formed serializable objects.
  - See your data as an object, similar to what you do with your application code.
  - Have your application assemble the dataset from the database into a class instance or a data structure.
  - Remove the object from cache if its underlying data has changed.
  - Allows for asynchronous processing: workers assemble objects by consuming the latest cached object.

## Cache Update Strategies

### Cache-aside

![Cache Aside updation strategy](assets/cache-aside.png)

- The application is responsible for reading and writing from storage.
- The cache does not interact with storage directly.
- The application does the following:
  - Look for entry in cache, resulting in a cache miss.
  - Load entry from the database.
  - Add entry to cache.
  - Return entry.
- Example - Memcached.
- Subsequent reads of data added to cache are fast.
- Also referred to as lazy loading.
- Only requested data is cached, which avoids filling up the cache with data that isn't requested.

**Disadvantages**:

- Each cache miss results in three trips, which can cause a noticeable delay.
- Data can become stale if it is updated in the database.
- This issue is mitigated by setting a time-to-live (TTL) which forces an update of the cache entry, or by using write-through.
- When a node fails, it is replaced by a new, empty node, increasing latency.


### Read-Through

- Same as cache aside, but in case of a cache miss, the cache will fetch from db and update itself.

### Write-through

![Write through cache updation strategy](assets/write-through.png)

- The application uses the cache as the main data store, reading and writing data to it, while the cache is responsible for reading and writing to the database:
  - Application adds/updates entry in cache.
  - Cache synchronously writes entry to data store
- Write-through is a slow overall operation due to the write operation, but subsequent reads of just written data are fast.
- Users are generally more tolerant of latency when updating data than reading data.
- Data in the cache is never stale.

**Disadvantages**:

- When a new node is created due to failure or scaling, the new node will not cache entries until the entry is updated in the database.
- Cache-aside in conjunction with write through can mitigate this issue.
- Most data written might never be read, which can be minimized with a TTL.

### Write-behind

- Same as write-through, but the write to the db will happen asynchronously.

### Refresh-Ahead

![Refresh-ahead cache updation strategy](assets/refresh-ahead.png)

- You can configure the cache to automatically refresh any recently accessed cache entry prior to its expiration.
- Refresh-ahead can result in reduced latency vs read-through if the cache can accurately predict which items are likely to be needed in the future.

**Disadvantages**:

- Not accurately predicting which items are likely to be needed in the future can result in reduced performance than without refresh-ahead.