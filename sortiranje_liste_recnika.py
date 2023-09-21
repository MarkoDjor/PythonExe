PEOPLE = [{'first':'Reuven', 'last':'Lerner',
'email':'reuven@lerner.co.il'},
{'first':'Donald', 'last':'Trump',
'email':'president@whitehouse.gov'},
{'first':'Vladimir', 'last':'Putin',
'email':'president@kremvax.ru'}
]

lastl = []

for dict in PEOPLE:

    lastl.append(dict["last"])

lastl.sort()

print(lastl)

people_s = []

for i in range(len(PEOPLE)):

    for dict in PEOPLE:

        if lastl[i] in dict.values():

           people_s.append(dict)

print( people_s )