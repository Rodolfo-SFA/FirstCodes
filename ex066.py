v = 0
soma = 0
while True:
    n = int(input('Escolha um número: '))
    if n == 999:
        break
    v += 1
    soma += n
print(f'A soma dos {v} é {soma}.')
