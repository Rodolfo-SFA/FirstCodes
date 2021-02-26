r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Triângulo EQUILATÉRO!')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('Triângulo ISOSCÉLES!')
    else:
        print('Triângulo ESCALENO!')
else:
    print('Não pode ser formado um triângulo!')
