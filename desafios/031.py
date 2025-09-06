distancia = float(input('Digite a distância em Km da viagem: '))
if distancia <= 200:
    preco = distancia * 0.50
    print("O valor da passagem será de R${:.2f}".format(preco))
else:
    preco = distancia * 0.45
    print('O valor da passagem será de R${:.2f}'.format(preco))