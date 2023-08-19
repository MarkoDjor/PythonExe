#! /usr/bin/env python3

import numpy as np

print("Hello Word test")

vektor = np.array(list(range(1,11)))

vektor_2 = np.square( vektor )

print( "Original vector is {}, while the squared vector is {}".format(vektor , vektor_2 ) )

