animal = "octopus"

animal_c = ""

for i,lett in enumerate(animal):

    if i==4:

        animal_c = animal_c + "P"

    else:

        animal_c = animal_c + lett

print(animal_c)