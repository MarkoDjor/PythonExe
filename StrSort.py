#In this exercise, you’ll explore this idea by writing a function, strsort, that takes a
#single string as its input and returns a string. The returned string should contain the
#same characters as the input, except that its characters should be sorted in order, from
#the lowest Unicode value to the highest Unicode value. For example, the result of
#invoking strsort('cba') will be the string abc.

#Treba da se napise program za koji korisnik treba da unese string, koji se zatim #sortira. sortirani string treba da se odstampa.

#lista.sort()

tekst = "cba"

tekstnovi=list(tekst)

tekstnovi.sort()

print(tekstnovi)