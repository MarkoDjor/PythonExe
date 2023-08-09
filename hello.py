#!/usr/bin/env python3
"""
Author : Marko Djordjevic <dmarko@bio.bg.ac.rs>
Date   : 2023-07-20
Purpose: Say hello with optional world
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='One positional argument',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('name',
                        metavar='name',
                        help='A name to greet!')


    return parser.parse_args()

#def starts_with_vowel(word):
#    vowels = ['a', 'e', 'i', 'o', 'u']
#    return word[0].lower() in vowels
# --------------------------------------------------
def main():
    """Make piano play here"""

    args = get_args()
    name = args.name
    #int_arg = args.int
    #file_arg = args.file
    #flag_arg = args.on
    #pos_arg = args.positional

    print(f'name = "{name}"')
    #print(f'int_arg = "{int_arg}"')
    #print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    #print(f'flag_arg = "{flag_arg}"')
    #print(f'positional = "{pos_arg}"')

    #word = str_arg

    print(f"Hello {name}!.")

if __name__ == '__main__':
    main()
