#!/usr/bin/env python3
"""
Author : Marko Djordjevic <dmarko@bio.bg.ac.rs>
Date   : 2023-07-26
Purpose: Rock the Casbah
"""

import argparse

from pprint import pprint as pp


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='letters to look in gashly dictionary',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letters',
                        metavar='str',
                        nargs="*",
                        type = str ,
                        default = [] ,
                        help='letters to look up in gashly dictionary')

    parser.add_argument('-f',
                        '--altdict',
                        help='file for alternative dictionary',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()

def lower_list(s_list):

    letters_s = []

    for lett in s_list:

        letters_s.append( lett.lower() )

    return letters_s

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    fh = args.altdict

    letters = args.letters

    letters_s = lower_list( letters )

    ghostly_dict = dict()

    #for lines in fh:

        #letter = lower_list( lines.strip() )[0]

        #ghostly_dict[letter] = lines.strip()

    ghostly_dict = { lower_list( lines.strip() )[0] : lines.strip() for lines in fh }

    #pp(ghostly_dict)

    #for elements in ghostly_dict.items():

        #print( elements )

    for lett in letters_s:

        if lett in ghostly_dict.keys():

            print( ghostly_dict[lett] )

# --------------------------------------------------
if __name__ == '__main__':
    main()
