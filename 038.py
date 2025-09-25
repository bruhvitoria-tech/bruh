num = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite um outro numero inteiro: '))

if num> num2:
    print('O valor maior é o primeiro: {}'.format(num))
elif num2> num:
    print('O maior valor é o segundo:{}'.format(num2))
else:
    print('Não existe valor maior, os dois são iguais.')