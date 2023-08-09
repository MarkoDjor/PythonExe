#!/usr/bin/env python3
"""
Author : Marko Djordjevic <dmarko@bio.bg.ac.rs>
Date   : 2023-07-25
Purpose: Emulate Unix "wc" for multiple inputs
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='take one or more positional arguments or stdin if no arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin],
                        help='one or more files or strings')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    fhl = args.files

    print(f'input = "{fhl}"')

    nlines_t , nwords_t , nbytes_t = 0 , 0 , 0

    for fh in fhl:

        nlines , nwords , nbytes = 0 , 0 , 0

        for line in fh:

            nlines += 1
            nwords += len(line.strip().split())
            nbytes += len(line)

        print( f'{nlines:8}{nwords:8}{nbytes:8} {fh.name}'  )

        nlines_t += nlines
        nwords_t += nwords
        nbytes_t += nbytes

    if len( fhl ) > 1:
        print( f'{nlines_t:8}{nwords_t:8}{nbytes_t:8} total'  )

# --------------------------------------------------
if __name__ == '__main__':
    main()
