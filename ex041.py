nasc_ano = int(input('Ano de Nascimento do Atleta: '))
idade = 2020 - nasc_ano

if idade <= 9:
    print('Categoria MIRIM')
elif 9 < idade <= 14:
    print('Categoria INFATIL')
elif 14 < idade <= 19:
    print('Categoria JUNIOR')
elif 19 < idade <= 20:
    print('Categoria SÊNIOR')
elif idade > 20:
    print('Categoria MASTER')