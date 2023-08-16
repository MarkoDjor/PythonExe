#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@DESKTOP-BF1BI4H>
Date   : 2023-08-13
Purpose: Print only odd numbers in a list which is provided as a file or a text string
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='parse list of numbers at the command line input',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('lista',
                        metavar='lista',
                        help='List provided either as an input string or file')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    lista_t = args.lista

    if os.path.exists(lista_t):
        with open(lista_t,"r") as fh:
            lista_t = fh.read().strip()

    lista = lista_t.split()

    numbers = [ int(num) for num in lista ]

    numbers_odd = list( filter( lambda num:num%2==1 , numbers ) )

    letters_odd = [ str(num) for num in numbers_odd ]

    print(' '.join(letters_odd) )

# --------------------------------------------------
if __name__ == '__main__':
    main()
