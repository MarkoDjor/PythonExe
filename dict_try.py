lancelot = dict()

lancelot['name'] = "Sir Lancelot"
lancelot['quest'] = "Seek Holy grail"
lancelot['favorit_color'] = "blue"

lancelot_new = {'name': "Sir Lancelot", 'quest': "Seek Holy grail", 'favorit_color': "blue" }

lancelot_new2 = dict( name  = 'Sir Lancelot' , quest = 'Seek Holy Grail' , favorit_color = 'blue' )

arthur = dict( function = 'King' , name = 'Arthur', role = 'protect England' )

arthur2 = {'function': 'King' , 'name': 'Arthur' , 'role': 'protect England' }

arthur3 = {}

arthur3['function'] = 'King'

arthur3[ 'name' ] = 'Arthur'

arthur3[ 'role' ] = 'protect England'

vel = arthur3.get('name','NA')

vel2 = arthur3.get('age','NA')

print(f'vel: {vel}, vel2: {vel2}')

if vel2 == 'NA' and (vel != 'NA'):

    print("OK")