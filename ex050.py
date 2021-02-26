m = 0
for soma in range(1, 7):
    n = int(input('Escolha um número: '))

    if (n % 2) == 0:
        m += n

print(m)