print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Triângulo formado!')
else:
    print('Triângulo não pode ser formado!')
print('FIM!')