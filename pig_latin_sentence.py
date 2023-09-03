#Korisnik treba na pocetku da zada recenicu na engleskom. Radi jednostavnosti, ta recenica se sastoji samo od reci, odnosno ne pocinje velikim slovom i ne zavrsava se tackom npr.: "it is nice weather today". Svaku od reci u recenici promeniti u skladu sa pig latin pravilima i tako promenjenu recenicu odstampati. Recenica iz primera treba da posle promene postane:
#"itway isway icenay eatherway odaytay"

recenica=input("napisi recenicu:")

recenical=recenica.split()

reclasa=[]

for rec in recenical:

    if rec[0] in ["a","e","i","o","u"]:

     reclasa.append(rec + "way")

    else:
        reclasa.append(rec[1:] + rec[0] + "ay")

print(" ".join(reclasa))
