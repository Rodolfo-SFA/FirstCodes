pt = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
nt = int(input('Quantos termos quer mostrar? '))
#termo = pt
mais = nt
check = 0
while mais != 0:
    while check != nt:
        check += 1
        print('{} '.format(pt), end='-> ')
        pt += razao
    print('PAUSA!')
    mais = int(input('Quantos termos você quer ver mais? '))
    nt += mais
print('FIM!')
print('Progessão finalizada com {} termos mostrados.'.format(nt))
