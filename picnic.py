#!/usr/bin/env python3
"""
Author : marko <marko@localhost>
Date   : 2023-07-22
Purpose: Rock the Casbah
"""

import argparse

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='arguments provided as a list of strings',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('food',
                        metavar='str',
                        nargs = '+',
                        help='provisional number of string arguments representing food')

    parser.add_argument('-s',
                        '--sort',
                        help='whether or not to sort the food items',
                        action='store_true')

    return parser.parse_args()

#---------------------------------------------------

def print_list_elements(my_list):
    #sorted_list = sorted(my_list)
    text = "You are bringing "
    for i, element in enumerate(my_list):
        if i == len(my_list) - 1:
            text += "and " + str(element)
        elif i == len(my_list) - 2:
            text += str(element) + " "
        else:
            text += str(element) + ", "
    text += "."
    print(text)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    s = args.sort
    food_list = args.food

    print(f'sort the foods = "{s}"')
    print(f'foods = "{food_list}"')

    if s:
        food_list_sorted = sorted( food_list )
        print_list_elements(food_list_sorted)
    else:
        print_list_elements(food_list)

# --------------------------------------------------
if __name__ == '__main__':
    main()
