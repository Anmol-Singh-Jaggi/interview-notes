# Features:
- Group messaging.
- Sent/Delivered/Read receipts.
- Storing media.
- Online/Last-seen feature.

# Basic design
- Multiple servers.
- Each whatsapp user will be connected to any one of the servers.
- It will maintain a websocket connection to the user's app as soon as the app comes onlone.
- We can use consistent hashing to map between users and servers.
- Every data flow from/to user A will always be with server 1.


# Sent/Delivered/Read receipts
- Lets say User A is mapped to server 1 and user B is mapped to server2.
- A sends a message.
- It will be first stored in a database/queue containing `message_id, message_content, from, to, timestamp`.
- Then it will also be stored in a table 'Message status' `message_id, status, status_timestamp`, where status will be 'Delivered' in the beginning.
- As soon as the db insert succeeds, we will send a reply back to client saying that message is sent successfully.
- Now server 1 forwards the message to server 2.
- Server 2 registers the message again in its queue signifying that this message has not yet been delivered.
- It will deliver it as soon as the user comes back online.
- On the other hand, if the user is online right now, then it will send the message to the user B right away.
- As soon as it gets a response, it will mark the message as 'Delivered' and update the message status.
- When B reads it, status will become 'Read'.

# Storing media
- Same as storing images in Tinder case-study.

# Online/Last-Seen feature.
- There can be a **Last-Seen Service**.
- Every time the user does an activity, a signal is sent to the last-seen service.
- If last-seen is less than say, 10 seconds, that means they are probably online.
- We can use redis to maintain a hash map of user vs last-seen.

# Group messaging
- A new **Group service** will maintain the mapping between a group and a user.
- Every group has a message queue with a publisher-subscriber model.
- Lets say a group G1 contains users A, B, C.
- A sends a message. It will go to server 1 (server that was mapped to A).
- Then server 1 will query group service message to know who else is there in the group.
- Then it will forward this message to everyone else.
- The same mechanism as a one-to-one chat would apply mostly.
