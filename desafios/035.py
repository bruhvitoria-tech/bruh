r1 = float(input("Digite o valor do comprimento 1: "))
r2 = float(input("Digite o valor do comprimento 2: "))
r3 = float(input("Digite o valor do comprimento 3: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Pode ser formado um triângulo!")
else: 
    print("Não é possivel formar um triangulo...")