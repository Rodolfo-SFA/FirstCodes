plv = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(plv))
print('Só tem espaços?', plv.isspace())
print('É um número?', plv.isnumeric())
print('São apenas letras alfabéticas?', plv.isalpha())
print('É um alfanúmerico?', plv.isalnum())
print('Está em maiúscula?', plv.isupper())
print('Está em minúscula?', plv.islower())
print('Está capitalizada?', plv.isidentifier())
