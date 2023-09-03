import numpy as np
import random

N = 1000
success = 0

for n in range(N):

    #print(n)

    x = random.random()

    y = random.random()

    r = np.sqrt( x**2 + y**2 )

    if r < 1:

        success += 1

pi = 4*success/N

print(pi)