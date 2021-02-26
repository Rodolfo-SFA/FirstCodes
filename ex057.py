sexo = str(input('Informe seu sexo: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).upper().strip()[0]

if sexo in 'Mm':
    print('O sexo é masculino.')
elif sexo in 'Ff':
    print('O sexo é feminino')