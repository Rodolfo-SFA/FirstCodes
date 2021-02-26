formula = str(input('Escreva a formula que deseja analisar: '))
formlist = []

for c in range(0, len(formula)):
    formlist.append(formula[c])

if formlist.count('(') == formlist.count(')'):
    print('A expressão está correta.')
else:
    print('A expressão está incorreta. Tente novamente.')