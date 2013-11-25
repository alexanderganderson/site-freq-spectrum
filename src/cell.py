# Class for an infinite sites model of a cell
import random

def firstn():
    """
    Give identity of next mutation in infinite sites model. 
    """
    num = 1
    while True:
        yield num
        num += 1

### Initialize iterator and mutation probability
id_counter = firstn()
p = .1


class InfSiteCell:
    
    """
    Infinite sites model of a cell - contains list of mutation sites
    """    
    
    def __init__(self, mut = []):
        self.mut = mut
    
    def ancestor(self):
        """
        Return an ancestor cell. Random chance of a new mutation. 
        """
        if(random.random() < p):
            return InfSiteCell(mut = self.mut + [id_counter.next()])
        else:
            return InfSiteCell(mut = self.mut + [])
    
    def __str__(self):
        return str(self.mut)
    
    def __repr__(self):
        return Cell.__str__(self)
    
    def mut_list(self):
        """
        Return a copy of the list of mutation sites. 
        """
        return self.mut + []