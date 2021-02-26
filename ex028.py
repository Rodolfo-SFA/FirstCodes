from random import randrange
e = int(input('Digite um número entre 1 a 5: '))
n = randrange(1, 5)
if e == n :
    print('Você acertou! Parabéns. O número que a máquina escolheu é {}, a sua escolha foi {}.'.format(n, e))
else:
    print('Você errou! Tente novamente. O número que máquina escolheu é {}, a sua escolha foi {}.'.format(n, e))
