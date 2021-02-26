n = 0
soma = 0
v = 0
while n != 999:
    soma += n
    v += 1
    n = int(input('Escreva um número inteiro: '))
v = v - 1
print('Foram {} números e a soma deles foi {}.'.format(v, soma))
