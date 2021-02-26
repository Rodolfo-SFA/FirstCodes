pt = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termos = 0
while termos != 10:
    termos += 1
    print('{} '.format(pt), end='-> ')
    pt += razao
print('Acabou!')w