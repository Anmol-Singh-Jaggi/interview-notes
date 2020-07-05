from collections import deque


class QueueFromStacks:
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, item):
        self.stack1.append(item)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1)
        return self.stack2.pop()

    def __len__(self):
        return len(self.stack1) + len(self.stack2)

    def __repr__(self):
        return repr(self.stack1) + "\n" + repr(self.stack2)


def main():
    qs = QueueFromStacks()
    qs.push(1)
    print(qs)


main()
