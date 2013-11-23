# class for a cell

import random

def firstn():
    num = 1
    while True:
        yield num
        num += 1

id_counter = firstn()
p = .1

class Cell:    
    def __init__(self, mut = []):
        self.mut = mut
    def ancestor(self):
        if(random.random() < p):
            return Cell(mut = self.mut + [id_counter.next()])
        else:
            return Cell(mut = self.mut + [])
    def __str__(self):
        return str(self.mut)
    def __repr__(self):
        return Cell.__str__(self)
    def ty(self):
        return self.mut