# Features:
- Store profiles/images.
- Authentication.
- Recommend matches.
- Remember matches.
- Direct messaging.


# Storing profile/images.
- Each user might have a max of 5 images.
- Option 1: Store as a blob.
- Option 2: Store in the filesystem.
- File preferred over blob. Why?
- In case of images, we dont need mutability, ACID, indexing etc.
- But we do need access control.
- We can store the images as `/root/<userId>/<imageId>.jpg`. This is called partitioning.
- Filesystem would be cheaper and faster.
- We can also serve images over a CDN, since an image will never change ever.
- In the db, we can instead just store the image file URL.
- We will use a distributed file system.

# Authentication
- Use Oauth2.
- Every API request will contain the token.
- Clients will interact with a **Gateway service**.
- Gateway service will redirect all the requests to the **Authentication Service**.
- If auth successful, then gateway service will redirect the request to the appropriate internal services.


# Recommender
- We can shard the database based on their location, age, gender etc.
- We can use Cassandra/Dynamo.

# Matches
- We can have a matcher service.
- It can be a key-value store (`user1 -> <user2, user3, ...>`)

# Direct messaging.
- Use XMPP or websockets.