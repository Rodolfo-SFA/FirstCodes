from datetime import date
maior = 0
menor = 0
atual = date.today().year

for ano in range(1,8):
    dt = int(input('Data de Nascimento {}: '.format(ano)))
    idade = atual - dt

    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1

print('Temos {} pessoas menores de idade e {} maiores de idade.'.format(menor, maior))