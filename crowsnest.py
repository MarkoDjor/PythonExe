#!/usr/bin/env python3
"""
Author : Marko Djordjevic <dmarko@bio.bg.ac.rs>
Date   : 2023-07-21
Purpose: Crowsnest example
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Takes one positional string argument',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('name',
                        metavar='str',
                        type=str,
                        help='name of the animal to print')

    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    name = args.name

    dec = args.on

    article = "an" if name.lower()[0] in 'aeiou' else "a"

    if dec:
        print("I observe {} {}".format(article,name))
    else:
        print("I see {} {}".format(article,name))
# --------------------------------------------------
if __name__ == '__main__':
    main()
