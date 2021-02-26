aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
print(f'Nome é igual a {aluno["Nome"]}.')
print(f'A média é igual a {aluno["Média"]}.')
if aluno["Média"] >= 7:
    aluno['Situação'] = 'Aprovado'
    print(f'Situação do aluno é {aluno["Situação"]}.')
else:
    aluno['Situação'] = 'Reprovado'
    print(f'Situação do aluno é {aluno["Situação"]}`')