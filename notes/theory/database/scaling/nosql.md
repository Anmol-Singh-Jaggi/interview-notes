# NoSQL

- Data is denormalized, and joins are generally done in the application code.
- Most NoSQL stores lack true ACID transactions and favor eventual consistency.

## Types

- Key-value: Basically a hash-map. Could store the keys in sorted order also. -> Redis
- Document: Basically a hash-map with documents(XML/JSON/binary) as values. -> Mongo
- Column store: Stores data in a `super-document`. -> Cassandra
- Graph database: Stores data in the form of a graph. -> Neo4j

## NoSQL BASE

- The BASE acronym was defined by Eric Brewer, who is also known for formulating the CAP theorem.
- The CAP theorem states that a distributed computer system cannot guarantee all of the following three properties at the same time:

  - Consistency
  - Availability
  - Partition tolerance

- A BASE system gives up on consistency.
- **Basically available** indicates that the system does guarantee availability (most of the time :p), in terms of the CAP theorem.
- **Soft state** indicates that the state of the system may change over time, even without input. This is because of the eventual consistency model.
- **Eventual consistency** indicates that the system will become consistent over time, given that the system doesn't receive input during that time.

--------------------------------------------------------------------------------

# SQL vs NoSQL

## Reasons for SQL:

- Structured data.
- Strict schema.
- Relational data.
- Need for complex joins.
- Transactions.
- Clear patterns for scaling.
- More established: developers, community, code, tools, etc.
- Lookups by index are very fast.

## Reasons for NoSQL:

- Semi-structured data.
- Dynamic or flexible schema.
- Non-relational data.
- No need for complex joins.
- Store many TB (or PB) of data.
- Very data intensive workload.
- Very high throughput for IOPS.

## Sample data well-suited for NoSQL:

- Rapid ingest of clickstream and log data.
- Leaderboard or scoring data.
- Temporary data, such as a shopping cart.
- Frequently accessed ('hot') tables.
- Metadata/lookup tables.
