ns = int(input('Quantos números da cadeia de Fibonnaci gostaria de ver? '))
n1 = 0
n2 = 1
qtd = 1
mais = ns
n3 = n1 + n2
print('{} --> {}'.format(n1, n2), end=' --> ')
while mais != 0:
    while qtd != mais:
        print('{} '.format(n3), end='--> ')
        n1 = n2
        n2 = n3
        n3 = n1 + n2
        qtd += 1
    qtd = 0
    print('PAUSA!')
    mais = int(input('Gostaria mais quantas sequências de Fibonnaci? '))
print('FIM!')
