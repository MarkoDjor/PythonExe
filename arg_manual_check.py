#!/usr/bin/env python3
"""
Author : Marko Djordjevic <dmarko@bio.bg.ac.rs>
Date   : 2023-07-21
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def check_in_range(number, lower_bound, upper_bound):
    if lower_bound <= number <= upper_bound:
        return True
    else:
        return False

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    args = parser.parse_args()

    lower_bound = 1

    upper_bound = 10

    if not check_in_range(args.int, lower_bound, upper_bound):
        parser.error(f'{args.int} has to be in the range from {lower_bound} to {upper_bound}')

    return parser.parse_args()
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    int_arg = args.int

    print(f'int_arg = "{int_arg}"')

# --------------------------------------------------
if __name__ == '__main__':
    main()
