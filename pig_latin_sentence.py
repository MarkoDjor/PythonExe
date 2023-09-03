#Korisnik treba na pocetku da zada recenicu na engleskom. Radi jednostavnosti, ta recenica se sastoji samo od reci, odnosno ne pocinje velikim slovom i ne zavrsava se tackom npr.: "it is nice weather today". Svaku od reci u recenici promeniti u skladu sa pig latin pravilima i tako promenjenu recenicu odstampati. Recenica iz primera treba da posle promene postane:
"itway isway icenay eatherway odaytay"

def pig(rec):

    if rec[0] in "aeiou":

        rec += "way"

    else:

        rec = rec[1:] + rec[0] + "ay"

    return rec


def pig_sentence(recenica):

    recenical = recenica.split()

    recenicaln = list()

    for rec in recenical:

        recenicaln.append(pig(rec))

    recenican = " ".join(recenicaln)

    return recenican


def main():

    recenica = input("Unesi recenicu na Engleskom:")

    print( pig_sentence(recenica) )


if __name__ == "__main__":

    main()