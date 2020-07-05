def removeLoop(head):
    '''
    1. First find the meeting point.
    2. Then take turtle to head and keep hare at the meeting point itself.
    3. Advance both at a speed of 1.
    4. Their meeting point will be the cycle start node.
    See kartik kukreja's blog post for proof.
    '''
    hare = head
    turtle = head
    meeting_point = None
    while hare and turtle and turtle.next:
        hare = hare.next
        turtle = turtle.next.next
        if hare == turtle:
            meeting_point = hare
            break
    if meeting_point is None:
        # No loop
        return
    turtle = head
    while True:
        if hare.next == turtle.next:
            hare.next = None
            break
        hare = hare.next
        turtle = turtle.next


def removeLoopCountCycleLength(head):
    '''
    1. First find the meeting point.
    2. Then compute the length of the cycle.
    3. Then bring turtle to head and hare to cycle_length distance from head.
    4. Now advance both by a speed of 1.
    5. Their meeting point will be the cycle start node.
    '''
    hare = head
    turtle = head
    meeting_point = None
    while hare and turtle and turtle.next:
        hare = hare.next
        turtle = turtle.next.next
        if hare == turtle:
            meeting_point = hare
            break
    if meeting_point is None:
        # No loop
        return

    # Compute length of cycle.
    cycle_length = 1
    hare = hare.next
    while hare != turtle:
        hare = hare.next
        cycle_length += 1
    # Bring turtle to head
    # and advance hare k nodes from head.
    turtle = head
    hare = head
    while cycle_length:
        cycle_length -= 1
        hare = hare.next
    while True:
        if hare.next == turtle.next:
            hare.next = None
            break
        hare = hare.next
        turtle = turtle.next
