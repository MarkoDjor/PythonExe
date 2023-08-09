#!/usr/bin/env python3
"""
Author : Marko Djordjevic <dmarko@bio.bg.ac.rs>
Date   : 2023-07-26
Purpose: Rock the Casbah
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        type=str,
                        help='string or filename')

    parser.add_argument('-c',
                        '--change',
                        help='character to which to change vowels',
                        metavar='str',
                        type=str,
                        choices=['a','e','i','o','u'],
                        default='a')

    return parser.parse_args()

def change_vowels(st,char_change):

    changed_str = ""

    for ch in st:

        if ch.lower() in 'aeiou':

            if ch.islower():

                changed_str += char_change.lower()

            else:

                changed_str += char_change.upper()

        else:

            changed_str += ch

    return changed_str

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    char_change = args.change
    st = args.text

    if os.path.isfile(st):
        file = open(st,'rt')
        text = file.read().strip()
        file.close()
    else:
        text = st

    print( change_vowels(text,char_change) )

# --------------------------------------------------
if __name__ == '__main__':
    main()
