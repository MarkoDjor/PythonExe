import random as rnd

def main():

    n,a,s = 2,2,1

    adjectives = [ "false", "ruinous", "filthsome", "caterwauling" , "toad-spotted" , "cullionly" , "rotten" , "caterwauling" ]

    nouns = [ "slave" , "villian" , "traitor" , "lunatic" , "harpy" ]

    print( n, a , s)

    rnd.seed(s)

    for i in range(1,n+1):

        text = "You "

        for j in range(1,a+1):

            adj = rnd.choice(adjectives)

            if j == a:

                text += adj + " "

            else:

                text += adj + ", "


        noun = rnd.choice(nouns)

        text += noun + "."

        print( text )

if  __name__ == '__main__':

    main()