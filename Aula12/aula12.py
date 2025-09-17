nome = str(input('Qual é o seu nome? '))
if nome == 'Bruna':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Jessicaine':
    print("Voces pertencem a comunidade colorida...")
elif nome in 'Ana Claudia Ana Paula Claudia':
    print('Voces possuem nomes em comum.')
else:
    print("Seu nome é comum >-<")

print('Tenha um bom dia {}'.format(nome))