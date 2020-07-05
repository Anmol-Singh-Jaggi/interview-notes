class StackWithMin():
    '''
    Just remember this algo.
    The same can be used for Stack with Max.
    '''

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val):
        if self.min is None:
            self.min = val
            self.stack.append(val)
            return
        if val >= self.min:
            self.stack.append(val)
        else:
            dummy = 2 * val - self.min
            self.stack += [val, dummy]
            self.min = val

    def pop(self):
        if not self.stack:
            raise Exception()
        last = self.stack.pop()
        if last >= self.min:
            return last
        # We reached some dummy.
        # That means we are removing the minimum element.
        # That means time to update the minimum.
        self.min = 2 * self.min - last
        return self.stack.pop()
