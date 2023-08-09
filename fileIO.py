import os

file = '/home/marko/Documents/tiny_python_projects/for_my_trial/howler_text.txt'

#file = '/home/marko/Documents/tiny_python_projects/for_my_trial/something.txt'

if os.path.isfile( file ):

    text = open(file).read().strip().upper()

    #text = fh.read()

    print( text )
