[Source1](http://ksat.me/a-plain-english-introduction-to-cap-theorem/).  
[Source2](https://en.wikipedia.org/wiki/CAP_theorem).

- **Consistency:** Every read receives the most recent write or an error
- **Availability:** Every request receives a (non-error) response – without the guarantee that it contains the most recent write
- **Partition Tolerance:** The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes.
- **Eventual Consistency:** Every read receives the most recent write, after a specified time!
* When you are designing a distributed system you can get cannot achieve all three of Consistency, Availability and Partition tolerance. You can pick only two.
* Meaning, there can only be 3 types of system: AC, AP and CP.
* No distributed system is safe from network failures, thus network partitioning generally has to be tolerated.
* In the presence of a partition, one is then left with two options: consistency or availability.
* When choosing consistency over availability, the system will return an error or a time-out if particular information cannot be guaranteed to be up to date due to network partitioning.
* When choosing availability over consistency, the system will always process the query and try to return the most recent available version of the information, even if it cannot guarantee it is up to date due to network partitioning.
* In the absence of network failure – that is, when the distributed system is running normally – **both availability and consistency can be satisfied**.
* CAP is frequently misunderstood as if one has to choose to abandon one of the three guarantees at all times. In fact, the choice is really between consistency and availability only when a network partition or failure happens; at all other times, no trade-off has to be made.
* What it means is that AC and CP are essentially the same (dropping A only when P happens).
* This means only 2 types of systems: CP and AP.
* Database systems designed with traditional ACID guarantees in mind such as RDBMS choose consistency over availability, whereas systems designed around the BASE philosophy, common in the NoSQL movement for example, choose availability over consistency.

# PACELC theorem

It states that in case of network partitioning (P) in a distributed computer system, one has to choose between availability (A) and consistency (C) (as per the CAP theorem), but else (E), even when the system is running normally in the absence of partitions, one has to choose between latency (L) and consistency (C).