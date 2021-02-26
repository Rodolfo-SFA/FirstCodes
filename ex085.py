numeros = [[], []]

for c in range(0, 7):
    num = int(input('Digite um valor: '))
    if (num % 2) == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(numeros)
