sexo = str(input('Digite o seu sexo: [M/F]')).strip().upper()[0]
#print(sexo)
while sexo not in  'MmFf':
    sexo = str(input('Dados inválidos!\nPor favor, informw seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'. format(sexo))
