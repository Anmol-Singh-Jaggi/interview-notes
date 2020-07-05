from collections import deque


class QueueFromStack:
    def __init__(self):
        self.stack1 = deque()

    def push(self, item):
        self.stack1.append(item)

    def pop(self):
        """
        Actually it using the recursion stack as the other stack.
        """
        top = self.stack1.pop()
        if not self.stack1:
            return top
        oldest = self.pop()
        self.stack1.append(top)
        return oldest

    def __len__(self):
        return len(self.stack1) + len(self.stack2)

    def __repr__(self):
        return repr(self.stack1) + "\n" + repr(self.stack2)


def main():
    qs = QueueFromStack()
    qs.push(1)
    print(qs)


main()
