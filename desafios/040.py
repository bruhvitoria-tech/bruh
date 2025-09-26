nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5:
    
    print("Sua nota foi {}, média abaixo de 5.0: Reprovado".format(media))

elif 7 > media >= 5:
    print('Sua nota foi {} \nEstá de Recuperação'.format(media))

elif media >= 7:
    print('Sua nota foi {} \nEstá aprovado!!'.format(media))
