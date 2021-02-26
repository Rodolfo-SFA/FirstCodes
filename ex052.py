n = int(input('Escreva um número: '))

for primo in (1, n):
    print(n%primo)
    if (n % primo) == 0:
        print('Não é um número primo.')
    else:
        print('É um número primo!')
