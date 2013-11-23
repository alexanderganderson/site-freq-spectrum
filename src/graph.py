#graph class

class MarkedGraph:
    def __init__(self, _L = 4):
        self.L = _L;
        self.g = {}
        for i in range(self.L): 
            for j in range(self.L):
                self.g[(i, j)] = [0, [( (i + ii) % self.L, (j + jj) % self.L ) 
                    for ii in [-1,0,1] for jj in [-1,0,1] if (ii != 0 or jj != 0)] ]
    def get_neighbors(self, key):
        try:
            return self.g[key][1]
        except KeyError, e:
            return []
            
    def get_keys(self):
        return self.g.keys()
        
    def mark(self, key):
        """
        Mark key as visited
        """
        if(self.g[key][0]==1):
            print "Key " + str(key) + " already marked"
        self.g[key][0] = 1
    def is_marked(self, key):
        """
        Return if key has been visited
        """
        return self.g[key][0] == 1
    def get_unmarked_n(self, key):
        """
        Return list of unmarked neighbors
        """
        return [n_key for n_key in self.get_neighbors(key) if not self.is_marked(n_key)]
    def __str__(self):
        s = ''
        for i in range(self.L): 
            for j in range(self.L):
                s += ( str(self.g[(i,j)][0]) + ' ' )
            s += '\n'
        return s
    def __repr__(self):
        return self.__str__()