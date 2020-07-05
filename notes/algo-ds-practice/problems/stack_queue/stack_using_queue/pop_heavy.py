from collections import deque


class StackFromQueues:
    def __init__(self):
        # queue1 always stores oldest element first.
        # queue2 is always empty.
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, item):
        self.queue1.append(item)

    def pop(self):
        while len(self.queue1 > 1):
            self.queue2.append(self.queue1.pop())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return self.queue2.pop()

    def __len__(self):
        return len(self.queue1)
