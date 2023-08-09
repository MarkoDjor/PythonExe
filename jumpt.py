text = "Call 1-800-329-8044 yesterday!"

numc = { '0':'5', '1':'9' , '2':'8' , '3':'7' , '4':'6' , '5':'0' , '6':'4' , '7':'3' , '8':'2', '9':'1' }

print( numc )

textc = ""

for let in text:

    letc = numc.get(let,'NA')

    if letc == 'NA':

        textc += let

    else:

        textc += letc

print(textc)
