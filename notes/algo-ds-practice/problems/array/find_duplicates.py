"""
Given an array of n elements which contains elements from 0 to n-1, with any of these numbers appearing any number of times.
Find these repeating numbers in O(n) and using only constant memory space.

SOLUTION:

Algorithm:

While traversing the list, for each element do:
{
    elem = A[i];
    elem_abs = abs(elem);
    sign = sign(A[elem_abs]);
    if sign is +ve
    {
        //make it -ve
        A[elem_abs] = -A[elem_abs]
    }
    else
    {
        elem is a repetition.
    }
}

Basically we are marking the occurrence of an element `elem` by making arr[elem] -ve.

Example: A[] =  {1, 1, 2, 3, 2}
i=0;
Check sign of A[abs(A[0])] which is A[1].  A[1] is positive, so make it negative.
Array now becomes {1, -1, 2, 3, 2}

i=1;
Check sign of A[abs(A[1])] which is A[1].  A[1] is negative, so A[1] is a repetition.

i=2;
Check sign of A[abs(A[2])] which is A[2].  A[2] is  positive, so make it negative. '
Array now becomes {1, -1, -2, 3, 2}

i=3;
Check sign of A[abs(A[3])] which is A[3].  A[3] is  positive, so make it negative.
Array now becomes {1, -1, -2, -3, 2}

i=4;
Check sign of A[abs(A[4])] which is A[2].  A[2] is negative, so A[4] is a repetition.
"""
