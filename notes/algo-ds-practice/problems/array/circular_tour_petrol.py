"""
Suppose there is a circle. There are N petrol pumps on that circle.

You will be given two sets of data.
1. The amount of petrol that every petrol pump has.
2. Distance from that petrol pump to the next petrol pump.

Return the index of the first petrol pump which can be the starting point of the tour such that truck can cover all the pumps.
Note :  Assume for 1 litre petrol, the truck can go 1 unit of distance.

For example, let there be 4 petrol pumps with amount of petrol and distance to next petrol pump value pairs as
{4, 6}, {6, 5}, {7, 3} and {4, 5}.
The first point from where the truck can make a circular tour is 2nd petrol pump.
Output should be “start = 1” (index of 2nd petrol pump).
"""


def circular_tour_petrol(petrols, distances):
    # CAREFUL: Tricky implementation!
    # Just remember this by heart!
    start = 0
    end = 1
    size = len(petrols)
    current_petrol = petrols[start] - distances[start]
    if size == 1:
        if current_petrol >= 0:
            return 0
        else:
            return -1
    while start != end:
        if current_petrol < 0:
            # Just bring the start to end and current petrol to 0.
            # Note that we are doing this directly as it cannot happen that
            # new start will come somewhere before old_start and end.
            # If we reach a point where current_petrol is negative, that means
            # no index between start and end can be the new start ever.
            current_petrol = 0
            if end > start:
                start = end
            else:
                return -1
        current_petrol += petrols[end] - distances[end]
        end = (end + 1) % size
    if current_petrol < 0:
        return -1
    return start

