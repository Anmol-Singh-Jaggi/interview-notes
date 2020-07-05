def detectLoop(head):
    hare = head
    turtle = head

    while hare and turtle and turtle.next:
        hare = hare.next
        turtle = turtle.next.next
        if hare == turtle:
            return True
    return False
