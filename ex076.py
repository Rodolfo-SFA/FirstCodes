mercadoria = ('Lápis', 5.90, 'Caderno', 11.90, 'Livro', 112.00, 'Lapiseira', 15.90, 'Branquinho', 8.50, 'Bolacha', 2.90, 'Bloco de Notas', 9.00,
              'Cartolina', 1.90, 'Grampeador', 44.90, 'Borracha', 12.00)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for produto in range(0, len(mercadoria), 2):
    print(f'{mercadoria[produto]:.<30}R$ {mercadoria[produto+1]: >7.3f}')
