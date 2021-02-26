vel = float(input('Qual é a velocidade do carro? '))
if vel > 80:
    acima = vel - 80
    multa = acima * 7
    print('Você ultrapassou o limite de velocidade! A sua velocidade foi {}, a sua multa é {} reais.'.format(vel, multa))
else:
    print('SEM MULTAS!')