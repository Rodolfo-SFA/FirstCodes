matriz = [[], [], []]

for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite o valor da posição [{l}, {c}]: '))
        matriz[l].append(num)
#print(matriz)
for mostrar, posic in enumerate(matriz):
    for an in range(0, len(matriz[mostrar])):
        print(f'[  {posic[an]}  ]', end=' ')
    print('')