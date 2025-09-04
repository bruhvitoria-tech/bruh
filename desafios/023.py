#num = int(input("Digite um numero entre 0 e 9999."))
#n= = str(num)
#print("Sua unidade é: {}".format(n[3]))
#print("Sua dezena é: {}".format(n[2]))
#print("Sua centena é: {}".format(n[1]))
#print("Sua milhar é: {}".format(n[0]))

num = int(input("Digite um numero entre 0 e 9999: "))
print("Analisando o número {}...". format(num))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10 
m = num // 1000 % 10
print("Sua unidade é: {}".format(u))
print("Sua dezena é: {}".format(d))
print("Sua centena é: {}".format(c))
print("Sua milhar é: {}".format(m))