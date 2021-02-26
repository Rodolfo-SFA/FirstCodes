numeros = []
continua = 'S'

while 'S' in continua:
    num = int(input('Digite um número para cadastro: '))
    if num in numeros:
        print('O número já está cadastrado.')
    else:
        numeros.append(num)
        print(f'Valor {num} cadastrado.')
    continua = str(input('Deseja continuar [S/N]? ')).strip().upper()
numeros.sort()
print(f'Os números cadastrados foram {numeros}')