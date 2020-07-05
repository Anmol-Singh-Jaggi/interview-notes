'''
Construct the sequence arr[1], arr[2], ... by the following rules.
For i=1 we put arr[1]=1.
Now let i >= 2.
Then arr[i] is the least positive integer such that the following two conditions hold:

(i) arr[i] > arr[i - 1];
(ii) for all k, j < i we have arr[i] is not equal to n1 * arr[k] - n2 * arr[j].

Find the first n terms of this sequence.

EXAMPLE:

n1=2, n2=1, n=10
Answer:
1 2 4 5 10 11 13 14 28 29

n1=2, n2=1, n=10
Answer:
1 2 3 4 5

n1=4, n2=2, n=4
Answer:
1 3 4 5

SOLUTION:
Finding arr[k] at each step directly by definition is very slow.
Let's do the following.
After we find some arr[k], let's mark all numbers greater than arr[k] that definitely can't be the future elements of this sequence.
What are these numbers?

Clearly that all numbers of the form n1 * arr[i] - n2 * arr[j] where 1 <= i, j <= k can't be the elements of this sequence.
But all other numbers possibly can belong to this sequence until we find the next element.
The element arr[k] bring us the following numbers that was not marked earlier: n1 * arr[k] - n2 * arr[i] for 1 <=i <=k and n1 * arr[i] - n2 * arr[k] for 1 <=i < k.
So we need to mark only these 2 * k - 1 numbers at kth step.
The finding of arr[k] now becomes easy.
We just need to iterate through all numbers greater than arr[k - 1] until we find not marked number.
This number is equal to arr[k].

Some additional hints:
Don't forget to mark a - b before finding arr[2].
Take some bound for numbers that will be marked.
We don't need to mark numbers greater than arr[n].
Of course we don’t know it. But we can estimate it.
Since at each step we mark at most 2 * k - 1 new numbers it follows that arr[k+1] <= arr[k] + 2 * k - 1.
And hence arr[n] <= 1 + 1 + 3 + 5 + ... + (2 * n - 3) = (n - 1)2 + 1.
Thus we can mark only numbers that is not greater than (n - 1)2 + 1.
In fact you don't need all this stuff and simply can mark all numbers using array with one million elements.
Thus we obtain algorithm with complexity O(n2).
'''
