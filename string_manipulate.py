texta = 'Aika ide napolje ponovo'

change = 'a'

for ch in 'aeiou':

    texta = texta.replace(ch,change).replace(ch.upper(),change.upper())

print( texta )