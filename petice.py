tekst = "U Afriku su isli Marko , Magdalena , Petra  i  Vasa"

tekstl = tekst.split()

recnik={"Marko":"camuga","Magdalena":"mama","Petra":"seka","Vasa":"gospodar camuga"}

#samoglasnici += "o"

tekstn=[]

for item in tekstl:

    if item in ("Marko","Magdalena","Petra","Vasa"):
        tekstn+=list(recnik[item])
    else:

       tekstn += [item]

tekstnn = ' '.join(tekstn)

print(tekstnn)







