salario = int(input('Escreva o salário: '))

if salario > 1250:
    perc = 1.1
    aum = salario * perc
else:
    perc = 1.15
    aum = salario * perc
print('O salário aumentou {:.2f}% para {}.'.format((perc-1)*100, aum))
