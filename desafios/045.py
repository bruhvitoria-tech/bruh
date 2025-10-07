from random import randint
itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0,2)
print('O computador escolheu {}'.format(itens[computador]))
print('''Suas opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))

if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador venceu!')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada inválida')

elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('Jogada inválida.')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida')
