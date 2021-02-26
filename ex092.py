from datetime import datetime

DataAtual = datetime.today().year

pessoas = {}

pessoas['Nome'] = str(input('Nome: '))
Ano = int(input('Ano de Nascimento: '))
idadep = DataAtual - Ano
pessoas['Idade'] = idadep
pessoas['Carteira de Trabalho'] = int(input('Carteira de Trabalho: '))
if pessoas["Carteira de Trabalho"] != 0:
    pessoas['Ano de Contratação'] = int(input('Ano de Contratação: '))
    pessoas['Aposentar'] = pessoas["Idade"] + 35

for k, v in pessoas.items():
    print(f'{k} é {v}.')