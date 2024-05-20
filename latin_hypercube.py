#!/usr/bin/env python3

from scipy.stats import qmc
import matplotlib.pyplot as plt
import numpy as np

sampler = qmc.LatinHypercube(d=2)

sample = sampler.random(n=10)

l_bounds = [0, 0]

u_bounds = [2, 3]

sample_scaled = qmc.scale(sample, l_bounds, u_bounds)

plt.scatter( sample_scaled[:,0], sample_scaled[:,1] )

plt.grid()

plt.show()
