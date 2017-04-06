import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.01)

s = np.sin(2 * np.pi * t)
# make line red 
#plt.rcParams['lines.color'] = 'red' -- can't be used to python 3.x
plt.plot(t,s,label = "$example$",color = 'r',marker = "+",linewidth=1)  
#plt.plot(t,s)

c = np.cos(2 * np.pi * t)
# make line thick
plt.rcParams['lines.linewidth'] = 3
#plt.rcdefaults()  -- set defaults
plt.plot(t,c)

plt.show()
