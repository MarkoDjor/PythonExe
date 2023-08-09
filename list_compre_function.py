def transform(char,ch_char):

    return ch_char if char in 'aeiou' else ch_char.upper() if char in       'AEIOU' else char

def main():

    ch_char = 'a'

    text = "Ovo je neki slucajan tekst"

    print( ''.join(transform(char,ch_char) for char in text) )

if __name__ == '__main__':
    main()
