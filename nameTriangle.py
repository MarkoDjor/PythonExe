#Write a program that asks the user for their name and then produces a “name
#triangle”: the first letter of their name, then the first two letters, then #the first
#three, and so forth, until the entire name is written on the final line.

#Napisi program koji korisnika pita za ime a onda na ekranu stampa "trougao imena": prvo #slovo prvog imena, onda prva dva slova imena u drugom redu, zatim prva tri slova u #trecem redu i tako dalje, sve dok citavo ime ne bude napisano u zavrsnoj liniji.

ime=input("Unesi ime:")



vasa=""

for i in range(len(ime)):
    vasa+= ime [:i + 1] + "\n"

print(vasa)











#print( " kako se zoves")


#for broj,elem in enumerate(ime):


    #print(f"{broj}. {elem+1}")