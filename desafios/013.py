'''salario = float(input("Digite o salário do funcionário: R$ "))
novo_salario = salario * 1.15
print(f"Novo salário com 15% de aumento: R$ {novo_salario:.2f}")'''

salario = float(input("Digite seu salário atual: R$"))
novoSal = salario + (salario * 15 / 100)
print("Seu novo salário com aumento de 15% é: R$ {}".format(novoSal))