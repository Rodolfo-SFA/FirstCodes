pt = int(input('Escolha o primeiro termo: '))
razao = int(input('Escolha a razão: '))
decimo  = pt + 10 * razao
for c in range(pt, decimo, razao):
    print('{} '.format(c), end=" -> ")
print('Acabou!')
