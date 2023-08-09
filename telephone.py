#!/usr/bin/env python3
"""
Author : Marko Djordjevic <dmarko@bio.bg.ac.rs>
Date   : 2023-08-01
Purpose: For random string mutation
"""

import argparse
import random as rnd
import string
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Randomly mutate a string',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Initial string or text file name to be mutated')

    parser.add_argument('-m',
                        '--m_rate',
                        help='Percent of letters to be mutated',
                        metavar='float',
                        type=float,
                        default=0.3)

    parser.add_argument('-s',
                        '--seed',
                        help='random seed',
                        metavar='int',
                        type=int,
                        default=1)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    s = args.seed
    m = args.m_rate

    if os.path.isfile(text):
        fh = open(text,'r')
        text = fh.read().strip()
        fh.close()

    rnd.seed(s)

    print("You said: " + text)

    lena = len(text)

    len_m = round(m*lena)

    alpha_l = sorted( string.ascii_letters + string.punctuation )

    alpha = ''.join(alpha_l)

    len_a = len(alpha)

    #mut_list = [ alpha[ rnd.randint(0,len_a-1) ] for _ in #range(len_m) ]

    mut_pos = [ rnd.randint(0,lena-1) for _ in range(len_m) ]

    mut_list = []

    for pos in mut_pos:

        lett = text[pos]

        alpha_r = alpha.replace(lett,'')

        mut_list.append( alpha_r[rnd.randint(0,len_a-2) ])

    text_list = list(text)

    for n,char_m in enumerate(mut_list):

        text_list[mut_pos[n]] = char_m

    mutated_string = ''.join(text_list)

    print( "I said: " + mutated_string)

# --------------------------------------------------
if __name__ == '__main__':
    main()
