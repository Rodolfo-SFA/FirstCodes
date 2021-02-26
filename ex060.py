n1 = int(input('Escreva um número para saber seu FATORIAL: '))
n2 = 1
n3 = 1

while n2 != n1:
    n2 += 1
    n3 *= n2

print('O valor fatorial de {}! é {}.'.format(n1, n3))