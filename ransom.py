import random as rnd

def bernouli():

    p = rnd.random()

    if p < 0.5:

        return True

    else:

        return False

def main():

    text = "Pay for the cat or we will get her"

    text_m = ""

    for lett in text:

        lett_m = lett if bernouli() else lett.upper()

        text_m += lett_m

    print(text_m)

if __name__ == "__main__":
    main()


