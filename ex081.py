cadastro = []
cont = 'S'
nd = 0
while 'S' in cont:
    num = int(input('Digite um valor: '))
    cadastro.append(num)
    nd += 1
    cont = str(input('Deseja continuar [S/N]? ')).strip().upper()

print(f'Resposta 1: Foram digitado {nd} números.')
if 5 in cadastro:
    print(f'Resposta 3: O valor 5 foi digitado e está na posição {cadastro.index(5)}')
else:
    print('Resposta 3: Não há um número 5 cadastrado.')
cadastro.sort(reverse=True)
print(f'Resposta 2: A lista dos valores ordenadas em crescescente é {cadastro}')
