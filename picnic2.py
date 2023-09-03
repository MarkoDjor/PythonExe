#!/usr/bin/env python3
"""
Author : marko <marko@localhost>
Date   : 2023-07-22
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='list of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('food',
                        metavar='str',
                        nargs="+",
                        help='food items')

    parser.add_argument('-s',
                        '--sortirano',
                        help='sort food items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    s = args.sortirano
    listf = args.food

    print(f'sortirano = "{s}"')
    print(f'food items = "{listf}"')

    if s:
        listf.sort()

    foodj = ', '.join(listf[0:-1]) + " and " + listf[-1] + "."

    print( f'You are bringing {foodj}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
