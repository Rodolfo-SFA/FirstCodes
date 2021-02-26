from random import randint
from time import sleep
palpite = list()
numeros = list()
cont = 'S'
while True:
    nump = int(input('Qual o número de palpites que deseja? '))
    for number_guess in range(0, nump):
        while len(numeros) != 6:
            valor = randint(1, 60)
            if valor not in numeros:
                numeros.append(valor)
        palpite.append(numeros[:])
        numeros.clear()
    print('-='*30)
    print('{SORTEANDO JOGOS:^30}')
    print(f'Os {nump} palpites estão abaixo: ')
    for mostrar in range(0, nump):
        print(f'Palpite {mostrar}: {palpite[mostrar]}')
        sleep(0.5)

    cont = str(input('\nDeseja continuar [S/N]? \n')).upper().strip()
    if 'S' not in cont:
        break


