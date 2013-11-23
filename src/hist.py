#plot mutation spectrum

import pickle
import numpy as np

file = open('hist.pkl', 'rb')

x = pickle.load(file)
y = pickle.load(file)

file.close()


import pylab as pyl
import math
import matplotlib.pyplot as plt

def make_plot(x,y):
    m1 = 10
    m2 = 100
    fit = pyl.polyfit(np.log(x[m1:m2]), np.log(y[m1:m2]),1)
    fit_fun = pyl.poly1d(fit)
    power_fit = lambda x: math.exp(fit_fun(math.log(x)))
    vec_power_fit = np.vectorize(power_fit)
    plt.plot(x, y, 'yo')
    plt.plot(x,vec_power_fit(x),'b')
    ax = plt.axes()
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.text(0.3, 0.07,
        'log(y(x)) = %.3f log(x) + %.3f' % (fit[1], fit[0]),
        fontsize=14,
        horizontalalignment='center',
        verticalalignment='center',
        transform=ax.transAxes)
    plt.show()

#run ipython hist.py -i in terminal
# input these lines to autoreload make_plot every line
"""    
%load_ext autoreload
%autoreload 2
from hist import make_plot
"""