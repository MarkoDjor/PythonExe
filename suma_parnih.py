#Napisi funkciju koja na ulazu uzima listu brojeva. Nadji sumu svih brojeva #sa parnim indeksima (nulti, drugi, cetvrti) u listi. Lista na inputu moze biti razlicite duzine (odnosno da ne bude duzine 6).

lista = [ 10, 20, 30, 40, 50, 60 ]

listal=lista[::2]

pinsum=sum(listal)

print(pinsum)