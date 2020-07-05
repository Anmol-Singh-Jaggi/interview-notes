'''
We have a buffer of size k and an infinite stream of objects coming in.
Our aim is to maintain that buffer such that every element has an equal probability of being selected.

SOLUTION:

When we are seeing the first item, we can simply push it to the buffer.
We can keep simply pushing elements into the buffer as long as n <= k.
The probability of each of them being selected would be = 1.
But when the buffer is full, how do we decide whether to put it in the buffer or not by replacing someone else??

At the nth element, we can generate x = rand(n).
If x <= k, then replace buffer[x] with the new element.
For example k=10.
Now we get 11th element.
Probability of 11th item being selected = 10/11.
Probability of 10th item being kept in the buffer = Probability of 10th item selected in the buffer * probability of 11th item not replacing 10th item.
 = 1 * 10/11 = 10/11.
Similarly for every element in buffer, prob = 10/11.

Now 12th element comes. Its prob = 10/12.
Prob(11) = Prob of 11th item selected * Prob of 12th item not replacing 11th item
 = (10/11) * (11/12) = (10/12).
Similarly for every element, prob = 10/12

Hence, it can be shown that when we have processed n items, the prob of each item of being present in the buffer = k / n.

One more fantastic explanation:
https://qr.ae/TWsZtZ
https://youtu.be/A1iwzSew5QY
'''
