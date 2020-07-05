# Telephone Round:

## PROBLEM 1:
next permutation with same digits.

## PROBLEM 2:
Given an array, find a pair whose sum is equal to target.

------------
------------
------------

# ROUND 1:

## PROBLEM 1:
Design a data structure supporting following operations for integers:
getMin()
getMax()
insert()
delete()

Note that multiple entries for the same integer are allowed.
While deleting, if the frequency of a number is more than 1, then just decrement the count.

### SOLUTION 1:
- Use hash-map of `<number> vs <frequency>`.
- insert() and delete() are O(1).
- getMin() and getMax() will be O(n) since we will be iterating through the whole hashmap.

### SOLUTION 2:
- Use the above hash-map as well as a min-heap and max-heap.
- insert() and delete() will become O(logn), but getMin() will be O(1)
- We can use Fibonacci heaps to get to O(1) from O(logn)

### SOLUTION 3:
- Use the above hash-map as well as a BST.
- Same complexities as above.

### SOLUTION 4:
- Use the above hash-map + maintain a sorted doubly linked-list.
- delete(), getMin(), getMax() will be O(1), but insert() will be O(n).

------------

## PROBLEM 2:
- You are given a matrix where each cell has a character from 'a' to 'z'.
- You have to reach (n,n) from (0,0).
- And the path you choose should be lexicographically smallest after sorting of all the possible paths.
- For example, if there are 2 paths 'cbaab' and 'abcdb', the first path is preferable.

### SOLUTION:
- Start from bottom-right to top-left and apply DP.
- For a cell(i,j), consider 2 paths - one for (i+1,j) and one for (i, j+1); answers for both will be precomputed by the time we reach (i,j).
- The answers can always be stored in a char frequency map of size 26.
- Now just compare these 2 answers and add `matrix[i][j]` to the lexicographically smallest answer.
- Comparing will be O(1) since we are comparing 2 hash-maps of size 26.
- Note that for every cell, we are comparing just 2 possible paths and taking the best.

------------

## PROBLEM 3:
- You are given queries of the form (u, v) where u and v are integers and u < v.
- For each query, return the number within that range with the maximum number of divisors.
- For example: u,v = 2, 7.
- Answer = 6 (4 divisors).
- Max possible value of v = 10^7.

### SOLUTION 1:
- Just prime factorize every number in the range.
- If prime factorization = p1^x1 * p2^x2 * p3^x3, then number of divisors = (x1+1)*(x2+1)*(x3+1)...
- And then choose the max of them.
- Complexity -> O((v-u) * sqrt(v))

### SOLUTION 2:
- Use something like sieve of eratosthenes to precompute the prime factorization for all numbers till 10^7 in O(nlogn).
- Then for each query, just iterate through the range and return the max in O(v-u).
- Alternatingly, create a seg tree and it will be O(logn).

------------
------------
------------

# ROUND 2:

## PROBLEM 1:
- Given a set of URL mappings with patterns, how will you match the URL to the pattern??
- For example, lets say we have the following mappings:
  - GET, /orders/prices, foo1()
  - GET, /orders/:id:/, foo2()
  - POST, /persons/:id:/orders/:id:, foo3()
- Explanation:
  - `foo1()` is the function to be called on hitting the URL "GET, /orders/prices".
- Given an input like `<GET, "/persons/12/orders/5">`, you should return "foo3()".

### SOLUTION:
- Create a trie of all the input mappings.
- For example, in case of <GET, /orders/prices, foo1()>, the trie will look like:
- Root -> GET -> orders -> prices
- And the "prices" node will have the function object foo1() mapped to it.
- For <POST, /persons/:id:/orders/:id:, foo3()>, the trie will look like:
- Root -> POST -> persons -> $$ -> orders -> $$
- Then when given an input like "POST, /persons/12/orders/5", we will just iterate through the trie and return the function mapped to the end node.
- Note that while traversing down the trie, if at any point we reach a dead-end, we should explore the $$ branch also.
- But the above solution misses 1 edge case:
- Mappings `GET /xyz/abc, foo1()` and `GET /xyz/:id:/def, foo2()` and the input `GET /xyz/abc/def`.
- By the above algorithm we will first visit "xyz", then "abc", then reach dead end and return null.
- But we should have explored the other $$ branch also.
- So, we will have to write a recursive function in which explore a child branch; if that branch returns None, then we explore `$$` branch also if present.

------------
------------

# ROUND 3:

## PROBLEM 1:
- Design bowling alley (low-level).
- It should easily accomodate custom scoring strategies (for example, if the player hits pins equal to some 'number of the day', then he should get bonus points).
- It should also be possible to apply multiple scoring strategies at the same time in complex ways.
- Follow-up: Create multithreaded code for this.
- Follow-up: How does Concurrent Hash Map works?

### SOLUTION:
Use Strategy + Chain of responsibility patterns.

------------
------------

# ROUND 4:

Hiring manager round bs.