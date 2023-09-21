import numpy as np

import matplotlib.pyplot as plt

lam = 0.5

step = 0.001

t_vec = np.arange(0,20,step)

p_vec = lam*np.exp(-lam*t_vec)

plt.plot(t_vec,p_vec,'r-')

plt.xlabel( "times" )

plt.ylabel( "probability" )

plt.show()

norm = np.sum( p_vec )*step

print( norm )

mean = np.sum( p_vec*t_vec )*step

print( mean )