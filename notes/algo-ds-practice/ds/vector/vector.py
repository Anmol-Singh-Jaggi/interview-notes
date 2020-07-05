class Vector:
    size = 0
    capacity = 0
    data = []

    def _init__(self, size=0):
        self.size = size
        if size:
            self.data = [None] * size
        print('Vector initialized!!')

    def __str__(self):
        return "Size = {} \nCapacity = {} \nData = {}\n".format(
            self.size, self.capacity, self.data)

    def __reserve__(self, new_capacity):
        if new_capacity <= self.capacity:
            return
        data_bak = self.data
        self.data = [None] * new_capacity
        for i in range(len(data_bak)):
            self.data[i] = data_bak[i]
        del data_bak
        self.capacity = new_capacity

    def push(self, element):
        if self.capacity == self.size:
            new_capacity = 1 if self.size == 0 else self.size * 2
            self.__reserve__(new_capacity)
        self.data[self.size] = element
        self.size += 1

    def __shrink__(self, new_capacity):
        if new_capacity >= self.capacity:
            return
        data_bak = self.data
        self.data = [None] * new_capacity
        for i in range(len(self.data)):
            self.data[i] = data_bak[i]
        del data_bak
        self.capacity = new_capacity

    def pop(self):
        if (self.size == 0):
            return
        self.size -= 1
        self.data[self.size] = None
        new_capacity = self.capacity >> 1
        if self.size <= new_capacity:
            self.__shrink__(new_capacity)


vec = Vector()
for i in range(10):
    vec.push(i)
    print(vec)

for i in range(10):
    vec.pop()
    print(vec)