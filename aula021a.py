def contador(i, f, p=1):
    """
    --> Faz uma contagem e mostra na tabela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: Contagem
    Função criada pelo Rodolfo.
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

contador(0, 10)
help(contador)