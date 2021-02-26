palavra = ('Maluco beleza', 'marola', 'loucao', 'cheirinho', 'de sexo', 'toma toma', 'sequencia de vapo vapo')

for cont in palavra:
    print(f'\nA palavra {cont.upper()} tem as seguintes vogais: ', end='')
    for pos in cont:
        if pos.lower() in 'aeiou':
            print(pos, end=' ')