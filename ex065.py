qtd = 0
continuar = 'S'
n = int(input('Escreva o número: '))
soma = 0
maior = n
menor = n
while continuar in 'SIM':
    continuar = str(input('CONTINUAR [S/N]: ')).upper()
    if continuar in 'SIM':
        n = int(input('Escreva o número: '))
    qtd += 1
    soma += n
    if maior < n:
        maior = n
    if menor > n:
        menor = n
media = soma/qtd
print('A média dos valores é {}, o maior número foi {} e o menor número foi {}.'.format(media, maior, menor))