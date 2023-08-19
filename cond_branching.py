lista = [ "salad" , "cake" , "meat" , "apple" ]

#listal = []

#for ime in lista:

#    listal.append( ime.capitalize() )

#listal = [ ime.capitalize() for ime in lista ]

lista[-1] = "and " + lista[-1]

listas = ", ".join(lista)

print( "You are bringing " + listas + ".")

print(f"You are bringing {listas}.")

print("You are bringing {}.".format(listas) )