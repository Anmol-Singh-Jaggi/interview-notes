# Microservices

- A suite of independently deployable, small, modular services.
- Each service runs a unique process and communicates through a well-defined, lightweight mechanism to serve a business goal.
- Pinterest, for example, could have the following microservices: user profile, follower, feed, search, photo upload, etc.

## Benefits
- Faster delivery because of smaller changes.
- Isolation; one crash will not affect others.
- Scaling; Can scale individual services.
- Culture; Well defined ownership;
- Flexibility; Each service can use its own tech.

## Limitations of microservices

- With lack of documentation a team implementing service X which should be using service of team Y has unnecessary overheads of communication, general mistakes and in general bitching as to why team Y doesn’t care enough about their deadlines.
- No documented contract of the service means a central person/group cannot make sure that all the API’s follow a particular standard, leading to each team or even the same team developing different looking API contracts.
- Every time a service is being called in another service plumbing code needs to be written to integrate with the service, including models, connectors etc, if you are one of those super organized teams which churn out clients after every time a service is built for every language that other teams uses, then rule this statement out.
- Every time a contract changes slightly every team needs to be informed about the new functionality and the plumbing code needs to be updated.
- Every time an automation QA guy needs to understand the 20 services that you have he will need to sit with the relevant team to understand or force them to make a document for him, this will repeat with changes to the contract.
- For those services which are public in nature, the documentation’s test harness or try it functionality (which you should have) is always lagging from the actual service contract.

## Circuit-breaker pattern:
- Lets say service A calls service B.
- If B fails, all the calls will fail leading to unpredictable problems in A.
- As a solution, let A make a call to a 'Request Interceptor', which will monitor B.
- If, lets say 70% of requests to B are failing (maybe because of overload), then mark B as unhealthy and return a default error msg to A.
- It will also check for health of B after a certain timeout.
- Lets say A, B and C call D.
- If D is overloaded and becomes slow, then A, B and C will also become slow, which will in turn might make other services slow.
- To prevent this cascading failures, we basically block/limit all the calls to D for some time.

## Bulkhead patern:
- Bulkhead terminology is used in ship building to ensure that if one bulkhead is sinking, the ship as a whole survives.
- Lets say service A calls B, C, and D.
- Now service A has a thread pool of size 10.
- Every request to A is done in a separate thread.
- If B is overloaded and slows down, then it might end up taking all the threads of A.
- As a solution, we limit max threads for each service (one-third for each).

## Service Discovery
- Systems such as Consul, Etcd, and Zookeeper can help services find each other by keeping track of registered names, addresses, and ports.
- Health checks help verify service integrity and are often done using an HTTP endpoint.
- Both Consul and Etcd have a built in key-value store that can be useful for storing config values and other shared data.

## API Gateway:
- Authentication.
- SSL.
- DDoS protection.
- Cache.
- Load balancer + Router.

## Canary deploys
- Deploy new feature only for 5% users to check for bugs.

## Readings
- https://www.confluent.io/blog/data-dichotomy-rethinking-the-way-we-treat-data-and-services/
- https://docs.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis
- https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html