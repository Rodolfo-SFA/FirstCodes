from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
ranking1 = {}

for c in range(0, 5):
    jogadores[f"Jogador {c}"] = randint(1, 6)

for jg, ponto in jogadores.items():
    print(f'O {jg} teve pontuação {ponto}.')
    sleep(0.5)
print(jogadores)
ranking1 = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for rankjg, rankpontos in ranking1:
    print(f'O {rankjg} com o nº {rankpontos}.')
    sleep(1)