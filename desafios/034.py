salario = float(input('Digite o seu salário atual: '))

if salario <= 1.250:
    aumento = salario + (salario * 15/100) 
    print('O seu salario ficou R${:.2f}'.format(aumento))
else:
    aumento = salario + (salario * 10/100) 
    print("O seu salário ficou R${:.2f}".format(aumento))