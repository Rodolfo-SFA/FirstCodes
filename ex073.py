brasileiro = ('São Paulo', 'Atlético-MG', 'Flamengo', 'Internacional', 'Grêmio', 'Palmeiras', 'Fluminense', 'Santos',
              'Corinthians', 'Ceará', 'Athletico-PR', 'Atlético-GO', 'Bragantino', 'Fortaleza', 'Sport',
              'Bahia', 'Vasco', 'Goiás', 'Botafogo', 'Coritiba')

print('-=-'*20)
print(f'A: {brasileiro[0:4]}')
print(f'B: {brasileiro[-4:]}')
print(f'C: {sorted(brasileiro)}')
print('C: {}'.format((brasileiro.index('Fortaleza'))+1))
