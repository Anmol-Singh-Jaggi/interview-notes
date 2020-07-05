'''
Since the normal sieve takes O(n) space which can be a problem, we can sieve in segments.
We first generate all the primes <= sqrt(n) using normal sieve.
Then we segment the rest of the range in size sqrt(n) such that the number of segments
is srqt(n) * sqrt(n) = n.
For each segment, we mark of all the composite numbers using the prime numbers generated
in the first step.
So time complexity would be O(sqrt(n)loglogsqrt(n)) + O(nloglogn) = same as original sieve.

NOTE:
Actually, we can use any random number as the segment size, at the minimum it can be PI(sqrt(x)),
where PI() is the the prime counting function. This is so because we already have generated and
stored this number of primes, so space complexity has anyways touched O(PI(sqrt(x))).
But still if the memory requirement is such that we dont have 2 * PI(sqrt(x)) space, then we can
further decrease the segment size.
'''
