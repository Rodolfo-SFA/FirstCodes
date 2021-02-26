from time import sleep
ap = {}
gols = []

ap['nome'] = str(input('Nome do Jogador: '))
ap['njogos'] = int(input('Número de Jogos: '))

for g in range(0, ap['njogos']):
    ngol = int(input(f'Nº de Gols na partida {g}: '))
    gols.append(ngol)
ap['gols'] = gols
ap['total'] = sum(ap["gols"])

print('-='*40)
print(f'{ap}')
print('-='*40)

# for k, v in ap:
#     print(f'O {k} é {v}.')

print('-='*40)
print(f'O jogador {ap["nome"]} que fez {ap["njogos"]} partidas.')
for c, n in enumerate(ap["gols"]):
    print(f'A partida {c} foram {n} gols.')
    sleep(0.5)

print(f'O número total de gols foi {ap["total"]}.')