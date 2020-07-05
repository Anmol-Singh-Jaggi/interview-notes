# Features:
- Find nearby restaurants given an input coordinate.
- Add new restaurants to the database.
- Add reviews to the restaurants.

# Basics
- The hard problem is finding nearby places, rest is easy.

# Option 1 (RDBMS)
- We can store all the data of a city in 1 shard.
- While finding nearby restaurants given an input location (X, Y) and radius D, execute a query like:

```
Select * from Restaurants where Latitude between X-D and X+D and Longitude between Y-D and Y+D
# Note that this is actually a square and not a circle.
```

# Option 2 (Fixed-size grids)
- We can divide the world into 1x1 Km grids.
- We can then search only in the neaby grids.

```
Select * from Places where Latitude between X-D and X+D and Longitude between Y-D and Y+D and GridID in (GridID, GridID1, GridID2, ..., GridID8)
```

# Option 3 ( Dynamic Grids)
- Let’s assume we don’t want to have more than 500 places in a grid so that we can have a faster searching.
- So, whenever a grid reaches this limit, we break it down into four grids of equal size and distribute places among them.
- This means thickly populated areas like downtown San Francisco will have a lot of grids, and sparsely populated area like the Pacific Ocean will have large grids with places only around the coastal lines.
- What data-structure can hold this information? A tree in which each node has four children can serve our purpose.
- Each node will represent a grid and will contain information about all the places in that grid.
- If a node reaches our limit of 500 places, we will break it down to create four child nodes under it and distribute places among them.
- In this way, all the leaf nodes will represent the grids that cannot be further broken down. So leaf nodes will keep a list of places with them.
- This tree structure in which each node can have four children is called a QuadTree.

## Building quad tree
- How will we build a QuadTree?
- We will start with one node that will represent the whole world in one grid.
- Since it will have more than 500 locations, we will break it down into four nodes and distribute locations among them.
- We will keep repeating this process with each child node until there are no nodes left with more than 500 locations.

# Searching for a grid
- How will we find the grid for a given location?
- We will start with the root node and search downward to find our required node/grid.
- At each step, we will see if the current node we are visiting has children.
- If it has, we will move to the child node that contains our desired location and repeat this process.
- If the node does not have any children, then that is our desired node.

# Finding neighbouring places
- How will we find neighboring grids of a given grid?
- Since only leaf nodes contain a list of locations, we can connect all leaf nodes with a doubly linked list.
- This way we can iterate forward or backward among the neighboring leaf nodes to find out our desired locations.
- Another approach for finding adjacent grids would be through parent nodes.
- We can keep a pointer in each node to access its parent, and since each parent node has pointers to all of its children, we can easily find siblings of a node.
- We can keep expanding our search for neighboring grids by going up through the parent pointers.
- Once we have nearby LocationIDs, we can query the backend database to find details about those places.

# Final search flow
- What will be the search workflow? We will first find the node that contains the user’s location.
- If that node has enough desired places, we can return them to the user.
- If not, we will keep expanding to the neighboring nodes (either through the parent pointers or doubly linked list) until either we find the required number of places or exhaust our search based on the maximum radius.

# Sharding
- Actually even with a lot of places, all of the quad tree can fit in memory, but still...

## Sharding based on city.
- We can store different quad trees for different cities.

## Sharding based on location ID.
- Restaurants will be randomly distributed on different quad trees.
- We will have to aggregate all the results from all the machines for the query 'Get nearby restaurants from the location (x, y)'.


# Ranking
- We can do ranking based on the reviews.
