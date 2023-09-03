#napisi program koji za listu datu ispod stampa elemnte te liste ispisuje zajedno sa rednim brojevima u listi. Redni brojevi treba da budu takvi da je prvi element u listi 1 (ne nula). Dakle izlaz programa treba da bude:
#1. <vrednost prvog elementa u listi>
#2. <vrednost drugog elementa u listi>
#....
#Za resenje zadatka koristi enumerate funkciju.

lista = [ "1" , "5" , "8" , "17" ]

for broj,elem in enumerate(lista):

    print(f"{broj+1}. {elem}")