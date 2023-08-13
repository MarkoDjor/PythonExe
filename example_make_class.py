class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):

        return "Woof"

dog1 = Dog("Debora",4)

dog2 = Dog("Dona",2)

print( f'The first dog is {dog1.name} and it is {dog1.age} years old!: She says {dog1.bark()}.' )

print( f'The seconf dog is {dog2.name} and it is {dog2.age} years old!: She also says {dog2.bark().}' )
