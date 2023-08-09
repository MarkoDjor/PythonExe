#!/usr/bin/env python3
"""
Author : Marko Djordjevic <dmarko@bio.bg.ac.rs>
Date   : 2023-08-02
Purpose: Print Bottles of bear song
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print Bottles of bear song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num_verses',
                        help='Number of verses to use',
                        metavar='int',
                        type=int,
                        default=10)

    #return parser.parse_args()
    args = parser.parse_args()
    if args.num_verses <= 0:
        parser.error(f'--val "{args.num_verses}" must be a positive integer')
    return args

def verse(n):

    print(f'{n} bottles of beer on the wall,')
    print(f'{n} bottles of beer,')
    print(f'Take one down, pass it around,')
    print(f'{n-1} bottles of beer on the wall!\n\n')
# --------------------------------------------------
def main():
    """Make a piano noise here"""

    args = get_args()
    n = args.num_verses

    for i in reversed(range(2,n+1)):
        verse(i)

    print(f'1 bottles of beer on the wall,')
    print(f'1 bottles of beer,')
    print(f'Take one down, pass it around,')
    print(f'No more bottles of beer on the wall!\n')

#--------------------------------
if __name__ == '__main__':
    main()
