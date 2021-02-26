print('~~'*20)
print('Soma infinita')
print('~~'*20)
while True:
    n = int(input('Número para tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        mult = c * n
        print(f'{n}x{c}={mult}')
    print('-='*20)