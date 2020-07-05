'''
Suppose there is a circular road.
There are n petrol pumps on that road.
You are given two array, a[] and b[], and a positive integer c, where:
a[i] denote the amount of fuel we get on reaching ith petrol pump,
b[i] denote the amount of fuel used to travel from ith petrol pump to (i + 1)th petrol pump and
c denotes the capacity of the tank in the vehicle.
The task is to calculate the number of petrol pump from where the vehicle will be able to complete the circle and come back to starting point.
This post is different from Find the first circular tour that visits all petrol pumps.

Examples:

    Input : n = 3, c = 3
    a[] = { 3, 1, 2 }
    b[] = { 2, 2, 2 }
    Output : 2
    Explanation:
    If we starts with 0th petrol pump, we will gain
    3 (a[0]) litres of petrol and lose 2 litre (b[0] to travel
    to 1st petrol pump.On refueling 1 litre (a[1])
    of petrol on 1st petrol pump, we will lose 2
    litres (b[0]) of petrol to reach 2nd petrol pump.
    Now the tank is empty.On refueling 2 litres (a[2]) of petrol
    at 2nd petrol pump, we can travel back 0th
    petrol pump.

    If we starts from 1st petrol pump, we will gain 1
    litre of petrol but to travel to 2nd petrol pump
    we need 2 litres of petrol, which we don’t have. So, we cannot
    starts from 1st petrol pump.


    If we starts from 2nd petrol pump, we will gain 2
    litres of petrol and travel to 0th petrol pump by
    losing 2 litres of petrol. On refueling 3 litres on 1st
    petrol pump, we can travel to 1st petrol
    pump by losing 2 litre petrol. On refueling 1 litre of petrol, we
    will have 2 litres of petrol left which we can use by traveling to
    2nd petrol pump.

    Input : n = 3, c = 3
    a[] = { 3, 1, 2 }
    b[] = { 2, 2, 1 }
    Output : 2

SOLUTION:

The problem involves 2 parts, first involves if a valid starting petrol pump exists and second, if such a petrol pump exists, check if the petrol pump before it can also be used as a starting petrol pump.

First, lets start from a petrol pump s and travel to petrol pump, s + 1, s + 2, s + 3 till s + j, suppose we run out of fuel before we go to petrol pump s + j + 1, then no petrol pump between s and s + j can be used as starting petrol pump.
Hence, we start over with s + j + 1 as the starting petrol pump.
If no such petrol pump exists after all petrol pumps are exhausted, the answer is 0. This step takes O(n).

Second, lets visit one such valid petrol pump (lets call it s).
The petrol pump before s i.e s – 1 can also be a start petrol pump provided the vehicle can start at s – 1 and reach s.

If a[i] is take fuel available at petrol pump i, and c be the capacity of the fuel tank, and b[i] is the amount of fuel the vehicle takes to travel from petrol pump i to i + 1, then lets define need[i] as follows:

need[i] = max(0, need[i + 1] + b[i] - min(c, a[i]))

need[i] is the extra fuel, if present in the vehicle at the beginning of the journey at petrol pump i (excluding a[i]_, it can be a valid petrol pump.

If need[i] = 0, then petrol pump i is a valid starting petrol pump.
We know that need[s] = 0 from step 1.
We can evaluate if s – 1, s – 2, … are starting petrol pumps are not.
This step also takes O(n).
'''
