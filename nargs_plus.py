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
                        nargs='+',
                        type=int,
                        help='two integers to add')


    return parser.parse_args()


# --------------------------------------------------

def print_sum_expression(numbers):
    sum_expression = "+".join(str(num) for num in numbers)
    total_sum = sum(numbers)
    print(f"{sum_expression}={total_sum}")


def main():
    """Make a jazz noise here"""

    args = get_args()
    integers = args.integers

    print(integers)

    print_sum_expression(integers)

# --------------------------------------------------
if __name__ == '__main__':
    main()
