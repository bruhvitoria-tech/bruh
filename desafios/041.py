from datetime import date
atual = date.today().year
nasc = int(input("Digite o ano do seu nascimento: "))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Você é da categoria MIRIM.')

elif idade > 9 and idade <= 14:
    print('Você é da categoria Infantil')

elif idade > 14 and idade <= 19:
    print('Você é da categoria Junior')  

elif idade > 19 and idade <= 20:
    print("A sua categoria é Sênior")

elif idade > 20:
    print('Sua categoria é master.')