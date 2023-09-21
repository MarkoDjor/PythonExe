def is_convertible_int(rec):

    try:
        int(rec)
        return True
    except ValueError:
        return False

lista = ( 10, 20, 'a', '30', 'bcd' )

suma = 0

for elem in lista:

    if is_convertible_int(elem):

        suma += int(elem)

print( f'suma brojeva u listi je {suma}')