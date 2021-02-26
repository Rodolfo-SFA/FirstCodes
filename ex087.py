from typing import List, Any

matriz = [[], [], []]
par = col = 0
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite o valor da posição [{l}, {c}]: '))
        matriz[l].append(num)
#print(matriz)
for mostrar, posic in enumerate(matriz):
    for an in range(0, len(matriz[mostrar])):
        print(f'[  {posic[an]}  ]', end=' ')
    print('')

for lpar in matriz:
    for cpar in lpar:
        if (cpar % 2) == 0:
            par += cpar

for m in matriz:
     col += m[2]

print(f'Resposta 1: A soma dos valores pares é {par}.')
print(f'Resposta 2: O maior valor da segunda coluna é {max(matriz[1])}.')
print(f'Resposta 3: A soma dos valores da terceira coluna é {col}')