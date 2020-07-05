# Features
- Send a friend request.
- Accept a friend request.
- User searches for someone and sees the shortest path to the searched person.
- Find new connections.
- Groups.


# Basics
- User graph service.
- Graph will be too big to hold in memory at once.
- Can shard by user location.

# Send a friend request
- Can maintain a table `Requests - {sender, receiver}`.
- Can be handled by **User-Graph service**.

# Accept a friend request.
- Can maintain a table `Friends - {user1, user2}`.
- Handled by user graph service.

# Find new connections.
- From the friends table, find out all the friends (1st degree connections).
- Then in a BFS fashion, find out 2nd or max 3rd degree connections and show them.

# Search for someone.
- Do a BFS in the graph.
- Will have to load the graph incrementally.
- But BFS will ultimately lead to loading everything in memory.
- Better to do a bidirectional BFS.
- Read this please - <https://www.geeksforgeeks.org/design-data-structures-for-a-very-large-social-network-like-facebook-or-linkedln/>.

# Groups.
- A groups service and database `Groups - {group_id, member_id}`.

![](assets/social-graph1.png)  
![](assets/social-graph2.png)  