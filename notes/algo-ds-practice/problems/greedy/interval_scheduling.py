# Verified on https://www.spoj.com/problems/BUSYMAN/
'''
Given a list of activities `(st, et)`, where `st` and `et` are the start time and end time of an activity, return the maximum number of activities that can happen.

OR

We have just a single lecture hall. Among all the classes, make a schedule such that max number of classes can happen.

Also called as the `Activity selection`.

Example:

events = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
Answer = 4 (Activities 0, 1, 3, 4)

'''
def interval_scheduling(activities):
    '''
    Sort the events by their end times.
    Then starting from the beginning, keep including the events whose
    start time >= end time of last included event.
    '''
    activities = sorted(activities, key=lambda event: (event[1], event[0]))
    previous_end_time = 0
    result = []
    for activity in activities:
        start_time = activity[0]
        if start_time >= previous_end_time:
            result.append(activity)
            previous_end_time = activity[1]
    return result


def main():
    activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
    print(interval_scheduling(activities))


if __name__ == "__main__":
    main()
