#! /usr/bin/env python3

import numpy as np
import numba
import time

#@numba.njit( parallel = True )

#@numba.njit

def sum_vec(vec):

    lena = len(vec)

    suma = 0

    for i in range(len(vec)):

        suma += vec[i]

    return suma

def main():

    vec = np.arange(1,10001)

    start = time.perf_counter()

    print( sum_vec(vec) )

    end = time.perf_counter()

    print(f'elapsed time is {end-start}')


    start = time.perf_counter()

    print( sum_vec(vec) )

    end = time.perf_counter()

    print(f'elapsed time is {end-start}')



if __name__ == "__main__":

    main()

