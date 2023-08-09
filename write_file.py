file = '/home/marko/Documents/tiny_python_projects/for_my_trial/output.txt'

fh_w = open( file , 'wt')

fh_w.write('Do not make that mistake again!\n')

fh_w.close()

text_check = open( file ).read()

print(text_check)
