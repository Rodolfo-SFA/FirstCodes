n = int(input('Escreva um número inteiro: '))
r = n % 2
if r > 0:
    print('O número {} é ímpar.'.format(n))
    print(r)
else:
    print('O número {} é par.'.format(n))