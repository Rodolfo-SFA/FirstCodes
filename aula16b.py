a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a

print(f'Resposta 0: {c}')
print(f'Resposta 1: {len(c)}')
print(f'Resposta 2: {c.count(5)}')
print(f'Resposta 3: {c.count(9)}')
print(f'Resposta 4: {c.index(4)}')
print(f'Resposta 5: {c.index(2)}')
print(f'Resposta 6: {c.index(2, 4)}')
print(f'Resposta 7: {c.index(5, 1)}')

pessoa = ('Gustavo', 39, 'M', 99.88)
print(f'Resposta 8: {pessoa}')

del(pessoa)
print(pessoa)