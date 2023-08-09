import re

def main():

    text = "Ovo je neki tekst"

    pattern1 = '[aeiou].+'

    ch_char = 'a'

    text_new = re.sub( pattern1 , ch_char , text )

    pattern2 = '[AEIOU].+'

    text_new_2 = re.sub( pattern2 , ch_char.upper() , text_new )

    print( text_new_2 )

if __name__ == '__main__':
    main()