#Napisi funkciju koja na ulazu uzima niz brojeva. Na izlazu treba da se dobije #rezultat naizmenicnog sabiranja i oduzimanja brojeva jednih od drugih. Na primer ako je ulazni niz brojeva [10, 20, 30, 40, 50, 60], rezultat treba da bude: 10+20-30+40-50+60.

#10-20+30-40+50-60.

lista = [ 10, 20, 30, 40, 50, 60, 50  ]

istal=sum(lista[0::2]) - sum(lista[1::2])


print(istal)