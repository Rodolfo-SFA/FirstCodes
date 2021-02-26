oldname = ''
soma = 0
num = 0
mulher = 0

for p in range(1, 5):
    nome = str(input('Nome da Pessoa {}: '.format(p)))
    idade = int(input('Idade da Pessoa {}: '.format(p)))
    sexo = str(input('Sexo da Pessoa {} (M ou F): '.format(p)))

    soma += idade
    num += 1

    if sexo == 'F' and idade < 20:
        mulher += 1

    if sexo == 'M':
        if oldname == '':
            velho = idade
            oldname = nome
        else:
            if velho < idade:
                oldname = nome

media = soma/num
print('O homem mais velho é {}.'.format(oldname))
print('A média de idade é {}.'.format(media))
print('O número de mulher é {}'.format(mulher))