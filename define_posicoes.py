def define_posicoes(linha, coluna, orientacao, tamanho):
    saida = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            term = [linha+i, coluna]
            saida.append(term)
        else:
            term = [linha, coluna+i]
            saida.append(term)
    return saida