a = [2, 3, 4, 7]
b = a
c = a[:]

print(f'Resposta 1: {a} e {b}')
print(f'Resposta 2: {c}')

b[2] = 11
c[1] = 15

print(f'Resposta 3: {a} e {b}')
print(f'Resposta 4: {c}')
