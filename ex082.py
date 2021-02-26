principal = []
cont = 'S'

while cont == 'S':
    num = int(input('Digite um valor: '))
    principal.append(num)
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()

par = []
impar = []
for valor in principal:
    if (valor % 2) == 0:
        par.append(valor)
    else:
        impar.append(valor)

print(f'A lista principal é {principal}')
print(f'Os valores pares da lista principal são {par}')
print(f'Os valores impares da lista principal são {impar}')