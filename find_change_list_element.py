lista = [ 'bananna','lemon','kivi','orange']

if 'lemon' in lista:
    ind = lista.index('lemon')
    lista[ind] = 'potatoe'

print(lista)

lista_j = ', '.join(lista[0:-1])

print( lista_j + " and " + lista[-1] )