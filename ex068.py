from random import randint
vit = 0
while True:
    while True:
        ip = str(input('Par ou Impar? ')).upper().strip()
        if ip == 'PAR':
            ip = 'Par'
            break
        elif ip == 'IMPAR':
            ip = 'Impar'
            break
        else:
            print('Opção errada. Escreva PAR ou IMPAR!')
    n = int(input('Escolha um número: '))
    m = randint(0, 10)
    d = m + n
    if (d % 2) == 0 and ip == 'Par':
        vit += 1
        print(f'Você escolheu PAR e ganhou!! A AI escolheu {m} resultando em {d}.')
        print('~~'*20)
    elif (d % 2) != 0 and ip == 'Impar':
        vit += 1
        print(f'Você escolheu IMPAR e ganhou!! A AI escolheu {m} resultando em {d}.')
    else:
        print(f'Você perdeu!! A AI escolheu {m} resultado em {d}.')
        break
print(f'Você ganhou {vit} vezes.')