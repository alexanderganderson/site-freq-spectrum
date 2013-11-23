# graph simulation

import graph
import cell
import random_queue
import numpy as np
import matplotlib.pyplot as plt
import random
from math import floor

# parameters

L = 10
MAX_ITER = L * L * 2

# initialize data structures
q = random_queue.RandomQueue() 
f = {} #dict with (key,val) = (filled node with empty neighbor, value for that cell)
mg = graph.MarkedGraph(_L=L)
r = np.zeros(L * L, dtype = 'int') #store the results of the simulation


#initialize 
keys = mg.get_keys()

k = keys[0]
f[k]=cell.Cell()
mg.mark(k)
q.add(k)


for mu in range(MAX_ITER):
    if q.is_empty():
        print "Queue is empty" 
        print "The size of f is " + str(len(f))
        break
    #print q.size()
    #print len(f)
    k1 = q.rand_pop()
    nei = mg.get_unmarked_n(k1)
    l_nei = len(nei)
    if(l_nei > 1):
        q.add(k1)
    
    if(l_nei == 0):
        for site in f[k1].ty():
            r[site] += 1
        del f[k1]
        continue
        
    # choose a random neighbor 
    k2 = nei[random.randrange(0,l_nei)]

    # add cell to that neighbor
    f[k2] = f[k1].ancestor()
    mg.mark(k2)
    q.add(k2)
    

for val in f.values():
    for site in val.ty():
        r[site] += 1

m = np.max(r)
y, x = np.histogram(r, bins = range(1,m+1))
#y, x = np.histogram(r, bins = range(0,m+1,(m+1)/100))
tot = np.sum(y)
y = np.cumsum(y[::-1])[::-1]
y = y / (1.0 * tot )
x = x[:-1]

import pickle

output = open('../data/hist1.pkl','wb')

pickle.dump(x, output)
pickle.dump(y, output)

output.close()

