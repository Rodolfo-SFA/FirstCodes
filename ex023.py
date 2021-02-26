from random import randrange
#num = str(randrange(0, 9999))
num = str(input('Número: '))
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num[3], num[2], num[1], num[0]))
