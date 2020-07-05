## You are given an array of 8 numbers. Find the second min using least number of comparisons.

- One approach can be to first find the smallest in 7 comparisons, and then again second smallest in 6 comparisons.
- 7 comparisons because `let min = arr[0]...Compare with 7 remaining numbers`.
- So, in general for an array of length k, we need k-1 comparisons to find the smallest.
- So the total answer = 7 + 6 = 13.
- But what if we compare the numbers pairwise in a tournament tree fashion?
- Compare index 0 with 1, 2 with 3 and so on.. We will be left with 4 numbers.
- Repeat the same algo till we find the winner.
- There will be log(8) = 3 such tournaments.
- Now what if we store all the numbers that competed directly against the winner in a separate array?
- There will be one such number in every round of the tournament (Because every index fights with just one other index in a round).
- We can be sure that the second min must be present in this array (because it would win over every other number and compete against min eventually).
- We can simply apply our original algo in this array, which will take log(8)-1 = 3 - 1 = 2 comparisons.
- So total = 7 + 2 = 9 comparisons.
- Note that many people think that second min would reach till the last tournament always, but no.
- It could happen that index 0 is min and index 1 is second min, meaning that second min will not even reach the second round.
- In general, the answer for a list of size n = `n - 1 + log(n) - 1`.

## Defective box ball Weighing puzzle
- You are given 10 boxes with 10 balls each.
- Every ball weighs 1 kg except the ones in a certain box.
- Meaning that, say, box 8 might have 10 balls of 2 kg each.
- You can weigh multiple balls at the same time in a weighing machine.
- You need to find out the defective box in minimum number of weighings.

# SOLUTION 1:
- Take one ball from each box and weigh it one at a time to directly find out the defective ball.
- It will take 10 weighings in total.
- Answer = 10.

# SOLUTION 2:
- Lets say we divide the 10 boxes into 2 batches of 5.
- We can weigh both once; it might happen that in the first weighing itself, its weight is something other than 5 kg.
- But we will have to consider the worst case obviously.
- It turns out that first batch weighs 5 kg, meaning that defective piece is in other batch.
- So, we can run this algo in the second batch recursively.
- f(10) = 1 + f(5)
- f(5) = 1 + f(2)
- f(2) = 1
- Meaning f(10) = 3.
- So ans = 3

# SOLUTION 3:
- We can take 1 ball from each box and weigh them.
- Lets say the weight is 12 kg.
- This means that the difference in weight of the defective ball = 12 - 10 = 2kg.
- Now take 1 ball from box1, 2 from box2, ... 10 from box10 and weigh them.
- Their sum should have been 55 but lets say its 55 + x.
- Our answer would be x / 2, or x / y where y is the diff between normal and defective weight.
- So ans = 2.
