cont = 'S'
pessoa = {}
cadastros = []
np = ni = 0
while 'S' in cont:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo [M/F]: '))
    pessoa['Idade'] = int(input('Idade: '))
    cadastros.append(pessoa.copy())
    cont = str(input('Deseja continuar [S/N]? ')).upper().strip()
    np += 1
    ni += pessoa["Idade"]

media = ni / np
print(f'O grupo tem {np} pessoas cadastradas.')
print(f'A média de idade é {media}.')
print(f'A mulheres do grupo são: ', end='')
for c in cadastros:
    if c["Sexo"] == 'F':
        print(c["Nome"], end='')

print(f'As pessoas acima da média de idade são: ', end='')
for m in cadastros:
    if m["Idade"] > media:
        print(m["Nome"], end='')
#print(f'O grupo tem {count(cadastros)}.')
#print(f'A média de idade é {}')