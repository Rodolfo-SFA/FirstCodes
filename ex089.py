escola = list()
alunoinfo = list()
aluno = list()
nota = list()
cont = 'S'
while 'S' in cont:
    nome = str(input('Nome: '))
    aluno.append(nome)
    alunoinfo.append(aluno[:])

    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    nota.append(n1)
    nota.append(n2)
    alunoinfo.append(nota[:])
    escola.append(alunoinfo[:])

    aluno.clear()
    nota.clear()
    alunoinfo.clear()

    cont = str(input('Deseja continuar [S/N]? ')).upper().strip()
print(escola)
print('-=-'*20)
print(f'{"No.":<4} {"Nome":<10} {"Média":^6}')
for pos, lista in enumerate(escola):
    print(f'{pos:<4} {lista[0][0]:<10} {(sum(lista[1])/2):<6.2f}')
