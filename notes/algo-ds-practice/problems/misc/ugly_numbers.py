"""
Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers.
By convention, 1 is included.
Given a number n, the task is to find n’th Ugly number.

Examples:

Input  : n = 7
Output : 8

Input  : n = 10
Output : 12

Input  : n = 15
Output : 24

Input  : n = 150
Output : 5832


SOLUTION 1 (Heaps):

Add 1 to heap.
while len(ugly_nums) < n
{
    smallest = heap.pop()
    ugly_nums.append(smallest)
    for prime in [2, 3, 5]{
        heap.push(smallest*prime)
    }
}
return ugly_nums[n]

Complexity -> O(nlogn)

SOLUTION 2 (Use Dynamic Programming):
Here is a time efficient solution with O(n) extra space.
The ugly-number sequence is 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, …
Because every number can only be divided by 2, 3, 5, one way to look at the sequence is to split the sequence to three groups as below:
(1) 1×2, 2×2, 3×2, 4×2, 5×2, …
(2) 1×3, 2×3, 3×3, 4×3, 5×3, …
(3) 1×5, 2×5, 3×5, 4×5, 5×5, …

We can find that every subsequence is the ugly-sequence itself (1, 2, 3, 4, 5, …) multiply 2, 3, 5.
Then we can use similar merge method as merge sort, to get every ugly number from the three subsequence.
Every step we choose the smallest one, and move one step after.

1 Declare an array for ugly numbers:  ugly[n]
2 Initialize first ugly no:  ugly[0] = 1
3 Initialize three array index variables i2, i3, i5 to point to 1st element of the ugly array:
    i2 = i3 = i5 = 0;
4 Initialize 3 choices for the next ugly no:
    current_multiple_of_2 = ugly[i2]*2;
    current_multiple_of_3 = ugly[i3]*3
    current_multiple_of_5 = ugly[i5]*5;
5 Now go in a loop to fill all ugly numbers till n:
For (i = 1; i < n; i++ )
{
    next_ugly_no = Min(current_multiple_of_2,
                        current_multiple_of_3,
                        current_multiple_of_5);
    ugly[i] = next_ugly_no
    if (next_ugly_no == current_multiple_of_2)
    {
        i2++;
        current_multiple_of_2 = ugly[i2]*2;
    }
    if (next_ugly_no == current_multiple_of_3)
    {
        i3++;
        current_multiple_of_3 = ugly[i3]*3;
     }
     if (next_ugly_no == current_multiple_of_5)
     {
        i5++;
        current_multiple_of_5 = ugly[i5]*5;
     }

}
6.return next_ugly_no

Example:
Let us see how it works

initialize ugly[] =  | 1 |
i2 =  i3 = i5 = 0;

First iteration
   ugly[1] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
            = Min(2, 3, 5)
            = 2
   ugly[] =  | 1 | 2 |
   i2 = 1,  i3 = i5 = 0  (i2 got incremented )

Second iteration
    ugly[2] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
             = Min(4, 3, 5)
             = 3
    ugly[] =  | 1 | 2 | 3 |
    i2 = 1,  i3 =  1, i5 = 0  (i3 got incremented )

Third iteration
    ugly[3] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
             = Min(4, 6, 5)
             = 4
    ugly[] =  | 1 | 2 | 3 |  4 |
    i2 = 2,  i3 =  1, i5 = 0  (i2 got incremented )

Fourth iteration
    ugly[4] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
              = Min(6, 6, 5)
              = 5
    ugly[] =  | 1 | 2 | 3 |  4 | 5 |
    i2 = 2,  i3 =  1, i5 = 1  (i5 got incremented )

Fifth iteration
    ugly[4] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
              = Min(6, 6, 10)
              = 6
    ugly[] =  | 1 | 2 | 3 |  4 | 5 | 6 |
    i2 = 3,  i3 =  2, i5 = 1  (i2 and i3 got incremented )

Will continue same way till I < n
Complexity -> O(n)

NOTE: The above algos are also valid for 'super-ugly' numbers (that is for the general case).
See code for more info.
"""


def get_ugly_numbers(size):
    ugly_nums = [None] * size
    ugly_nums[0] = 1
    i2 = i3 = i5 = 0
    current_multiple_of_2 = 2
    current_multiple_of_3 = 3
    current_multiple_of_5 = 5
    for i in range(1, size):
        ugly_nums[i] = min(current_multiple_of_2, current_multiple_of_3, current_multiple_of_5)
        if ugly_nums[i] == current_multiple_of_2:
            i2 += 1
            current_multiple_of_2 = ugly_nums[i2] * 2
        if ugly_nums[i] == current_multiple_of_3:
            i3 += 1
            current_multiple_of_3 = ugly_nums[i3] * 3
        if ugly_nums[i] == current_multiple_of_5:
            i5 += 1
            current_multiple_of_5 = ugly_nums[i5] * 5
    return ugly_nums


def get_super_ugly_numbers(size, primes):
    ugly_nums = [None] * size
    ugly_nums[0] = 1
    prime_indices = [0] * len(primes)
    current_multiples = list(primes)
    for i in range(1, size):
        ugly_nums[i] = min(current_multiples)
        for j in range(len(current_multiples)):
            if ugly_nums[i] == current_multiples[j]:
                prime_indices[j] += 1
                current_multiples[j] = ugly_nums[prime_indices[j]] * primes[j]
    return ugly_nums


def main():
    ans = get_ugly_numbers(150)
    print(ans)
    ans = get_super_ugly_numbers(150, [2, 3, 5])
    print(ans)


if __name__ == "__main__":
    main()
