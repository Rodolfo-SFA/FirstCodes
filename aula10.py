n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
#print('PARABÉNS!' if m>=6 else 'ESTUDE MAIS!')
if m>=6:
    print('Parabéns! A sua média foi boa.')
else:
    print('Estude mais! Você não atingiu a média.')
