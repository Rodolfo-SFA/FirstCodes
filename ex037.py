N1 = int(input('Escreva o primeiro valor: '))
N2 = int(input('Escreva o segundo valor: '))

if N1 > N2:
    print('O primeiro valor {} é maior que o segundo {}.'.format(N1, N2))
elif N1 < N2:
    print('O segundo valor {} é maior que o primeiro {}.'.format(N2, N1))
elif N1 == N2:
    print('Os dois valores são iguais. {}'.format(N1))
