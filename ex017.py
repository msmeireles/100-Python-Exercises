#opo = float(input('Cateto oposto: '))
#adj = float(input('Cateto adjacente: '))
#hip = ((opo)**2+(adj)**2)**(1/2)
#print('A hipotenusa do respectivo triângulo retângulo vale {}.'.format(hip))

import math
opo = float(input('Cateto oposto: '))
adj = float(input('Cateto adjacente: '))
hip = math.hypot(opo, adj)
print('A hipotenusa do respectivo triângulo retângulo vale {}.'.format(hip))


