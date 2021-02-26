nome = str(input('Nome Inteiro: '))
a1 = nome.find(' ')
a2 = nome.rfind(' ')

print('{} {}'.format(nome[:a1], nome[a2+1:]))

n = nome.split()
print('{} {}'.format(n[1], n[len(n)]))
