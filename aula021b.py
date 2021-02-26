def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')

def teste(b):
    # Escopo local
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}.') # --> Receberá o "a" local
    print(f'B dentro vale {b}.') # --> Receberá o "a" local
    print(f'C dentro vale {c}.') # --> Receberá o "a" local

# Escopo Global
a = 5
teste(a)
print(f'A fora vale {a}') # --> Receberá o "a" local, porém, com o "global 'a'" ele receberá o 'a' global