a1 = int(input('Escreva um número: '))
a2 = int(input('Escreva outro número: '))
a3 = int(input('Escreva mais um número: '))
a4 = int(input('Escreva mais outro número: '))

b = (a1, a2, a3, a4)



if 9 in b:
    print(f'Resposta A: Apareceu {b.count(9)} vezes o número 9.')
elif 9 not in b:
    print('Resposta A: Não apareceu número 9.')
if 3 in b:
    print(f'Resposta B: Apareceu na {b.index(3)+1}º posição o número 3.')
else:
    print('Não há 3 na tupla.')
print('Resposta C: Os valores pares digitados pares foram: ', end='')
for cont in range(0, len(b)):
    if (b[cont] % 2) == 0:
        print(b[cont], end=' / ')


