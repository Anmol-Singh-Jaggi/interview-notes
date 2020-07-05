# Coins in prime-factor-numbered bag
- You are given a few bags of coins, initially empty.
- You will be given 2 types of queries:
  - Query type 1 -> Input = 'x': Add one coin to every ith bag where is a prime factor of x.
  - For example, if x = 10, then add one coin to bag 2 and bag 5.
  - Query type 2 -> Input = 'left right': Tell the number of coins in bags from indice left to right inclusive.
  - For example, if left, right = (1, 10), then answer would be 2 (one in 2 and other in 5).

## Solution:
- Create spf[] array (shortest prime factors).
- Then for every query type 1, prime factorize it using spf array (O(Logn)).
- Store and maintain the prime-exponent mapping in a Counter.
- For type 2 query, just iterate through the counter and sum up the exponents.
- Complexity:
  - O(n) to create spf array till 10^5.
  - O(log(n)) for query type 1.
  - O(n) for query type 2.
