a1 = int(input('Digite um número: '))
a2 = int(input('Digite outro valor: '))
a3 = int(input('Digite mais um valor: '))
a4 = int(input('Digite mais outro valor: '))
a5 = int(input('Digite o último valor: '))

numeros = [a1, a2, a3, a4, a5]

print(f'O maior valor é {max(numeros)}, na posição ', end='')
for maior, nome1 in enumerate(numeros):
    if nome1 == max(numeros):
        print(maior+1, end='... ')

print(f'\nO menor valor é {min(numeros)}, na posição ', end='')
for menor, nome2 in enumerate(numeros):
    if nome2 == min(numeros):
        print(menor+1, end='... ')
