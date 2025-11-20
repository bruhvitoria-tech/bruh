num = int(input('Digite um número inteiro: '))
c = num
f = 1
print('Calculando {}! = '.format(num))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else '=', end='')
    f = f*c
    c-=1
print('{}'.format(f))
#f = factorial()
#print('O fatorial de {} é {}.'format(n, f))