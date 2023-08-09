def main():

    add2 = lambda x: x + 1

    list_new = [ add2(n) for n in range(1,5) ]

    print( list_new )

    print( list( map( add2 , range(1,5) ) ) )

    list_3 = [ n+1 for n in range(1,5) ]

    print( list_3 )

    print( list( map( lambda n:n+1 , range(1,5) )   )    )

if __name__ == '__main__':

    main()
