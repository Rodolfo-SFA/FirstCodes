pessoas = {'nome': 'Rodolfo', 'sexo': 'M', 'idade': 25}

print(f'Resposta 1: {pessoas.values()}')
print(f'Resposta 2: {pessoas.keys()}')
print(f'Resposta 3: {pessoas.items()}')
print(f'Resposta 4: O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

for k in pessoas.keys():
    print(f'Resposta 5: {k}')

for v in pessoas.values():
    print(f'Resposta 6: {v}')

for k, v in pessoas.items():
    print(f'Resposta 7: {k} = {v}')

pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'Resposta 7: {k} = {v}')

del pessoas['sexo']
for k, v in pessoas.items():
    print(f'Resposta 8: {k} = {v}')

pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'Resposta 9: {k} = {v}')