km = int(input('Quantos KM foram a viagem: '))
if km > 200:
    pagar = km * 0.45
    print('A KM da viagem é {} km, então o valor da passagem é {:.2f} reais.'.format(km, pagar))
else:
    pagar = km * 0.50
    print('A KM da viagem é {} km, então o valor da passagem é {:.2f} reais.'.format(km, pagar))