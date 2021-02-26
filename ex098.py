from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo = -passo
    if inicio < fim:
        for c in range(inicio, fim, passo):
            print(c, end=' ')
            sleep(0.5)
        print('Fim!')
    elif inicio > fim:
        for c in range(inicio, fim, -passo):
            print(c, end=' ')
            sleep(0.5)
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)

inicio = int(input('Escolha o Inicio: '))
fim = int(input('Escolha o Fim: '))
passos = int(input('Escolha os Passos: '))

contador(inicio, fim, passos)

