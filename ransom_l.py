#!/usr/bin/env python3

import random as rnd

def bernouli():

    p = rnd.random()

    if p < 0.5:

        return True

    else:

        return False

def main():

    text = "Pay for the cat or we will get her"

    text_l = list(text)

    text_m = [ lett if bernouli() else lett.upper() for lett in text ]

    text_m = ''.join(text_m)

    print(text_m)

if __name__ == "__main__":
    main()
