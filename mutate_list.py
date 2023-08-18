lista = [ 21 , 33 , 18 , 17 , 35 ]

if 18 in lista:
    ind = lista.index(18)
    lista[ind]=lista[ind] - 1

print(lista)