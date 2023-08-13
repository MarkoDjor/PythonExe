#! /usr/bin/env python3

import numpy as np
import os
import sklearn

numbers = list(range(1,11))

numbers_odd = list( filter( lambda num:num%2==1 , numbers ) )

print(numbers_odd )

array1 = np.array([1.4,11,12.5,14.7])

array2 = array1**2

print( array1 )

print( array2 )