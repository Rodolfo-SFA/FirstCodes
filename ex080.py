lista = []
inserir = 0
valor = 0
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if len(lista) == 0 or num >= max(lista):
        lista.append(num)
        print('Inserido no final da lista.')
    else:
        for valor in range(0, len(lista)):
            if num < lista[valor]:
                lista.insert(inserir, num)
                print(f'Inserido na posição {inserir} da lista.')
                inserir = 0
                break
            else:
                inserir += 1
print(f'Os valores inseridos foram: {lista}')

