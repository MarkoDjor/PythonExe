import random as rnd

import string

text = "Where will we go now?"

m = 0.3

s = 8

rnd.seed(s)

print("You said: " + text)

lena = len(text)

len_m = round(m*lena)

alpha_l = sorted( string.ascii_letters + string.punctuation )

alpha = ''.join(alpha_l)

len_a = len(alpha)

#mut_list = [ alpha[ rnd.randint(0,len_a-1) ] for _ in #range(len_m) ]

mut_pos = [ rnd.randint(0,lena-1) for _ in range(len_m) ]

mut_list = []

for pos in mut_pos:

    lett = text[pos]

    alpha = alpha.replace(lett,'')

    mut_list.append(alpha[rnd.randint(0,len_a-1) ])


text_list = list(text)

for n,char_m in enumerate(mut_list):

    text_list[mut_pos[n]] = char_m

mutated_string = ''.join(text_list)

print( "I said: " + mutated_string)
