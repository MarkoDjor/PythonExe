#food = [ 'banana' , 'potatoe' , 'tomatoe' , 'onion' ]

food = ['tomatoe' , 'onion' ]

s = 0

if s:
    food.sort()

lena = len(food)

if lena == 1:

    print( f'You are bringing {food[0]}.')

elif lena ==2:

    print(f'You are bringing {food[0]} and {food[1]}.')

else:

    text = ''

    i = 0

    for word in food:

        if i == lena - 1:

            text = text + ' and ' + word

        elif i == 0:

            text = text + word

        else:

            text = text + ', ' + word

        i = i + 1

    print(f'You are bringing {text}.')
