from random import randint
a = randint(1, 100)
b = randint(1, 100)
c = randint(1, 100)
d = randint(1, 100)

tup = (a, b, c, d)

# for cont in range(0, len(tup)):
#     if cont == 0:
#         maior = menor = tup[cont]
#     if maior < tup[cont]:
#         maior = tup[cont]
#     if menor > tup[cont]:
#         menor = tup[cont]

print(f'A tupla criada foi: {tup}')
print(f'O maior número foi {max(tup)} e o menor número foi {min(tup)}.')