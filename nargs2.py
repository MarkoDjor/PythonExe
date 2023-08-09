#!/usr/bin/env python3
"""
Author : Marko Djordjevic <dmarko@bio.bg.ac.rs>
Date   : 2023-07-21
Purpose: two same arguments
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='two same integer arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('integers',
                        metavar='int',
                        nargs = 2,
                        type=int,
                        help='two integers to add')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    n1,n2 = args.integers

    print(f'{n1}+{n2} = {n1+n2}')
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
