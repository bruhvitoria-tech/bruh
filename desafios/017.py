"""from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))  
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))"""

from math import pow,sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = sqrt(pow(co,2) + pow(ca,2))
print('A hipotenusa vai medir {:.2f}'.format(hi))
