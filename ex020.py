import random
#a1 = str(input('Primeiro aluno: '))
#a2 = str(input('Segundo aluno: '))
#a3 = str(input('Terceiro aluno: '))
#a4 = str(input('Quarto aluno: '))
#lista = [a1, a2, a3, a4]
#ord = random.shuffle(lista)
#shuffle(lista)

lista = 'Maria João José Gabriel'.split()
random.shuffle(lista)

print(lista)