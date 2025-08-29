"""from math import pow,sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = sqrt(pow(co,2) + pow(ca,2))
print('A hipotenusa vai medir {:.2f}'.format(hi))

ang = float(input("Digite o valor do ângulo:  "))
sen = co/hi
cos = ca/hi
tg = co/ca

print("Aqui está o Sen {}, Cos {} e Tg {} desse ângulo.".format(sen,cos,tg))"""

from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: ')) 
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tangente))
