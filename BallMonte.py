import numpy as np
import random
import matplotlib.pyplot as plt

N = 1000

z_avg = []

n_list = []

n = 0

sum_z = 0

for i in range(N):

    x = random.random()

    y = random.random()

    if x**2 + y**2 < 1:

        z = np.sqrt( 1 - x**2 - y**2 )

        n = n + 1

        sum_z = sum_z + z

        z_avg.append(sum_z/n)

        n_list.append(n)

print( 2*z_avg[-1] )

plt.plot( n_list , z_avg )

plt.savefig( ~/Documents/Python/"ball_fac_conv" )

plt.show()