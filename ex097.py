def escreva(titulo):
    tam = len(titulo) + 4
    print('~'*tam)
    print(f'{titulo:^{tam}}')
    print('~'*tam)

msg = str(input('Escreva o título: '))
escreva(msg)