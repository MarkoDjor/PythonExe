import numpy as np
import matplotlib.pyplot as plt

b,c = 3,-1

a_vec = np.arange(-1,3,0.1)

print(a_vec)

x_vec = (-b + np.sqrt( b**2 - 4*a_vec*c))/(2*a_vec)

print(x_vec)

plt.plot( a_vec , x_vec , 'r-' )

plt.xlabel("a values")

plt.ylabel("x root values")

plt.show()