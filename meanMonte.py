import numpy as np
import random

N = 1000
success = 0

y_sum = 0

for n in range(N):

    x = random.random()

    y = np.sqrt( 1 - x**2 )

    y_sum += y

pi = 4*y_sum/N

print(pi)
