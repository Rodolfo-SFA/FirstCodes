ano = int(input('Escreva o ano: '))
bis = ano % 4
if bis == 0:
    print('O ano de {} é bissexto.'.format(ano))
else:
    print('O ano de {} não é bissexto.'.format(ano))
