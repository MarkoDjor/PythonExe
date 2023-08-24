sifra = { 0:5, 8:2, 4:6, 1:9, 7:3, 5:0, 2:8 ,6:4 , 9:1 , 3:7 }

for kljuc,vrednost in sifra.items():
    print( f"{kljuc:15} {vrednost}" )


sifral = list( sifra.values() )

print( sorted(sifral) )


