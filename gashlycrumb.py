def lower_list(s_list):

    letters_s = []

    for lett in s_list:

        letters_s.append( lett.lower() )

    return letters_s

fh = open('gashlycrumb.txt', 'rt')

letters = [ "A" , "Be" ]

letters_s = lower_list( letters )

ghostly_dict = dict()

for lines in fh:

    letter = lower_list( lines.strip() )[0]

    ghostly_dict[letter] = lines.strip()

fh.close()

for elements in ghostly_dict.items():

    print( elements )

for lett in letters_s:

    if lett in ghostly_dict.keys():

        print( ghostly_dict[lett] )

