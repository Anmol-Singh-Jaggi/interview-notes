# NoSQL

As you can see, there are three primary concerns you must balance when choosing a data management system: consistency, availability, and partition tolerance.

    Consistency means that each client always has the same view of the data.
    Availability means that all clients can always read and write.
    Partition tolerance means that the system works well across physical network partitions.

According to the CAP Theorem, you can only pick two. So how does this all relate to NoSQL systems?

One of the primary goals of NoSQL systems is to bolster horizontal scalability. To scale horizontally, you need strong network partition tolerance which requires giving up either consistency or availability. NoSQL systems typically accomplish this by relaxing relational abilities and/or loosening transactional semantics.

In addition to CAP configurations, another significant way data management systems vary is by the data model they use: relational, key-value, column-oriented, or document-oriented (there are others, but these are the main ones).

    Relational systems are the databases we've been using for a while now. RDBMSs and systems that support ACIDity and joins are considered relational.
    Key-value systems basically support get, put, and delete operations based on a primary key.
    Column-oriented systems still use tables but have no joins (joins must be handled within your application). Obviously, they store data by column as opposed to traditional row-oriented databases. This makes aggregations much easier.
    Document-oriented systems store structured "documents" such as JSON or XML but have no joins (joins must be handled within your application). It's very easy to map data from object-oriented software to these systems.

Now for the particulars of each CAP configuration and the systems that use each configuration:

Consistent, Available (CA) Systems have trouble with partitions and typically deal with it with replication. Examples of CA systems include:

    Traditional RDBMSs like Postgres, MySQL, etc (relational)
    Vertica (column-oriented)
    Aster Data (relational)
    Greenplum (relational)

Consistent, Partition-Tolerant (CP) Systems have trouble with availability while keeping data consistent across partitioned nodes. Examples of CP systems include:

    BigTable (column-oriented/tabular)
    Hypertable (column-oriented/tabular)
    HBase (column-oriented/tabular)
    MongoDB (document-oriented)
    Terrastore (document-oriented)
    Redis (key-value)
    Scalaris (key-value)
    MemcacheDB (key-value)
    Berkeley DB (key-value)

Available, Partition-Tolerant (AP) Systems achieve "eventual consistency" through replication and verification. Examples of AP systems include:

    Dynamo (key-value)
    Voldemort (key-value)
    Tokyo Cabinet (key-value)
    KAI (key-value)
    Cassandra (column-oriented/tabular)
    CouchDB (document-oriented)
    SimpleDB (document-oriented)
    Riak (document-oriented)



Redis (V3.2)

    Written in: C
    Main point: Blazing fast
    License: BSD
    Protocol: Telnet-like, binary safe
    Disk-backed in-memory database,
    Master-slave replication, automatic failover
    Simple values or data structures by keys
    but complex operations like ZREVRANGEBYSCORE.
    INCR & co (good for rate limiting or statistics)
    Bit and bitfield operations (for example to implement bloom filters)
    Has sets (also union/diff/inter)
    Has lists (also a queue; blocking pop)
    Has hashes (objects of multiple fields)
    Sorted sets (high score table, good for range queries)
    Lua scripting capabilities
    Has transactions
    Values can be set to expire (as in a cache)
    Pub/Sub lets you implement messaging
    GEO API to query by radius (!) 

Best used: For rapidly changing data with a foreseeable database size (should fit mostly in memory).

For example: To store real-time stock prices. Real-time analytics. Leaderboards. Real-time communication. And wherever you used memcached before.
Cassandra (2.0)

    Written in: Java
    Main point: Store huge datasets in "almost" SQL
    License: Apache
    Protocol: CQL3 & Thrift
    CQL3 is very similar to SQL, but with some limitations that come from the scalability (most notably: no JOINs, no aggregate functions.)
    CQL3 is now the official interface. Don't look at Thrift, unless you're working on a legacy app. This way, you can live without understanding ColumnFamilies, SuperColumns, etc.
    Querying by key, or key range (secondary indices are also available)
    Tunable trade-offs for distribution and replication (N, R, W)
    Data can have expiration (set on INSERT).
    Writes can be much faster than reads (when reads are disk-bound)
    Map/reduce possible with Apache Hadoop
    All nodes are similar, as opposed to Hadoop/HBase
    Very good and reliable cross-datacenter replication
    Distributed counter datatype.
    You can write triggers in Java. 

Best used: When you need to store data so huge that it doesn't fit on server, but still want a friendly familiar interface to it.

For example: Web analytics, to count hits by hour, by browser, by IP, etc. Transaction logging. Data collection from huge sensor arrays.
MongoDB (3.2)

    Written in: C++
    Main point: JSON document store
    License: AGPL (Drivers: Apache)
    Protocol: Custom, binary (BSON)
    Master/slave replication (auto failover with replica sets)
    Sharding built-in
    Queries are javascript expressions
    Run arbitrary javascript functions server-side
    Geospatial queries
    Multiple storage engines with different performance characteristics
    Performance over features
    Document validation
    Journaling
    Powerful aggregation framework
    On 32bit systems, limited to ~2.5Gb
    Text search integrated
    GridFS to store big data + metadata (not actually an FS)
    Has geospatial indexing
    Data center aware 

Best used: If you need dynamic queries. If you prefer to define indexes, not map/reduce functions. If you need good performance on a big DB. If you wanted CouchDB, but your data changes too much, filling up disks.

For example: For most things that you would do with MySQL or PostgreSQL, but having predefined columns really holds you back.
ElasticSearch (0.20.1)

    Written in: Java
    Main point: Advanced Search
    License: Apache
    Protocol: JSON over HTTP (Plugins: Thrift, memcached)
    Stores JSON documents
    Has versioning
    Parent and children documents
    Documents can time out
    Very versatile and sophisticated querying, scriptable
    Write consistency: one, quorum or all
    Sorting by score (!)
    Geo distance sorting
    Fuzzy searches (approximate date, etc) (!)
    Asynchronous replication
    Atomic, scripted updates (good for counters, etc)
    Can maintain automatic "stats groups" (good for debugging) 

Best used: When you have objects with (flexible) fields, and you need "advanced search" functionality.

For example: A dating service that handles age difference, geographic location, tastes and dislikes, etc. Or a leaderboard system that depends on many variables.



CouchDB (V1.2)

    Written in: Erlang
    Main point: DB consistency, ease of use
    License: Apache
    Protocol: HTTP/REST
    Bi-directional (!) replication,
    continuous or ad-hoc,
    with conflict detection,
    thus, master-master replication. (!)
    MVCC - write operations do not block reads
    Previous versions of documents are available
    Crash-only (reliable) design
    Needs compacting from time to time
    Views: embedded map/reduce
    Formatting views: lists & shows
    Server-side document validation possible
    Authentication possible
    Real-time updates via '_changes' (!)
    Attachment handling
    thus, CouchApps (standalone js apps) 

Best used: For accumulating, occasionally changing data, on which pre-defined queries are to be run. Places where versioning is important.

For example: CRM, CMS systems. Master-master replication is an especially interesting feature, allowing easy multi-site deployments.
Accumulo (1.4)

    Written in: Java and C++
    Main point: A BigTable with Cell-level security
    License: Apache
    Protocol: Thrift
    Another BigTable clone, also runs of top of Hadoop
    Originally from the NSA
    Cell-level security
    Bigger rows than memory are allowed
    Keeps a memory map outside Java, in C++ STL
    Map/reduce using Hadoop's facitlities (ZooKeeper & co)
    Some server-side programming 

Best used: If you need to restict access on the cell level.

For example: Same as HBase, since it's basically a replacement: Search engines. Analysing log data. Any place where scanning huge, two-dimensional join-less tables are a requirement.
HBase (V0.92.0)

    Written in: Java
    Main point: Billions of rows X millions of columns
    License: Apache
    Protocol: HTTP/REST (also Thrift)
    Modeled after Google's BigTable
    Uses Hadoop's HDFS as storage
    Map/reduce with Hadoop
    Query predicate push down via server side scan and get filters
    Optimizations for real time queries
    A high performance Thrift gateway
    HTTP supports XML, Protobuf, and binary
    Jruby-based (JIRB) shell
    Rolling restart for configuration changes and minor upgrades
    Random access performance is like MySQL
    A cluster consists of several different types of nodes 

Best used: Hadoop is probably still the best way to run Map/Reduce jobs on huge datasets. Best if you use the Hadoop/HDFS stack already.

For example: Search engines. Analysing log data. Any place where scanning huge, two-dimensional join-less tables are a requirement. 

## MongoDB

## Redis

## DynamoDB

## Cassandra

## CouchDB

## Neo4j

Neo4j (V1.5M02)

    Written in: Java
    Main point: Graph database - connected data
    License: GPL, some features AGPL/commercial
    Protocol: HTTP/REST (or embedding in Java)
    Standalone, or embeddable into Java applications
    Full ACID conformity (including durable data)
    Both nodes and relationships can have metadata
    Integrated pattern-matching-based query language ("Cypher")
    Also the "Gremlin" graph traversal language can be used
    Indexing of nodes and relationships
    Nice self-contained web admin
    Advanced path-finding with multiple algorithms
    Indexing of keys and relationships
    Optimized for reads
    Has transactions (in the Java API)
    Scriptable in Groovy
    Clustering, replication, caching, online backup, advanced monitoring and High Availability are commercially licensed 

Best used: For graph-style, rich or complex, interconnected data.

For example: For searching routes in social relations, public transport links, road maps, or network topologies. 

https://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis

# Lucene and Solr
