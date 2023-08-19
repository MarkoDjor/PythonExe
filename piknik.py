#lista = ["salad", "chips","potatoes","pizza", "tomatoes", "cake", "soda", "water"]
import cython
import numpy as np

vektor = np.arange(1,11)

print(vektor)

lista = ["cake", "salad"]
if len(lista) == 0:

    print("Ne brini, Vule Vu ce nam doneti svedski sto.")

elif len(lista) == 1:
    print(f"You are bringing {lista[0]}.")

elif len(lista) == 2:

    print(f"You are bringing {lista[0]} and {lista[1]}.")

else:
    lista[-1]="and " + lista[-1]
    listal=", ".join(lista)
    print(f"You are bringing {listal}.")



