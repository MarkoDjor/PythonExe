#!/usr/bin/env python3
"""
Author : Marko Djordjevic <dmarko@bio.bg.ac.rs>
Date   : 2023-07-21
Purpose: Print lines in a file together with line numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Readable text file as an input',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    return parser.parse_args()

def print_lines_with_line_numbers(file_path):
#with open(file_path, 'r') as file:
    for line_number, line in enumerate(file_path, start=1):
        print(f"{line_number}: {line.strip()}")

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    file_arg = args.file

    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))

    #file_path = 'path_to_your_text_file.txt'  # Replace with the actual path to your text file

    print_lines_with_line_numbers(file_arg)

# --------------------------------------------------
if __name__ == '__main__':
    main()
