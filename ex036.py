valor_casa = int(input('Valor da casa: '))
valor_sal_comp = int(input('Salário do Comprador: '))
anos_pag = int(input('Tempo em Anos para pagar: '))
meses_pag = anos_pag * 12

pag_mes = valor_casa/meses_pag
valor_ideal = valor_sal_comp * 0.3

if valor_ideal < pag_mes:
    tempo_ideal = (valor_casa // valor_sal_comp) + 1
    print('O empréstimo não foi aprovado. Aconselhamos o pagamento de {:.2f} meses com mensalidade {:.1f} reais.'.format(tempo_ideal, valor_ideal))
elif valor_ideal >= pag_mes:
    print('O valor está aprovado. O pagamento da casa será realizado em {:.1f} meses com valores mensais de {:.2f} reais.'.format(meses_pag, pag_mes))