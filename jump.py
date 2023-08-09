#!/usr/bin/env python3
"""
Author : Marko Djordjevic <dmarko@bio.bg.ac.rs>
Date   : 2023-07-23
Purpose: Change numbers in the input text according to the dictionary code
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('phone',
                        metavar='str',
                        help='Text with phone number to be changed')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.phone
    print(f'phone text = "{text}"')

    #text = "Call 1-800-329-8044 yesterday!"

    numc = { '0':'5', '1':'9' , '2':'8' , '3':'7' , '4':'6' , '5':'0' , '6':'4' , '7':'3' , '8':'2', '9':'1' }

    print( numc )

    textc = ""

    for let in text:

        letc = numc.get(let,'NA')

        if letc == 'NA':

            textc += let

        else:

            textc += letc

    print(textc)

# --------------------------------------------------
if __name__ == '__main__':
    main()
