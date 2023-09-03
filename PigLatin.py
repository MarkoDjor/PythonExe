# Pig Latin (http://mng.bz/YrON) is a common children’s “secret” language in English-
# speaking countries. (It’s normally secret among children who forget that their parents
# were once children themselves.) The rules for translating words from English into Pig
# Latin are quite simple:
#  If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the
# word. So “air” becomes “airway” and “eat” becomes “eatway.”
#  If the word begins with any other letter, then we take the first letter, put it on
# the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay”
# and “computer” becomes “omputercay.”

#Trazite korisniku da unese neku rec na engleskom.
#Ako rec pocinje sa samoglasnikom ("a","e","i","o","u"), dodaj "way" na kraju reci. Tako da npr. "air" postane "airway", a "eat" postane "eatway". Ako rec pocinje sa bilo kojim drugim slovom, onda uzmemo prvo slovo, stavimo ga na kraj reci i onda dodamo "ay". Tako da npr. "python" postane "ythonpay", a "computer" postane omputercay.

def pig(rec):

    if rec[0] in "aeiou":

        rec += "way"

    else:

        rec = rec[1:] + rec[0] + "ay"

    return rec

def main():

    rec = input("Unesi neku rec na Engleskom:")

    print( pig(rec) )

if __name__ == "__main__":

    main()



