salario = float(input("Digite o valor do seu sálario: "))
casa = float(input(" Digite o preço da casa que deseja comprar: "))
anos = int(input("Qaunto anos será de financiamento?"))

prestacao = casa/ (anos*12)
minimo = salario * 30/100

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end = '')
print('a prestação será de R${:.2f}'. format(prestacao))

if prestacao <= minimo:
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo NEGADO')