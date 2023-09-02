try_list = [ 'tomatoes' , 'potatoes' , 'something' ]

if ( 'potatoes' in try_list ):

    try_list.remove('potatoes')

print(try_list)

try_list.extend(["honey","meat","eggs","bananas"])

try_list.sort()

print( try_list )

try_list.reverse()

print( try_list )

try_list_sorted = sorted( try_list )