velCar = float(input("Digite a velocidade do seu carro no momento: "))
if velCar>80:
    multa = (velCar-80) * 7
    print("Voce foi multado... o valor da multa ficará: R${:.2f}".format(multa))
else:
    print('Tenha uma ótima viagem com segurança!')

