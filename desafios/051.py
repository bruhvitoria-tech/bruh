primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimoTermo = primeiro + (10-1)*razao
for c in range (primeiro, decimoTermo + razao, razao):
    print('{} '.format(c), end=' -> ')
print('Acabou')