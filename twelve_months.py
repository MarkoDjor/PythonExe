#! /usr/bin/env python3

def verse(n):

    lines = { 1:"A partridge in a pear tree" , \
    2:"Two turtle doves" , \
    3:"Three French hens" , \
    4:"Four calling birds" , \
    5:"Five gold rings" , \
    6:"Six geese a laying" , \
    7:"Seven swans a swimming" , \
    8:"Eight maids a milking" , \
    9:"Nine ladies dancing" , \
    10:"Ten lords a leaping" , \
    11:"Eleven pipers piping" , \
    12:"Twelve drummers drumming"}

    days = { 1:"first" , \
    2:"second" , \
    3:"third" , \
    4:"fourth" , \
    5:"fifth" , \
    6:"sixth" , \
    7:"seventh" , \
    8:"eight" , \
    9:"ninth" , \
    10:"tenth" , \
    11:"eleventh" , \
    12:"twelfth"  }

    lista_lines = []

    lista_lines.append( f'On the { days[n] } day of Christmas,' )

    lista_lines.append( 'My true love gave to me,' )

    num_days = [ day for day in range(1,n+1) ]

    num_days.reverse()

    for i in num_days:

        lista_lines.append( lines[i] )

    if n>1:

        lista_lines[-1] = "And a partrige in a pear tree."

    if n<12:
        lista_lines.append('\n')

    print("\n".join(lista_lines))

def main():

##

    n = 3
    print(n)

    for i in range(n,13):
        verse(i)

##

if __name__ == "__main__":
    main()