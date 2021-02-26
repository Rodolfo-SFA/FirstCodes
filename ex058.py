from random import randint
from time import sleep
n1 = int(input('Escolha um número entre 0 e 10: '))
sleep(1)
n2 = randint(0, 10)

n3 = 1
while n1 != n2:
    n1 = int(input('O jogo escolheu o número {} e você o número {}. Tente novamente, escolha um número entre 0 e 10: '.format(n1, n2)))
    sleep(1)
    n2 = randint(0, 10)
    n3 += 1

print('Parabéns! O número escolhido foi {}. Você precisou de {} tentativas para ganhar.'.format(n1, n3))