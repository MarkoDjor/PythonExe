#!/usr/bin/env python3
"""
Author : Marko Djordjevic <dmarko@bio.bg.ac.rs>
Date   : 2023-07-21
Purpose: Explore two positional arguments
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Two positional arguments string and integer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('colour',
                        metavar='colour',
                        type=str,
                        help='colour of the item',
                        choices=['red','blue','yellow','black'])

    parser.add_argument('size',
                        metavar='size',
                        type=int,
                        help='size of the item',
                        choices=range(1,11))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    colour = args.colour
    size = args.size

    print(f'colour is {colour}')
    print(f'size is {size}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
