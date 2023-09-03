#In Ubbi Dubbi, every vowel (a, e, i, o, or u) is prefaced with ub. Thus milk becomes
#mubilk and program becomes prubogrubam. So if the function is called with octopus, the #function will return the string uboctubopubus. And if the user passes the argument #elephant, you’ll output ubelubephubant.

#Korisnik treba da unese rec koja zatim treba da se prevede u Ubbi-Dubbi dijalekat. U Ubbi-Dubi dijalektu ispred samoglasnika (a, e, i, o, u) treba da se stavi "ub". Tako da rec "octopus" postane "uboctubopubus", a "elephant" postane "ubelubephubant".

ubbi=input("unesi rec:")

list(ubbi)

ubbid=()

if  ubbi[0] in ["a","e", "i","u","o"]:

    ubbid= "ub" + ubbi

else:

    ubbid=  ubbi[1:] + ubbi[0] + "ay"

    #recl=r


print(ubbid)

" ".join(ubbid)