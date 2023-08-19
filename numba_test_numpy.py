#! /usr/bin/env python3

import numpy as np

import time

def main():

    vec = np.arange(1,10001)

    start = time.perf_counter()

    print( np.sum(vec) )

    end = time.perf_counter()

    print(f'elapsed time is {end-start}')


    start = time.perf_counter()

    print( np.sum(vec) )

    end = time.perf_counter()

    print(f'elapsed time is {end-start}')

if __name__ == "__main__":

    main()