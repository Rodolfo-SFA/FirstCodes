cont = 'S'
consolidado = list()
pessoa = list()
#pesototal = cadastros = 0
acima = abaixo = cadastro = 0
acimalist = list()
abaixolist = list()

while 'S' in cont:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    consolidado.append(pessoa[:])
    pessoa.clear()
    cont = str(input('Deseja continuar [S/N]: ')).strip().upper()
    cadastro +=1

for c in range(0, len(consolidado)):
    if c == 0:
        acima = abaixo = consolidado[c][1]
    if acima < consolidado[c][1]:
        acima = consolidado[c][1]
    elif abaixo >= consolidado[c][1]:
        abaixo = consolidado[c][1]

for m in consolidado:
    if m[1] == acima:
        acimalist.append(m[0])
    elif m[1] == abaixo:
        abaixolist.append(m[0])

print(f'O número de clientes cadastrados foram {cadastro}.')
print(f'O maior peso foi {acima} dos clientes {*acimalist}.')
print(f'O menor peso foi {abaixo} dos clientes {*abaixolist}.')