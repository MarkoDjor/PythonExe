#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@DESKTOP-BF1BI4H>
Date   : 2023-08-14
Purpose: Twelve days of Christmas song
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Integer input and output file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--numDays',
                        help='a day from which to start the song',
                        metavar='int',
                        type=int,
                        default=1)

    parser.add_argument('-o',
                        '--outFile',
                        help='file to write output text',
                        metavar='FILE',
                        type=argparse.FileType('w'),
                        default=None)

    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
