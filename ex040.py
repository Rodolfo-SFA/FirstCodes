n1 = int(input('Primeira Nota: '))
n2 = int(input('Segunda Nota: '))

m = (n1 + n2) / 2

if m < 5:
    print('Reprovado!')
elif 5 <= m < 7:
    print('Recuperação!')
elif m >= 7:
    print('Aprovado!')