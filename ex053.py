frase = str(input('Escreva uma frase: ')).upper().strip()
div = frase.split()
juntar = ''.join(div)
tam = len(juntar)

pal = ''

for c in range(tam - 1, -1, -1):
    pal += juntar[c]

#print(pal, juntar)

if pal == juntar:
    print('A frase normal e ao contrário são iguais. É um palindromo.\n{} = {}'.format(pal, juntar))
else:
    print('Não é um palindromo!')

