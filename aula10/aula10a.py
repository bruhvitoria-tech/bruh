'''nome = str(input('Qual é o seu nome?'))
if nome == 'Bruna':
    print('Que lindo o nome que vc tem! ')
else: 
    print('Seu nome é tão normal...')
print('Bom dia, {}!'.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média média foi: {:.1f}'.format(m))
if m>= 6.0:
    print("Está aprovado. Parabéns!")
else:
    print("Está reprovado...estude mais :)")
