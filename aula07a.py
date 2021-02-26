n1: int = int(input('Um valor para calcular:'))
n2 = int(input('Outro valor para calcular:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
sdi = n1 // n2

print('O resultado da soma é {}.\nA multiplicação é {}.\nA divisão é {:.2f}'.format(s,m,d),end='')
print('O exponencial é {}.\nAs sobras da divisão é {}.'.format(e,sdi))

