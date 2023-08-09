text = "Ovo je neki slucajan tekst"

ch_char = 'a'

list_ch = [ ch_char if char in 'aeiou' else ch_char.upper() if char in 'AEIOU' else char for char in text ]

# for ch in text:
#
#     if ch in 'aeiou':
#
#         text_ch += ch_char
#
#     elif ch in 'AEIOU':
#
#         text_ch += ch_char.upper()
#
#     else:
#
#         text_ch += ch

text_ch = ''.join(list_ch)

print( text_ch )