from collections import deque


class QueueFromStacks:
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, item):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(item)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self):
        return self.stack1.pop()

    def __len__(self):
        return len(self.stack1) + len(self.stack2)

    def __repr__(self):
        return repr(self.stack1) + "\n" + repr(self.stack2)


def main():
    qs = QueueFromStacks()
    qs.push(1)
    print(qs)


main()
