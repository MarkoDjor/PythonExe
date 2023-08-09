text = 'mika vezba i uci python'

change_ch = 'a'

jumper = {'a': change_ch, 'e': change_ch , 'i': change_ch , 'o': change_ch, 'u': change_ch }

print( text.translate(str.maketrans(jumper) ) )
