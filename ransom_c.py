#!/usr/bin/env python3
"""
Author : Marko Djordjevic <dmarko@bio.bg.ac.rs>
Date   : 2023-08-09
Purpose: Play Shostakovich!
"""

import argparse
import sys
import random as rnd


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Play Shostakovich!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "text", metavar="str", type=str, help="text or filename to randomly capitalize"
    )

    parser.add_argument(
        "-s",
        "--seed",
        help="A named integer argument",
        metavar="int",
        type=int,
        default=None,
    )

    return parser.parse_args()


def bernouli():
    p = rnd.random()
    if p < 0.5:
        return True
    else:
        return False


# --------------------------------------------------
def main():
    """Make a piano noise here"""

    args = get_args()
    s = args.seed
    text = args.text

    if os.path.exists(text):
        with open(text, "r") as fh:
            text = fh.read().strip()

    text_m = ""

    if s:
        rnd.seed(s)

    for lett in text:
        lett_m = lett if bernouli() else lett.upper()

        text_m += lett_m

    print(text_m)


# --------------------------------------------------
if __name__ == "__main__":
    main()
