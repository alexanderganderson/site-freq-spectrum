# random queue
import random
from math import floor

class RandomQueue:
    def __init__(self):
        self.a = []
    def size(self):
        return len(self.a)
    def is_empty(self):
        return self.size() == 0
    def add(self, key):
        self.a.append(key)
    def rand_pop(self):
        i = random.randrange(0,self.size())
        self.a[i], self.a[-1] = self.a[-1], self.a[i]
        return self.a.pop()
    def __str__(self):
        return str(self.a)
    def __repr__(self):
        return str(self.a)
    