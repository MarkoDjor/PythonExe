import numpy as np

import matplotlib.pyplot as plt

b,c = 2,-1

a_vec = np.arange(-1,2,0.3)

x_vec = np.array([])

for a in a_vec:
    x = -b+np.sqrt(b**2-4*a*c)/(2*a)
    x_vec = np.append( x_vec , x )
    print( f"a = {a:.4f}, x = {x:.4f}" )

plt.plot( a_vec , x_vec , 'r-')
plt.xlabel( "b parameter from quadratic equation")
plt.ylabel( "positive root" )
plt.show()
