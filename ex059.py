esc = 6
n1 = float(input('Escolha o primeiro valor: '))
n2 = float(input('Escolha o segundo valor: '))

n3 = 0

while esc != 5:
    print('''   -=-=-=-=-=-=-=-
    [1] SOMA
    [2] MULTIPLIFICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    -=-=-=-=-=-=-=-''')
    esc = int(input('Escolha um opção: '))
    if esc == 1:
        n3 = n1 + n2
        print('OPÇÃO [1] SOMA: A soma dos valores é {}.'.format(n3))
    elif esc == 2:
        n3 = n1 * n2
        print('OPÇÃO [2] MULTIPLIFICADOR: O produto dos números escolhidos é {}'.format(n3))
    elif esc == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
        elif n2 > n1:
            print('O maior número é {}.'.format(n2))
        else:
            print('Os valores são iguais.')
    if esc == 4:
        n1 = float(input('Escolha um novo valor: '))
        n2 = float(input('Escolha outro valor: '))
    if esc > 5:
        print('OPÇÃO INVÁLIDA. Aperte 5 para caso queira SAIR DO PROGRAMA')