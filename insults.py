#!/usr/bin/env python3
"""
Author : marko <marko@localhost>
Date   : 2023-07-30
Purpose: Generate random insults
"""

import argparse
import random as rnd

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Generate random insults',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--number_insults',
                        help='Number of insults (sentences to repet)',
                        metavar='int',
                        type=int,
                        default=1)

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of insulting adjectives',
                        metavar='int',
                        type=int,
                        default=2)

    parser.add_argument('-s',
                        '--seed',
                        help='Seed for random selection',
                        metavar='int',
                        type=int,
                        default=None)

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    n,a,s = args.number_insults,args.adjectives,args.seed

    adjectives = [ "false", "ruinous", "filthsome", "caterwauling" , "toad-spotted" , "cullionly" , "rotten" , "caterwauling" ]

    nouns = [ "slave" , "villian" , "traitor" , "lunatic" , "harpy" ]

    rnd.seed(s)

    for _ in range(1,n+1):

        text = "You "

        for j in range(1,a+1):

            adj = rnd.choice(adjectives)

            if j == a:

                text += adj + " "

            else:

                text += adj + ", "

        noun = rnd.choice(nouns)

        text += noun + "!"

        print( text )

# --------------------------------------------------
if __name__ == '__main__':
    main()
