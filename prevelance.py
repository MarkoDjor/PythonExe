import numpy as np
import matplotlib.pyplot as plt

theta_vec = np.arange(0, 1.01, 0.01)
like_vec = theta_vec**3 * (1 - theta_vec)**7
Z = np.sum(like_vec)
pr = like_vec / Z

plt.plot(theta_vec, pr, 'r-')
plt.xlabel('theta_vec')
plt.ylabel('pr')
plt.show()