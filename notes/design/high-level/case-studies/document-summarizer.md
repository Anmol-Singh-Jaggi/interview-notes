We have a service which takes a document of max size 100KB as input and returns a short summary of it.
The summarization service is a bit slow (5 seconds for a document on average).
How to scale?

Short answer:

- Use async processing since the summarization takes a lot of time.
- We can use Kafka in which the app servers will insert the documents into.
- Then multiple services will consume that.

