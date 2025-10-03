preco = float(input('Digite o valor do produto: R$ '))
print('''Escolha uma opção de pagamento:
[1] Á vista no dinheiro/cheque
[2] Á vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input('Sua opção: '))
if opcao == 1:
    novoPrec = preco - (preco * 10/100)
    print('Á vista no dinheiro/cheque, o produto que custava R${}, vai custar R${}.'.format(preco, novoPrec))
elif opcao == 2:
    novoPrec = preco - (preco * 5/100)
    print('Á vista no cartão, o produto que custava R${}, vai custar R${}.'.format(preco, novoPrec))
elif opcao == 3:
        print('Em até 2x no cartão, o produto vai manter o preço de R${}.'.format(preco))
        novoPrec = preco/2
        print('Ficará com parcelas de R${}'.format(novoPrec))
elif opcao == 4:
         novoPrec = preco + (preco * 20/100)
         print('Parcelado em 3x ou mais, o produto vai ter juros de 20%, custando R${}.'.format(novoPrec))


