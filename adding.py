def adding(*argu):

    suma = argu[0]

    for item in argu[1:]:

        suma = suma + item

    return suma


#lista1 = [ 1 , 6 , 12 , 28 , 14 , 23 ]

lista1 = 'abcd'

#lista2 = [ 12, 18, 21, 11, 8 ]

lista2 = 'efgh'

lista3 = 'ijk'

suma = adding( lista1 , lista2 , lista3 )

print( suma )