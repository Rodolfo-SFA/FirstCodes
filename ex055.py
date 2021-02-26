m = 0
n = 0

for peso in range(1, 6):
    p = float(input('Peso da Pessoa {}: '.format(peso)))
    if peso == 1:
        m = p
        n = p
    else:
        if m > p:
            m = p
        if n < p:
            n = p

print('O maior peso é {} e o menor peso é {}.'.format(m, n))