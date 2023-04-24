import math

ca = float(input('Cateto Adjacente: '))
co = float(input('Cateto Oposto: '))

h=math.hypot(ca,co)

print('A hipotenusa é {:.2f}'.format(h))