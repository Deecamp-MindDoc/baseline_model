import os
import numpy as np
from squaresumerror import *

x = list()
y = list()

# Reading files and assign y values
for filename in os.listdir():
    if 'spatial_cov_bin' in filename:
        y.append(1 if filename.split('_')[0] == 'MDD' else 0)
        x.append(np.fromfile(filename))

# Initialization
m = x[0].size()[0]
n = len(y)
x = np.array(x)
y = np.array(y)


w0 = np.zeros(m)
w = np.zeros(m)
alpha0 = 1
b = np.mean(y)
b0 = b
f = squaresumerror(w, b, x, y)
g = 0
o0 = f + g
t = 1
alpha = 1
