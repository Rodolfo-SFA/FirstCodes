lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Resposta 1: Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Resposta 2: Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comidaa in enumerate(lanche):
    print(f'Resposta 3: Eu vou comer {comidaa} na posição {pos}')

#Organiza em ordem alfabetica a "TUPLA", PORÉM... Transforma em "LISTA"
print(sorted(lanche))
print(lanche)