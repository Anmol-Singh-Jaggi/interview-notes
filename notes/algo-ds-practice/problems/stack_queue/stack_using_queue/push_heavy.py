from collections import deque


class StackFromQueues:
    def __init__(self):
        # queue1 always stores in reverse order.
        # queue2 is used as a temporary buffer.
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, item):
        self.queue2.append(item)
        while self.queue1:
            self.queue2.append(self.queue1.pop())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        return self.queue1.pop()

    def __len__(self):
        return len(self.queue1)
