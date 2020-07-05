'''
Get count of the nodes in the first list, let count be c1.
Get count of the nodes in the second list, let count be c2.
Get the difference of counts d = abs(c1 – c2)
Now traverse the bigger list from the first node till d nodes so that from here onwards both the lists have equal no of nodes.
Then we can traverse both the lists in parallel till we come across a common node.
(Note that getting a common node is done by comparing the address of the nodes)
'''
