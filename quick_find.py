class QuickFind(object):
    def __init__(self, size):
        self.size = size
        self.array = None
        self.initialize()

    def initialize(self):
        self.array = [i for i in range(self.size)]

    def combine(self, x, y):
        for i in range(self.size):
            if self.array[i] == self.array[x]:
                self.array[i] = self.array[y]

    def find(self, x, y):
        return self.array[x] == self.array[y]


q = QuickFind(10)
print(q.array)
print(q.find(3, 4))
q.combine(3, 4)
q.combine(2, 1)
print(q.array)
print(q.find(1,2))
q.combine(2,3)
print(q.array)
print(q.find(1,4))

