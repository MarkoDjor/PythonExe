def main():

    text = "Ovo je neki tekst"

    ch_char = 'a'

    def transform(char):

        return ch_char if char in 'aeiou' else ch_char.upper() if char in   'AEIOU' else char

    ch_list = list(map( transform , text ))

    print( ''.join(ch_list) )

if __name__ == '__main__':
    main()
