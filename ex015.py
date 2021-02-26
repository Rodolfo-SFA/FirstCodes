#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float (input('Para saber o gasto total, digite quantos KM o carro percorreu? '))
dias = int(input('Quantos dias foi alugados? '))
aluguel = 60*dias
gas = km*0.15
total = aluguel+gas

print('O gasto de aluguel foi {} e o gasto em gasolina foi {}. Resultando no gasto total de {}'.format(aluguel, gas, total))