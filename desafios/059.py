num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
opcao = 0
while opcao != 5:
    print('''
    [1] Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números 
    [5]Sair do programa''')
    opcao = int(input('Qual é a sua opção?'))
    if opcao == 1:
        num3 = num1+num2
        print('Esse é o resultado da soma: {}'.format(num3))
    elif opcao == 2:
        num3 = num1*num2
        print('Esse é o resultado da multiplicação: {}'.format(num3))
    elif opcao == 3:
        if num1 > num2:
            maior =num1
        else: maior = num2
        print('Entre o valor do {} e do {}, o maior valor foi: {}'.format(num1,num2, maior))
    elif opcao == 4:
        print('Informe novamente os números: ')
        num1 = int(input('Primeiro número: '))
        num2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
print('Fim do programa! Volte sempre!')
