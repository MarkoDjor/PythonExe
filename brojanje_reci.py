#na ulazu korisnik treba da unese tekst. Treba da se napise program koji ce u tom tekstu da izbroje broj reci i da taj broj odstampa na ekranu. Prazna mesta u tekstu se ne racunaju. Npr. ako se unese "Vasa je odlican programer", program treba da odstampa "Broj reci u tekstu je 4"

recenica=input("napisi recenicu:")

rec=recenica.split()

reclasa=len(rec)

print(f"Broj reci u tekstu je {reclasa}")

