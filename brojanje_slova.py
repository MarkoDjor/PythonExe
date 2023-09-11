#na ulazu korisnik treba da unese tekst. Treba da se napise program koji ce u tom tekstu da izbroje broj slova i da taj broj odstampa na ekranu. Prazna mesta u tekstu se ne racunaju. Npr. ako se unese "Vasa je odlican programer", program treba da odstampa "Broj slova u tekstu je 22".

recenica=input("napisi recenicu:")

recenical=list(recenica)

reclasa= 0

for slovo in recenical:

    if slovo.isalpha():

        reclasa+= 1

print(f'broj slova u tekstu je "{reclasa}".')


