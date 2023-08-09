#!/usr/bin/env python3
"""
Author : Marko Djordjevic <dmarko@bio.bg.ac.rs>
Date   : 2023-07-23
Purpose: Put the text in uppercase letters
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='input text, or input file, or output file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-t',
                        '--text',
                        help='text to turn uppercase',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-f',
                        '--file',
                        help='A readable file with text to turn uppercase',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-w',
                        '--write',
                        help='A writable file to write text into',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=None)




    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    read_file = args.file
    write_file = args.write

    print(f'text = "{text}"')
    print('read_file = "{}"'.format(read_file.name if read_file else ''))
    print('write_file = "{}"'.format(write_file.name if write_file else ''))

    if text != '':
        if write_file:
            write_file.write(text + '\n' )
            write_file.close()
        else:
            print(text)
    else:
        print( read_file.read().upper() )

# --------------------------------------------------
if __name__ == '__main__':
    main()
