num = [2, 5, 9, 1]
num[2] = 3
print(f'Resposta 1: {num}')
num.append(7)
print(f'Resposta 2: {num}')
num.sort()
print(f'Resposta 3: {num}')
num.sort(reverse=True)
print(f'Resposta 4: {num}')
num.insert(6, 5)
print(f'Resposta 5: {num}')
num.pop(3)
print(f'Resposta 6: {num}')
num.remove(5) #Vai remover apenas o primeiro valor de 5 que encontrar.
print(f'Resposta 7: {num}')
