sal = int(input('Qual é o salário?'))
perc = int(input('Qual é o percentual de aumento?'))
aum = (perc/100)*sal
print('O salário {} mencionado com {:.2f}% é R${:.2f}.'.format(sal,perc,aum))
