"""
Implement two stacks in an array
Create a data structure twoStacks that represents two stacks.
Implementation of twoStacks should use only one array, i.e., both stacks should use the same array for storing elements. Following functions must be supported by twoStacks.
push1(int x) –> pushes x to first stack
push2(int x) –> pushes x to second stack

pop1() –> pops an element from first stack and return the popped element
pop2() –> pops an element from second stack and return the popped element

SOLUTION:

The idea is to start two stacks from two extreme corners of arr[].
stack1 starts from the leftmost element, the first element in stack1 is pushed at index 0.
The stack2 starts from the rightmost corner, the first element in stack2 is pushed at index (n-1).
Both stacks grow (or shrink) in opposite direction.
To check for overflow, all we need to check is for space between top elements of both stacks. This check is highlighted in the below code.
"""


class TwoStacks:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top1 = -1
        self.top2 = self.size

    def push1(self, elem):
        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = elem
        else:
            print("Stack Overflow!")
            return

    def push2(self, elem):
        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = elem
        else:
            print("Stack Overflow")
        return

    def pop1(self):
        if self.top1 >= 0:
            elem = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return elem
        else:
            print("Stack Underflow")
            return

    def pop2(self):
        if self.top2 < self.size:
            elem = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return elem
        else:
            print("Stack Underflow ")
            return


def main():
    ts = TwoStacks(5)
    ts.push1(5)
    ts.push2(10)
    ts.push2(15)
    ts.push1(11)
    ts.push2(7)
    ts.push2(40)


main()
