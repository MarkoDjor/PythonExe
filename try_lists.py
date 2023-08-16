def indeks(elem,lista):
    if elem in lista:
        print(f"{elem} is in the position {lista.index(elem)} in the list.")

        return lista.index(elem)

    else:
        print(f"No {elem} in the list.")

def main():

    lista = [ "mama" , "tata" ]

    elem = "tata"

    pos = indeks(elem , lista )

    print( pos + 1 )

if __name__ == "__main__":

    main()