from random import randint
from time import sleep 
computador = randint(0,5)
print('*' * 20)
print("Vou pensar em um número de 0 a 5...")
print("*" * 20)
jogador = int(input("Em que número eu pensei?")) 
print("Processando...")
sleep(3)
if jogador == computador:
    print("Venceu!")
else:
    print("Perdeu... eu pensei no número {} e não no {}".format(computador, jogador))