import numpy as np

a,b,c = -3,11,21

while (b**2-4*a*c)>0:

    x = ( -b + np.sqrt(b**2-4*a*c) )/(2*a)

    a = a -1

    print( f"value of a: {a:0.4f}, value of x: {x:0.4f}" )

