str_l = [ "Petra" , "Vasa" , "Magdalena" , "Marko" ]

str_l_super = list( map( lambda name:"Super "+name , str_l ) )

print(str_l_super)

name_marko = str_l_super.pop()

print(f"""Cool porodica je: "{', '.join(str_l_super)} i {name_marko}." """)

